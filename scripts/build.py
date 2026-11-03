"""Build the portable catalog from curated, cited source records (stdlib only)."""
import csv
import hashlib
import json
import re
from collections import Counter
from itertools import zip_longest
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-11-03'
SOURCE_GROUPS = ('code', 'video', 'site', 'direct_demo', 'ui_example', 'candidate_verified')
CATEGORIES = {
    '完整 UI':'完整界面', '界面区块':'完整界面', '完整网站':'完整界面', 'UI展示':'完整界面',
    'App微交互':'微交互', '加载与反馈':'微交互', '光标与 Hover':'微交互', '鼠标交互':'微交互',
    '滚动叙事':'滚动与叙事', '滚动动画':'滚动与叙事', '页面转场':'滚动与叙事',
    '3D 与 Shader':'3D与沉浸', '3D与WebGL':'3D与沉浸', '文字动效':'文字与排版', '文字动画':'文字与排版',
    '粒子与流体':'粒子与背景', '图标与矢量':'图形与图标', '图标动效':'图形与图标',
    '画廊与轮播':'画廊与导航', '图片与画廊':'画廊与导航', '游戏UI':'游戏与趣味', '物理交互':'游戏与趣味',
    '动画组件':'组件与合集', '动效合集':'组件与合集', 'CSS 动画':'组件与合集',
    '交互动画':'微交互',
    '导航与微交互':'微交互', '应用与数据界面':'完整界面', '滚动与版式':'滚动与叙事',
    'App 微交互':'微交互', '界面动效短片':'微交互',
    '应用界面展示':'完整界面', '品牌与产品界面':'完整界面', 'App 与硬件展示':'完整界面',
    '图像与转场':'画廊与导航',
    '作品集与展示':'画廊与导航', '作品集短片':'画廊与导航',
    '游戏与交互体验':'游戏与趣味', '游戏UI与HUD':'游戏与趣味',
    '音频可视化':'声音与可视化',
}
FEATURED = {'WebGL Fluid Simulation', 'Motion：App Store 卡片展开',
    'Igloo Inc.：品牌官网', 'monopo London：创意机构界面', 'Clay：数字产品与品牌案例',
    'Rive：3D 车辆与座舱控制面板概念录像', 'Rauno · Vanish Input',
    'House of Corto — 可拖动家具画廊', 'Lando Norris 官方网站',
    'Three.js：周期表空间排列', 'Blobmixer：虹彩雕塑轮播',
    '拿了个国际小奖，我的个人网站演示', '神兽管理局：中国神话交互网页',
    'UI 动效作品集：消消美食街',
    'Thomas Gertenbach：照片桌面作品集', 'FunTech Creativity：渲染模式切换实验',
    'A24：三维唱片式电影目录概念', 'Squarespace Foundations：动态品牌系统',
    'Overworld Audio：声音项目地图', 'Ceramic Beats：陶瓷音色序列器'}


def canonical_url(value):
    parts = urlsplit(value.strip())
    if parts.scheme not in ('https','http') or not parts.hostname or parts.username or parts.password:
        raise ValueError('Unsafe URL: ' + value)
    query = [(k,v) for k,v in parse_qsl(parts.query, keep_blank_values=True)
             if not k.startswith('utm_') and k not in ('spm_id_from','vd_source','si','trk','fbclid','t')]
    if parts.hostname in ('www.youtube.com','youtube.com'):
        query = [(k,v) for k,v in query if k in ('v','list')]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip('/'), urlencode(query), parts.fragment))


