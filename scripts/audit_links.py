"""Check public catalog destinations. HTTP success alone is not visual verification."""
import concurrent.futures
import json
import re
import subprocess
import sys
from pathlib import Path
from html import unescape

ROOT=Path(__file__).resolve().parents[1]


def check(item):
    url=item['url']
    if 'bilibili.com/video/' in url:
        bv=re.search(r'BV[A-Za-z0-9]+',url).group()
        url='https://api.bilibili.com/x/web-interface/view?bvid='+bv
    command=['curl.exe','--http1.1','--location','--silent','--show-error','--max-time','18',
             '--user-agent','Mozilla/5.0','--write-out','\n__AUDIT__%{http_code}|%{url_effective}',url]
    r=subprocess.run(command,capture_output=True,timeout=23)
    text=r.stdout.decode('utf-8','replace');body,_,tail=text.rpartition('\n__AUDIT__')
    status,_,final=tail.partition('|')
    title=re.search(r'<title[^>]*>(.*?)</title>',body,re.S|re.I)
    result={'name':item['name'],'url':item['url'],'status':int(status or 0),'final_url':final,
        'title':unescape(re.sub(r'\s+',' ',title.group(1))).strip() if title else '',
        'bytes':len(body),'curl_error':r.returncode,'checked_at':'2026-11-03'}
    if 'api.bilibili.com' in url:
        try:
            j=json.loads(body);result['bili_code']=j.get('code');result['title']=j.get('data',{}).get('title','')
        except Exception:result['bili_code']='parse failure'
    # Page content gates, not a verdict on the effect itself.
    result['blocked_or_missing']=bool(re.search(r'404|not found|just a moment|access denied|captcha|verify you are human|security checkpoint',result['title'],re.I))
    result['content_hint']=' '.join(re.findall(r'<h[12][^>]*>(.*?)</h[12]>',body,re.S|re.I))[:500]
    if 'youtube.com/' in url:result['content_hint']='YouTube playback not independently verified'
    return result


if __name__=='__main__':
    data=json.loads((ROOT/'library.json').read_text(encoding='utf-8'))['items']
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        futures={pool.submit(check,i):i for i in data}
        for future in concurrent.futures.as_completed(futures):
            item=futures[future]
            try:result=future.result()
            except Exception as error:result={'name':item['name'],'url':item['url'],'status':0,'error':type(error).__name__}
            results.append(result)
            if len(results)%30==0:print('Checked',len(results),'/',len(data),flush=True)
    (ROOT/'link_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'total':len(results),'http200':sum(x['status']==200 for x in results),'flagged':sum(x['status']!=200 or x.get('blocked_or_missing') for x in results)}))
