import unittest
import sys
import json
import io
import tempfile
from contextlib import redirect_stdout
from copy import deepcopy
from unittest.mock import patch
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build


class BuildTests(unittest.TestCase):
    def test_canonical_url_keeps_identity_not_tracking(self):
        self.assertEqual(build.canonical_url('https://www.youtube.com/watch?v=ABC_12&utm_source=x&t=8'), 'https://www.youtube.com/watch?v=ABC_12')
        self.assertEqual(build.canonical_url('https://example.com/test/?utm_source=x'), 'https://example.com/test')

    def test_rejects_unsafe_or_missing_urls(self):
        for value in ['javascript:alert(1)', 'file:///c:/secret', '//example.com', 'https://u:p@example.com']:
            with self.assertRaises(ValueError):
                build.canonical_url(value)

    def test_duplicate_sources_merge_without_losing_evidence(self):
        base = dict(name='Example', url='https://example.com/', category='完整界面', platform='独立站', kind='作品', tags=['UI'], description='参考界面', evidence_url='https://example.com', verification='页面信息')
        duplicate = dict(base, url='https://example.com?utm_source=test', tags=['动效'], repo_url='https://github.com/a/b')
        items = build.merge_items([base, duplicate])
        self.assertEqual(len(items), 1)
        self.assertEqual(set(items[0]['tags']), {'UI', '动效'})
        self.assertEqual(items[0]['repo_url'], duplicate['repo_url'])

    def test_script_serialization_cannot_close_script(self):
        out = build.safe_json([{'name': '</script><script>alert(1)</script>'}])
        self.assertNotIn('</script>', out)
        self.assertIn('\\u003c', out)

    def test_duplicate_cannot_inject_unsafe_repository_url(self):
        a = dict(name='A',url='https://example.com',description='A')
        with self.assertRaises(ValueError):
            build.merge_items([a,dict(a,repo_url='javascript:alert(1)')])

    def test_ids_stay_stable_when_order_changes(self):
        a = dict(name='A', url='https://a.com', description='A')
        b = dict(name='B', url='https://b.com', description='B')
        first = {v['url']:v['id'] for v in build.merge_items([a,b])}
        second = {v['url']:v['id'] for v in build.merge_items([b,a])}
        self.assertEqual(first, second)

    def test_repaired_link_preserves_existing_favorite_identity(self):
        item = dict(name='Preview', url='https://example.com/live-preview',
                    stable_id='ui-123456abcdef')
        self.assertEqual(build.merge_items([item])[0]['id'], 'ui-123456abcdef')

    def test_favorite_identity_cannot_be_shared_by_distinct_items(self):
        a = dict(name='A', url='https://a.example', stable_id='ui-123456abcdef')
        b = dict(name='B', url='https://b.example', stable_id='ui-123456abcdef')
        with self.assertRaises(ValueError):
            build.merge_items([a, b])

    def test_latest_explicit_verification_overrides_legacy_flag(self):
        item = dict(name='Old preview', url='https://example.com',
                    browser_verified=False, visual_verified=True)
        self.assertFalse(build.merge_items([item])[0]['browser_verified'])

    def test_invalid_preserved_identity_is_rejected(self):
        for identity in ('old id', '<script>', 123):
            with self.assertRaises(ValueError):
                build.merge_items([dict(name='A', url='https://a.example', stable_id=identity)])

    def test_official_build_rejects_unverified_inputs_before_writing_any_artifact(self):
        valid = dict(name='Verified example', url='https://example.com', description='Observed UI',
                     stable_id='ui-123456abcdef', browser_verified=True, checked_at='2026-11-03',
                     audit=dict(result='pass', action='Click next', observed='Panel changed', checked_at='2026-11-03'))
        cases = [
            ('missing audit', {'audit': None}),
            ('blocked', {'audit': dict(valid['audit'], result='blocked')}),
            ('missing action', {'audit': dict(valid['audit'], action='  ')}),
            ('missing observation', {'audit': dict(valid['audit'], observed='')}),
            ('missing audit date', {'audit': dict(valid['audit'], checked_at=None)}),
            ('old audit date', {'audit': dict(valid['audit'], checked_at='2026-11-02')}),
            ('old item date', {'checked_at': '2026-11-02'}),
            ('false browser flag', {'browser_verified': False}),
            ('string browser flag', {'browser_verified': 'true'}),
            ('remove in audit', {'audit': dict(valid['audit'], quality_recommendation='remove')}),
            ('remove in item', {'quality_recommendation': 'remove'}),
        ]
        for label, changed in cases:
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root/'web').mkdir()
                for filename in ('template.html','style.css','catalog.js','app.js'):
                    (root/'web'/filename).write_text('__DATA__' if filename=='template.html' else '', encoding='utf-8')
                # A duplicate URL must not hide the invalid second source record.
                (root/'site_items.json').write_text(json.dumps([valid, dict(deepcopy(valid), **changed)]), encoding='utf-8')
                (root/'index.html').write_text('previous release', encoding='utf-8')
                before = {p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}
                with patch.object(build, 'ROOT', root), redirect_stdout(io.StringIO()):
                    with self.assertRaisesRegex(ValueError, 'Unverified catalog input'):
                        build.build()
                after = {p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}
                self.assertEqual(after, before, 'An invalid source must not create or overwrite generated files')

    def test_official_build_publishes_valid_audit_with_preserved_identity(self):
        item = dict(name='Verified example', url='https://example.com/repaired', description='Observed UI',
                    stable_id='ui-123456abcdef', browser_verified=True, checked_at='2026-11-03',
                    audit=dict(result='pass', action='Click next', observed='Panel changed', checked_at='2026-11-03'))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'web').mkdir()
            for filename in ('template.html','style.css','catalog.js','app.js'):
                (root/'web'/filename).write_text('__DATA__' if filename=='template.html' else '', encoding='utf-8')
            (root/'site_items.json').write_text(json.dumps([item]), encoding='utf-8')
            with patch.object(build, 'ROOT', root), redirect_stdout(io.StringIO()):
                build.build()
            published = json.loads((root/'library.json').read_text(encoding='utf-8'))['items'][0]
            self.assertEqual(published['id'], 'ui-123456abcdef')
            self.assertEqual(published['url'], 'https://example.com/repaired')
            self.assertEqual(published['audit']['observed'], 'Panel changed')

    def test_null_record_cannot_be_silently_dropped_as_pagination_padding(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'site_items.json').write_text('[null]', encoding='utf-8')
            with patch.object(build, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'Unverified catalog input'):
                    build.build()
            self.assertEqual({p.name for p in root.iterdir()}, {'site_items.json'})

    def test_official_build_rejects_conflicting_identities_for_one_canonical_url(self):
        first = dict(name='Original', url='https://example.com/demo/', description='Observed UI',
                     stable_id='ui-123456abcdef', browser_verified=True, checked_at='2026-11-03',
                     audit=dict(result='pass', action='Click next', observed='Panel changed', checked_at='2026-11-03'))
        second = dict(first, name='Duplicate', url='https://example.com/demo?utm_source=test', stable_id='ui-abcdef123456')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'web').mkdir()
            for filename in ('template.html','style.css','catalog.js','app.js'):
                (root/'web'/filename).write_text('__DATA__' if filename=='template.html' else '', encoding='utf-8')
            (root/'site_items.json').write_text(json.dumps([first, second]), encoding='utf-8')
            (root/'index.html').write_text('previous release', encoding='utf-8')
            before = {p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}
            with patch.object(build, 'ROOT', root), redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(ValueError, 'Conflicting catalog identities for URL'):
                    build.build()
            self.assertEqual({p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}, before)


if __name__ == '__main__':
    unittest.main()