def merge_items(raw):
    merged = {}
    identities = set()
    for original in raw:
        item = dict(original)
        if 'stable_id' in item and (not isinstance(item['stable_id'], str) or not re.fullmatch(r'ui-[0-9a-f]{12}', item['stable_id'])):
            raise ValueError('Invalid preserved catalog identity')
        url = canonical_url(item['url'])
        for key in ('repo_url','evidence_url','thumbnail_url'):
            if item.get(key): canonical_url(item[key])
        if url in merged:
            prior = merged[url]
            prior['tags'] = list(dict.fromkeys(prior.get('tags',[]) + item.get('tags',[])))
            for k,v in item.items():
                if v and not prior.get(k): prior[k] = v
            continue
        item['url'] = url
        item['id'] = item.get('stable_id') or 'ui-' + hashlib.sha256(url.encode()).hexdigest()[:12]
        if item['id'] in identities:
            raise ValueError('Duplicate catalog identity: ' + item['id'])
        identities.add(item['id'])
        item['category'] = CATEGORIES.get(item.get('category'), item.get('category','灵感索引'))
        item['tags'] = list(dict.fromkeys(item.get('tags', [])))
        item['platform'] = item.get('platform','独立站')
        if item['platform'] == '官方站点': item['platform'] = '独立站'
        item['kind'] = item.get('kind','作品')
        item['browser_verified'] = bool(item.get('browser_verified', item.get('visual_verified', False)))
        item['featured'] = bool(item.get('featured') or item.get('name') in FEATURED)
        item['checked_at'] = item.get('checked_at','2026-11-02')
        item['verification'] = item.get('verification','待核验')
        if item.get('thumbnail_url','').startswith('http://i') and 'hdslb.com/' in item['thumbnail_url']:
            item['thumbnail_url'] = item['thumbnail_url'].replace('http://','https://',1)
        merged[url] = item
    return list(merged.values())


