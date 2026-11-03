"""Stage audited catalog records without changing their original source files."""
from copy import deepcopy
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

from build import canonical_url

AUDIT_DATE = '2026-11-03'


def audit_rows(payload):
    if isinstance(payload, list):
        return payload, None
    if isinstance(payload, dict) and isinstance(payload.get('items'), list):
        return payload['items'], payload.get('date')
    raise ValueError('Audit must be an array or an object containing items')


def index_audits(payloads, fallback_date=None):
    indexed = {}
    for payload in payloads:
        rows, date = audit_rows(payload)
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get('url'), str):
                raise ValueError('Audit record requires a string URL')
            normalized = dict(row, url=canonical_url(row['url']))
            resolved_date = row.get('checked_at') or date or fallback_date
            value = (normalized, resolved_date)
            if normalized['url'] in indexed and indexed[normalized['url']] != value:
                raise ValueError('Conflicting audit for URL: ' + normalized['url'])
            indexed[normalized['url']] = value
    return indexed


def promote(source, review, identity, date):
    item = deepcopy(source)
    original_url = canonical_url(source['url'])
    item['url'] = canonical_url(review.get('replacement_url') or original_url)
    item['stable_id'] = identity
    for source_key, target_key in [('suggested_name', 'name'), ('suggested_description', 'description'), ('access_notes', 'access_notes'), ('kind', 'kind')]:
        if review.get(source_key) or (source_key == 'access_notes' and review.get(source_key) == ''):
            item[target_key] = review[source_key]
    if urlsplit(item['url']).path.lower().endswith(('.mp4', '.webm', '.mov')):
        item['kind'] = '视频'
    if review.get('replacement_url') and item.get('kind') == '视频':
        host = urlsplit(item['url']).hostname or ''
        item['platform'] = 'YouTube' if host in ('youtube.com', 'www.youtube.com', 'youtu.be') else 'B站' if host == 'bilibili.com' or host.endswith('.bilibili.com') else '独立站'
    item['browser_verified'] = True
    item['visual_verified'] = True
    # Admitted video audits require actual playback; an explicit audit exception wins.
    item['playback_verified'] = item.get('kind') == '视频' and review.get('playback_verified', True) is True
    item['review_status'] = 'verified'
    item['checked_at'] = review.get('checked_at') or date
    item['verification'] = ('本轮实际播放片段核查' if item['playback_verified'] else
                            '本轮实际画面核查（未验证播放）' if item.get('kind') == '视频' else
                            '本轮实际画面与关键操作核查')
    for field in ('action', 'observed', 'notes'):
        item['verification_' + field] = review.get(field, '')
    item['audit'] = dict(deepcopy(review), original_url=original_url, verified_url=item['url'], checked_at=item['checked_at'])
    item['original_url'] = original_url
    return item


