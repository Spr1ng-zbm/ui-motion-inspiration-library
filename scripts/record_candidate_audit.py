"""Append observed candidate checks; does not promote them into the catalog."""
import json
import sys
import argparse
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
sys.stdin.reconfigure(encoding='utf-8', errors='strict')
parser = argparse.ArgumentParser()
parser.add_argument('--batch', choices=('sites', 'videos'), default='sites')
args = parser.parse_args()
DEST = ROOT / ('docs/audit-new-sites.json' if args.batch == 'sites' else 'docs/audit-video-round3.json')

def key(url):
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, p.path.rstrip('/'), p.query, p.fragment))

candidates = []
for name in ('candidate_items_20261103.json', 'candidate_items_round2.json', 'candidate_items_round4.json', 'candidate_video_round3.json', 'candidate_items_round5.json', 'candidate_items_round6.json', 'candidate_items_round7.json'):
    candidates.extend(json.loads((ROOT/name).read_text(encoding='utf-8')))
known = {key(i['url']): i for i in candidates}
data = json.loads(DEST.read_text(encoding='utf-8')) if DEST.exists() else []
by_url = {key(i['url']): i for i in data}
for update in json.load(sys.stdin):
    candidate = known[key(update['url'])]
    if update['result'] not in ('pass', 'fail', 'blocked') or not update.get('action') or not update.get('observed'):
        raise ValueError('A real action and observation are required')
    by_url[key(update['url'])] = dict(name=candidate['name'], checked_at='2026-11-03', **update)
encoded = (json.dumps(list(by_url.values()), ensure_ascii=False, indent=2)+'\n').encode('utf-8')
temporary = DEST.with_suffix('.json.tmp')
temporary.write_bytes(encoded)
temporary.replace(DEST)
from collections import Counter
print(dict(Counter(i['result'] for i in by_url.values())))