def safe_json(value):
    return json.dumps(value, ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')


def markdown_text(value):
    return str(value).replace('|','\\|').replace('\n',' ').replace('[','\\[').replace(']','\\]')


def validate_release_input(item):
    """Only the official build requires a current, complete browser audit."""
    if not isinstance(item, dict):
        raise ValueError('Unverified catalog input: expected an item object')
    audit = item.get('audit')
    problems = []
    if not isinstance(audit, dict):
        problems.append('audit object is required')
    else:
        if audit.get('result') != 'pass':
            problems.append('audit.result must be pass')
        for key in ('action', 'observed'):
            if not isinstance(audit.get(key), str) or not audit[key].strip():
                problems.append('audit.' + key + ' must be non-empty text')
        if audit.get('checked_at') != DATE:
            problems.append('audit.checked_at must be ' + DATE)
        if audit.get('quality_recommendation') == 'remove':
            problems.append('audit recommends removal')
    if item.get('browser_verified') is not True:
        problems.append('browser_verified must be true')
    if item.get('checked_at') != DATE:
        problems.append('checked_at must be ' + DATE)
    if item.get('quality_recommendation') == 'remove':
        problems.append('item recommends removal')
    if problems:
        raise ValueError('Unverified catalog input ' + str(item.get('url', item.get('name', ''))) + ': ' + '; '.join(problems))


def build():
    groups = {}
    for source_name in SOURCE_GROUPS:
        path = ROOT / f'{source_name}_items.json'
        if path.exists():
            records = json.loads(path.read_text(encoding='utf-8-sig'))
            if not isinstance(records, list):
                raise ValueError('Unverified catalog input ' + path.name + ': expected an array')
            groups[source_name] = records
    identities_by_url = {}
    for records in groups.values():
        for item in records:
            validate_release_input(item)
            url = canonical_url(item['url'])
            identity = item.get('stable_id') or 'ui-' + hashlib.sha256(url.encode()).hexdigest()[:12]
            if url in identities_by_url and identities_by_url[url] != identity:
                raise ValueError('Conflicting catalog identities for URL ' + url + ': ' + str(identities_by_url[url]) + ' / ' + str(identity))
            identities_by_url[url] = identity
    raw = [item for row in zip_longest(*groups.values()) for item in row if item is not None]
    items = merge_items(raw)
    # All audit, URL and identity checks finish before any generated file is written.
    for source_name, source_items in groups.items():
        source_lines = [f'# 当前收录来源 · {source_name}', '', f'整理于 {DATE}。仅列出本版仍收录的 {len(source_items)} 条。', '']
        for item in source_items:
            source_lines += [f"## {item['name']}", '', f"- 作品：{item['url']}", f"- 依据：{item.get('evidence_url', item['url'])}", f"- 核验：{item.get('verification','页面内容核验')}", '']
        (ROOT/f'{source_name}_sources.md').write_text('\n'.join(source_lines),encoding='utf-8')
    items.sort(key=lambda item: (not item['browser_verified'], not item['featured']))
    counts = Counter(i['category'] for i in items)
    data = {'updated_at':DATE, 'items':items, 'counts':dict(counts),
            'limitations':['小红书：XHS Bridge 未连接，未取得可核验笔记，0 条收录。',
                '当前主库各条目均记录实际浏览器画面与操作；视频按关键片段核验，未遍历每一种交互状态。',
                '预览可能受地区网络、浏览器与 GPU 支持影响；WebGPU 案例已标注要求。']}
    (ROOT/'library.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (ROOT/'library.csv').open('w',encoding='utf-8-sig',newline='') as out:
        keys = ['id','name','url','platform','category','kind','description','tags','repo_url','verification','verification_action','verification_observed','verification_notes','evidence_url','checked_at','access_notes']
        writer = csv.DictWriter(out,fieldnames=keys); writer.writeheader()
        for item in items:
            row = {k:item.get(k,'') for k in keys};row['tags']=' / '.join(item['tags'])
            for key,value in row.items():
                if isinstance(value,str) and value.startswith(('=','+','-','@')): row[key]="'"+value
            writer.writerow(row)
    page = (ROOT/'web/template.html').read_text(encoding='utf-8')
    page = page.replace('/*__STYLE__*/',(ROOT/'web/style.css').read_text(encoding='utf-8'))
    page = page.replace('/*__CATALOG__*/',(ROOT/'web/catalog.js').read_text(encoding='utf-8'))
    page = page.replace('/*__APP__*/',(ROOT/'web/app.js').read_text(encoding='utf-8'))
    page = page.replace('__DATA__',safe_json(data))
    (ROOT/'index.html').write_text(page,encoding='utf-8')
    lines = ['# UI Motion Library · UI 界面与动效灵感库','',
        f'收录 **{len(items)} 条**具体 UI 界面、可体验动效与作品展示。最后整理：{DATE}。', '',
        '**[打开在线灵感库 →](https://spr1ng-zbm.github.io/ui-motion-inspiration-library/)**','',
        '也可以下载仓库后直接打开 [index.html](index.html)，支持搜索、分类、平台筛选、本地收藏、随机发现与导出。','',
        '[全部数据 JSON](library.json) · [CSV 索引](library.csv) · [本轮逐项核验](docs/current-audit.md)','',
        '> 主库仅保留已实际查看画面的具体作品、UI 和动效；教程、泛导航、占位页面与无法确认核心画面的条目不入库。详情记录做了什么、看到了什么；产品展示与实际可交互演示分别说明。视频按关键片段核验，不代表完整播放或遍历全部状态。', '',
        '## 从这里开始','']
    for item in [i for i in items if i['featured']][:24]:
        lines.append(f"- [{markdown_text(item['name'])}]({item['url']}) — {markdown_text(item['description'])}")
    lines += ['', '## 分类目录','']
    for category,n in sorted(counts.items()): lines.append(f'- {category}：{n} 条')
    for category in sorted(counts):
        lines += ['', '## '+category, '', '| 名称 | 平台 / 类型 | 值得参考 | 原链接 / 实现 |','|---|---|---|---|']
        for item in [x for x in items if x['category']==category]:
            source = f"[打开]({item['url']})"
            if item.get('repo_url'): source += f" · [源码]({item['repo_url']})"
            lines.append(f"| {markdown_text(item['name'])} | {markdown_text(item['platform'])} / {markdown_text(item['kind'])} | {markdown_text(item['description'])} | {source} |")
    lines += ['', '## 更新方式','', '修改来源 JSON 后运行：', '', '```sh','python scripts/build.py','python -m unittest discover -s tests','node --test tests/catalog.test.cjs','```','',
        '收藏保存在当前浏览器本地，不会上传 GitHub；可用浏览页的导出按钮备份。预览图片从原站载入，失效时保留文字卡片和原链接。','',
        '## 来源与使用','',
        '原创整理与浏览器代码见 [LICENSE](LICENSE)。第三方网站、图像、视频和代码各自保留原作者权利；本库的许可不覆盖第三方素材。各项目具体许可记录可在浏览页详情和 JSON 查看。','',
        '[动效来源](code_sources.md) · [视频来源](video_sources.md) · [网站与界面来源](site_sources.md) · [独立演示来源](direct_demo_sources.md) · [界面来源](ui_example_sources.md) · [本轮新增](candidate_verified_sources.md)','']
    (ROOT/'README.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'items':len(items),'categories':dict(counts),'featured':sum(i['featured'] for i in items)},ensure_ascii=True))


if __name__ == '__main__': build()