def assemble(manifest, sources, baseline_audit, candidates=None, candidate_audits=None, audit_date=None):
    if audit_date is not None and audit_date != AUDIT_DATE:
        raise ValueError('This release requires audit date ' + AUDIT_DATE)
    by_url = index_audits([baseline_audit], audit_date)
    manifest_urls, manifest_ids = set(), set()
    source_index = {}
    for name, records in sources.items():
        source_index[name] = {}
        for record in records:
            url = canonical_url(record['url'])
            if url in source_index[name]:
                raise ValueError('Duplicate source URL in ' + name + ': ' + url)
            source_index[name][url] = record
    for entry in manifest:
        url = canonical_url(entry['url'])
        if not isinstance(entry.get('id'), str) or not re.fullmatch(r'ui-[0-9a-f]{12}', entry['id']):
            raise ValueError('Invalid baseline stable_id: ' + str(entry.get('id')))
        if not entry.get('id') or entry['id'] in manifest_ids or url in manifest_urls:
            raise ValueError('Duplicate or missing baseline identity: ' + url)
        manifest_urls.add(url)
        manifest_ids.add(entry['id'])
        if url not in source_index.get(entry.get('source_file'), {}):
            raise ValueError('Missing baseline source: ' + url)
    for url in by_url.keys() - manifest_urls:
        raise ValueError('Unknown baseline audit URL: ' + url)
    items = []
    grouped = {name: [] for name in sources}
    report = dict(release_ready=True, excluded=[], errors=[])

    def admissible(entry, review, origin, date, required=False):
        reason, error = None, None
        if not review:
            reason = 'missing_audit'
            if required:
                error = 'Baseline record has no matching audit'
        elif required and review.get('result') == 'pending':
            reason, error = 'audit_pending', 'Baseline audit is still pending; every original record must be attempted'
        elif review.get('quality_recommendation') == 'remove':
            reason = 'quality_remove'
        elif review.get('result') in ('fail', 'blocked', 'pending'):
            reason = 'audit_' + review['result']
        elif review.get('result') != 'pass':
            reason, error = 'invalid_result', 'Unknown or missing audit result'
        else:
            missing = [key for key in ('action', 'observed') if not isinstance(review.get(key), str) or not review[key].strip()]
            if not (review.get('checked_at') or date):
                missing.append('checked_at (or batch date / --audit-date)')
            if missing:
                reason, error = 'incomplete_pass', 'Missing pass fields: ' + ', '.join(missing)
            elif (review.get('checked_at') or date) != AUDIT_DATE:
                reason, error = 'audit_date_mismatch', 'This release requires audit date ' + AUDIT_DATE
        if reason:
            record = dict(name=entry.get('name'), url=entry['url'], origin=origin, reason=reason, result=review.get('result') if review else None)
            if review:
                record['audit'] = deepcopy(review)
            report['excluded'].append(record)
            if error:
                report['errors'].append(dict(url=entry['url'], message=error))
            return False
        return True

    for entry in manifest:
        original_url = canonical_url(entry['url'])
        review, date = by_url.get(original_url, (None, audit_date))
        if review and review.get('id') and review['id'] != entry['id']:
            raise ValueError('Audit ID differs from baseline: ' + original_url)
        if not admissible(entry, review, 'baseline', date, required=True):
            continue
        source = source_index[entry['source_file']][original_url]
        item = promote(source, review, entry['id'], date)
        if any(prior['url'] == item['url'] for prior in items):
            raise ValueError('Baseline final URL collision: ' + item['url'])
        items.append(item)
        grouped[entry['source_file']].append(item)
    candidate_reviews = index_audits(candidate_audits or [], audit_date)
    known_candidates = {canonical_url(source['url']) for source in candidates or []}
    for url in candidate_reviews.keys() - known_candidates:
        raise ValueError('Unknown candidate audit URL: ' + url)
    grouped['candidate_verified_items.json'] = []
    final_urls = {item['url']: item for item in items}
    for source in candidates or []:
        original_url = canonical_url(source['url'])
        review, date = candidate_reviews.get(original_url, (None, audit_date))
        if not admissible(source, review, 'candidate', date):
            continue
        identity = 'ui-' + hashlib.sha256(original_url.encode()).hexdigest()[:12]
        item = promote(source, review, identity, date)
        if item['url'] in final_urls:
            report['excluded'].append(dict(name=source.get('name'), url=source['url'], origin='candidate', reason='duplicate_final_url', retained_id=final_urls[item['url']]['stable_id']))
            continue
        if identity in {prior['stable_id'] for prior in items}:
            raise ValueError('Duplicate final identity: ' + identity)
        final_urls[item['url']] = item
        items.append(item)
        grouped['candidate_verified_items.json'].append(item)
    report['release_ready'] = not report['errors']
    report['counts'] = dict(baseline=len(manifest), candidates=len(candidates or []), admitted=len(items), excluded=len(report['excluded']), errors=len(report['errors']))
    report['exclusion_reasons'] = dict(Counter(row['reason'] for row in report['excluded']))
    return dict(items=items, sources=grouped, report=report)


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main(argv=None):
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, default=root)
    parser.add_argument('--manifest', type=Path, default=root / 'docs/full-audit-manifest.json')
    parser.add_argument('--baseline-audit', type=Path, default=root / 'docs/full-audit.json')
    parser.add_argument('--candidate', type=Path, action='append', default=[], help='Candidate JSON array; repeat for each batch')
    parser.add_argument('--candidate-audit', type=Path, action='append', default=[], help='Final candidate audit array or items object; repeat for each batch')
    parser.add_argument('--audit-date', help='Explicit fallback date for audit arrays missing per-record dates')
    parser.add_argument('--out-dir', type=Path, default=root / 'staging/verified-release')
    args = parser.parse_args(argv)
    safe_output = False
    snapshots = {}

    def load_snapshot(path):
        path = Path(path).resolve()
        if path not in snapshots:
            snapshots[path] = path.read_bytes()
        return json.loads(snapshots[path].decode('utf-8-sig'))

    try:
        source_root, output = args.source_root.resolve(), args.out_dir.resolve()
        if output == source_root:
            raise ValueError('Output directory must differ from source root')
        manifest = load_snapshot(args.manifest)
        if not isinstance(manifest, list):
            raise ValueError('Manifest must be a JSON array')
        source_names = list(dict.fromkeys(entry['source_file'] for entry in manifest))
        for name in source_names:
            if not isinstance(name, str) or Path(name).name != name or '/' in name or '\\' in name:
                raise ValueError('Manifest source_file must be a file name: ' + str(name))
        input_paths = [args.manifest, args.baseline_audit, *args.candidate, *args.candidate_audit, *(source_root / name for name in source_names)]
        output_names = [*source_names, 'candidate_verified_items.json', 'assembled_items.json', 'assembly-report.json', 'assembly-report.md']
        if any((output / name).resolve() == path.resolve() for name in output_names for path in input_paths):
            raise ValueError('Output would overwrite an input file')
        safe_output = True
        sources = {name: load_snapshot(source_root / name) for name in source_names}
        candidates = []
        for path in args.candidate:
            records = load_snapshot(path)
            if not isinstance(records, list):
                raise ValueError('Candidate file must contain an array: ' + str(path))
            candidates.extend(records)
        result = assemble(manifest, sources, load_snapshot(args.baseline_audit), candidates,
                          [load_snapshot(path) for path in args.candidate_audit], args.audit_date)
        result['report']['inputs'] = [dict(path=str(path.resolve()), sha256=hashlib.sha256(snapshots[path.resolve()]).hexdigest()) for path in input_paths]
        result['report']['audit_date_fallback'] = args.audit_date
        output.mkdir(parents=True, exist_ok=True)
        for name, records in result['sources'].items():
            write_json(output / name, records)
        write_json(output / 'assembled_items.json', result['items'])
        write_json(output / 'assembly-report.json', result['report'])
        lines = ['# 核验入库暂存报告', '', '仅为审阅产物，未覆盖原始来源。', '',
                 '准入检查：' + ('通过' if result['report']['release_ready'] else '未通过；请修复 errors 后重跑'),
                 '', '## 数量', '', json.dumps(result['report']['counts'], ensure_ascii=False), '', '## 未纳入条目', '']
        for row in result['report']['excluded']:
            lines.append('- ' + str(row.get('name') or row['url']).replace('\n', ' ') + ' — ' + row['reason'] + ' — ' + row['url'])
        lines += ['', '## 错误', ''] + [json.dumps(error, ensure_ascii=False) for error in result['report']['errors']]
        (output / 'assembly-report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
        print(json.dumps(dict(output=str(output), **result['report']['counts'], release_ready=result['report']['release_ready']), ensure_ascii=False))
        return 0 if result['report']['release_ready'] else 2
    except (ValueError, KeyError, TypeError, OSError) as error:
        if safe_output:
            output.mkdir(parents=True, exist_ok=True)
            write_json(output / 'assembly-report.json', dict(release_ready=False, errors=[dict(message=str(error))], note='Assembly aborted. Other staged files, if present, are from an earlier run and must not be published.'))
        print('Assembly error: ' + str(error), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
