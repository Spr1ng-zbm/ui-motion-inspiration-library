"""Record human-observed browser checks against a fixed catalog snapshot."""
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
sys.stdin.reconfigure(encoding='utf-8', errors='strict')
DEST = ROOT / 'docs/full-audit.json'

def key(url):
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, p.path.rstrip('/'), p.query, p.fragment))

if DEST.exists():
    data = json.loads(DEST.read_text(encoding='utf-8'))
else:
    items = json.loads((ROOT/'library.json').read_text(encoding='utf-8'))['items']
    data = {'date':'2026-11-03','method':'逐条浏览器画面与关键操作核验；HTTP 状态不作为通过依据',
            'items':[dict(number=n,id=i['id'],name=i['name'],url=i['url'],result='pending') for n,i in enumerate(items,1)]}
updates = json.load(sys.stdin)
by_url = {key(i['url']):i for i in data['items']}
for update in updates:
    if update['result'] not in ('pass','fail','blocked'):
        raise ValueError('Invalid audit result')
    if not update.get('observed') or not update.get('action'):
        raise ValueError('Observation and action are required')
    by_url[key(update['url'])].update(update)
encoded = (json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
temporary = DEST.with_suffix('.json.tmp')
temporary.write_bytes(encoded)
temporary.replace(DEST)
from collections import Counter
print(dict(Counter(i['result'] for i in data['items'])))
