"""Summarize the actual published collection against the frozen baseline."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    data = json.loads((ROOT/'library.json').read_text(encoding='utf-8'))
    items = data['items']
    baseline = json.loads((ROOT/'docs/full-audit-manifest.json').read_text(encoding='utf-8'))
    audits = json.loads((ROOT/'docs/full-audit.json').read_text(encoding='utf-8'))['items']
    by_id = {i['id']: i for i in items}
    old_ids = {i['id'] for i in baseline}
    kept = sum(i['id'] in by_id for i in baseline)
    def clean(value): return str(value).replace('|', '\\|').replace('\n', ' ')
    lines = ['# 当前版本逐项核验', '', f"更新：{data['updated_at']}。主库 **{len(items)} 条**；旧库 {len(baseline)} 条全部尝试核查，保留 **{kept} 条**，移出 **{len(baseline)-kept} 条**；新增 **{sum(i['id'] not in old_ids for i in items)} 条**。", '',
        '主库每条均有实际画面依据和具体操作记录。静态界面可以作为 UI 参考；只有看到变化才描述为已验证动效。视频核验关键片段，不代表完整播放。', '',
        '## 入库标准', '', '保留具体 UI、交互演示、创意网站或高完成度展示视频。排除教程、泛导航、主体占位过多、低完成度小样及本轮无法确认核心画面的条目。链接修复后保留原收藏 ID。', '',
        '“暂无法核验”仅描述本轮环境，不等于原站永久失效。候选文件与历史审计不属于推荐主库；当前推荐以 library.json / 在线浏览页为准。', '',
        '## 分类', '']
    lines += [f'- {name}：{count} 条' for name,count in data['counts'].items()]
    lines += ['', '## 原有 173 条的逐项结果', '', '| 条目 | 当前处理 | 本轮依据 / 移出原因 |', '|---|---|---|']
    review_by_id = {i['id']:i for i in audits}
    for row in baseline:
        a=review_by_id[row['id']]
        current=by_id.get(row['id'])
        status='保留' if current else '质量移除' if a.get('quality_recommendation')=='remove' or a['result']=='fail' else '暂无法核验，移出'
        reason=a.get('quality_reason') if not current else None
        reason=reason or a.get('observed','')
        lines.append(f"| [{clean((current or row)['name'])}]({(current or row)['url']}) | {status} | {clean(reason)} |")
    lines += ['', '## 新增条目逐项记录', '', '| 作品 | 实际操作 | 实际所见 |', '|---|---|---|']
    for i in items:
        if i['id'] not in old_ids:
            lines.append(f"| [{clean(i['name'])}]({i['url']}) | {clean(i['verification_action'])} | {clean(i['verification_observed'])} |")
    lines += ['', '## 数据依据', '', '[完整主库](../library.json) · [旧库原始清单](full-audit-manifest.json) · [旧库逐项审计](full-audit.json) · [新增网站审计](audit-new-sites.json) · [新增展示录像审计](audit-new-videos.json) · [第二轮审计](audit-round2-sites.json)', '',
        '小红书连接未就绪，未取得可核验笔记，因此没有以搜索摘要补数。第三方网站、图像、视频和代码的权利归原作者；本库只整理入口与参考点。', '']
    (ROOT/'docs/current-audit.md').write_text('\n'.join(lines),encoding='utf-8')
    print(f'Audit report: {len(items)} entries, {kept} retained baseline')

if __name__ == '__main__': main()
