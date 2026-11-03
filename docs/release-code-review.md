# 本轮发布代码审查

审查日期：2026-11-03。范围：`scripts/build.py`、`web/*`、`tests/*`，辅以本轮 audit 的实际结构。仅审查并新增本文，未修改构建代码、主数据或生成页面。审查期间其他核验仍在进行，本文不把中途数量视作最终发布数量。

结论：现有静态浏览器可以继续使用，不需要重写。发布前必须处理稳定 ID、核验结果准入和核验证据显示；候选另设文档入口即可。当前测试通过，但尚不能发现这些发布风险。

## 必修问题

### P1：修复 URL 会丢失原收藏

- 位置：`scripts/build.py:53`；`web/app.js:7`。
- 构建无条件用当前 URL 的 SHA-256 覆盖 `id`，即使输入明确提供旧 ID。前端再把不在当前 ID 集合中的收藏删掉并写回 localStorage。
- 已做纯内存复现：同一条记录显式给出 `id=ui-keep12345678`，URL 从 `/old` 换为 `/new`，输出分别成为 `ui-815d893c7089` 和 `ui-f8c0bb50121f`。因此修复到独立预览、官方 MP4 或 B 站第二分集会使已有收藏失效。
- 最小修正：从当前 `library.json` 或冻结的 `docs/full-audit-manifest.json` 保留旧条目的 ID；入库装配时先按原 URL/ID 匹配 audit，再换主 URL。构建尊重有效的显式 ID，只给真正新作品生成 ID，并校验最终 ID 唯一。不要顺便全面重做 URL 规范化。
- 如果已经发布过重算 ID 的版本，需提供旧 ID→保留 ID 的别名，在前端过滤失效收藏之前迁移。若尚未发布，保留原 ID 即可，无须额外迁移框架。真正删除的作品仍可按现有规则清理收藏。

### P1：旧布尔标记能覆盖本轮核验结论，audit 本身不会影响发布

- 位置：`scripts/build.py:59`、`:79`、`:89`；`web/app.js:30`。
- 构建只读取 5 个来源 JSON，不读取 `docs/full-audit.json` 或新增候选 audit；记录一条 fail/blocked 不会自动删除原库内容。
- `browser_verified = bool(browser_verified or visual_verified)` 会将本轮明确的 false 和历史 true 合并为 true。纯内存复现已确认：`browser_verified=false, visual_verified=true, verification='candidate'` 仍输出 `browser_verified=true`，页面会显示“画面已确认”。
- 最小修正：统一的发布装配步骤以本轮 audit 为权威，主库只接纳 `result=pass` 且含 `action`、`observed` 的条目。旧库未完成、fail、blocked 与新增未核验候选均不进入本轮正式集合；blocked 只表示当前未能核验，不能描述为作品本身失效。
- 从最终 audit 显式派生布尔值，移除旧 `visual_verified` 对本轮结论的兜底。对有冲突的重复记录直接报错或明确择取本轮结果，不能依赖当前“先遇到的非空字段胜出”的合并规则（`:46–50`）。
- 这可以在一次性发布装配脚本完成，再由 `build.py` 加发布不变量校验；不必强行让通用构建器读取所有研究文件。

### P1：替代链接需要保留验证对象与范围

- 本轮实际存在：React Bits 文档→官方 MP4、Magic UI Animated Beam→官方 MP4、Aceternity 文档→独立预览、B 站主分集→`?p=2`。
- 不可只换 `url` 后继续沿用旧描述及“交互已通过”。MP4 验证的是录像播放；减少动画偏好下的文档预览仍可能未完整复现。卡片类型和动作应随验证对象更新为“视频”和“观看原视频”。
- 最小记录：保留 `original_url`，明确 `verified_url` 或把审查记录中的 `replacement_url` 作为最终 URL；保留本轮 `action`、`observed`、`notes`。只有实际核验过替代地址才换主入口。ID 沿用原作品，不沿用旧链接哈希重新生成。
- `docs/full-audit-manifest.json` 是原 173 条的冻结基线，应保留；它不应被新库条目数量覆盖。

## 证据如何呈现

推荐把最终记录统一为一个 `audit` 对象，字段至少为：

```json
{
  "result": "pass",
  "action": "实际执行的操作",
  "observed": "实际看到的主体与变化",
  "notes": "只核验录像、减少动画偏好等范围限制",
  "checked_at": "2026-11-03",
  "browser": "IAB",
  "original_url": "原条目地址",
  "verified_url": "本次实际核验的最终入口"
}
```

- 现有 audit 并不完全同构：旧库文件是 `{date, method, items}`，新增 audit 多为数组；部分逐条记录缺日期和 browser。日期可从其所属批次的明确日期补入，浏览器信息只在已有证据支持时补入；不要凭空补“已完整观看”。
- `web/app.js:40` 目前只显示 `verification`、`checked_at` 等旧字段。详情增加“核验操作”“看到的效果”“核验限制”；继续使用已有 `textContent` 创建元素，避免把研究内容拼为 HTML。
- 卡片最小可用标记是“已核验”，具体范围放详情。若希望分成“播放已核验/交互已核验/画面已核验”，应加显式核验方式字段，不能仅按 `kind` 推导已经播放。
- `evidence_url` 多数是官方出处，不是本次实际操作证明。将 `app.js:43` 的“打开核验来源”改为“打开资料来源”，实际操作证据由上面的 audit 文本承担。需要审查报告入口时可用页面固定链接；现有 `Catalog.safeUrl` 不接受相对路径，不要把 `docs/xxx.md` 当外部作品 URL 传进去。
- `library.json` 会保留新增字段；CSV 在 `build.py:98` 使用固定列，目前丢失 ID 和全部结构化 audit 信息。至少新增 `id`、`audit_result`、`audit_action`、`audit_observed`、`audit_checked_at`，显式展平对象。JSON 仍可作为完整备份。

## 统计与旧文案的来源

| 内容 | 实际生成位置 | 本轮处理 |
|---|---|---|
| 首页总数、分类数、视频数、源码数 | `web/app.js:57–59`，来自正式 `data.items` | 保持自动计算；候选不得混入正式 items |
| 导航总数与分类计数 | `web/app.js:52`、`:58` | 与最终正式集合一致 |
| README 总条数与分类目录 | `scripts/build.py:112`、`:120–127` | 改构建器后重新生成，不手改输出 |
| 整理日期 | `scripts/build.py:11`，前端 `app.js:60` | 用实际发布日期/审核批次，不误写未来日期 |
| JSON limitations | `scripts/build.py:93–95` | 更新为实际验证范围；“未完整观看全部视频”仍可保留，不等同未逐条抽查 |
| README “并非每条都已逐一交互测试” | `scripts/build.py:116` | 按最终准入标准改为每条核验主体及关键操作，具体范围看详情；不承诺遍历全部功能 |
| 页脚“视频未逐一完整播放” | `web/template.html:44` | 与实际范围一致，避免和卡片“已核验”形成歧义 |
| 来源 Markdown | `scripts/build.py:82–87` 只重建 code/video/site 三份 | 扩展到全部正式来源，或把另外两份显式标为历史材料 |
| 旧研究说明 | `docs/research-notes.md` | 当前仍是部分抽查口径，更新到本轮规则 |
| 独立演示与新增界面说明 | `direct_demo_sources.md`、`ui_example_sources.md` | 仍有“13 条画面确认”“50 条均未浏览核验”等历史说明，不应作为当前状态展示 |

所有最终数量应从装配后的集合计算；原 173 条 audit 基线、研究批次 79/41/17 等历史数量可以保留，但必须有批次语义。

## 候选入口的最小方案

推荐在 README 和页面页脚新增“研究候选（尚未入库）”固定入口，指向一份汇总说明，再链接三批候选 JSON、选品审查和视频研究记录。候选入口应明确“仅确认来源/元数据，未必已浏览器通过”。

不要为此把候选塞入正式 `data.items`：现有筛选器不认识准入状态，新增一个 `data-view=candidates` 按钮也不会自动隔离候选。这样会污染总数、随机发现、收藏和导出。独立候选浏览页可以后续做，本次不是必要条件。

若展示“待核验候选数量”，应从候选集合减去已入库/已明确拒绝的唯一记录，不能直接把三批总数相加当作剩余量。同一品牌的网站与官方宣传片 URL 不同，仍需内容层面的去重，不能只按 URL 去重。

## 平台与分类

- `web/template.html:36` 的平台选项写死为 GitHub、B站、独立站、灵感平台，没有 YouTube。新增已核验 YouTube 作品时至少加入该选项；更稳妥的是从正式数据生成平台选项，保留 GitHub 为“含源码入口”的特殊筛选。
- `scripts/build.py:12–20` 的映射未覆盖新增候选中的“导航与微交互”“应用与数据界面”“滚动与版式”“应用界面展示”“界面动效短片”“作品集短片”“游戏UI与HUD”。入库时映射到有限的现有分类，或明确决定新增分类；不要让近义分类意外拆散目录。
- `canonical_url` 保留 B 站 `p` 参数，适合第二分集入口；不要删除它。其当前规范化不统一 www、youtu.be 等视频别名，本轮新增视频需用一致的 watch URL，并按视频 ID 复核内容去重。

## 测试结果与最小补充

本次只运行不会构建页面的已有测试：

- `python -m unittest discover -s tests`：6/6 通过。
- `node --test tests/catalog.test.cjs`：5/5 通过。
- 未运行 `tests/browser.cjs`；该脚本会写 `preview-desktop.png`、`preview-mobile.png`，且当前子代理没有可用浏览器。以上结果不能代替发布后的页面核验。

建议本轮补充能直接防回归的测试：

1. 原作品 URL 修复后，构建仍保留原 ID；浏览器预置原 ID 收藏后加载新版本仍保留收藏。真正移除的 ID 仍被清理。
2. pass/fail/blocked/pending、缺 action/observed、旧 visual=true 与新 false 冲突：仅满足本轮准入规则者进入正式集合。
3. 替代 MP4 的最终 URL、kind、原 ID、original_url 和 audit 观察内容一致；B 站 `p=2` 参数保留。
4. 最终 URL 与 ID 唯一；重复记录的矛盾 audit 不能静默合并。类别计数和总数仅覆盖正式集合。
5. 详情显示审查动作、观察与限制，并能安全显示 `<script>` 等文本；CSV 和 JSON 导出包含可追溯 ID/状态。
6. 新平台（尤其 YouTube）筛选可达；候选入口可打开且不影响正式搜索、随机和收藏。

现有浏览器测试还需小幅去除与旧选品绑定的假设：`tests/browser.cjs:17` 写死搜索“React 背景”，`:34` 固定加载更多后为 60 条。可以从当前数据选择能匹配的非空搜索词，并用 `min(60, items.length)` 等当前分页规则验证，避免正常删减后误报。保留 390/320 像素无横向溢出、详情关闭、收藏持久化、下载和无脚本报错的现有检查。

## 建议实施顺序

1. 冻结原 ID 并生成按 audit 准入的最终来源集合，保留替代入口的原始对应关系。
2. 构建器尊重 ID、校验准入与唯一性，规范分类，展平 CSV 证据列。
3. 页面详情展示 audit；补平台选项、固定候选入口和当前范围文案。
4. 重建全部生成物与当前来源清单；执行上述针对性测试，再检查实际浏览页。

已读取 `code-review` 技能：其正式流程要求指定 Git diff 基点并做双代理审查。本任务是父代理明确安排的全量只读发布审查，没有指定 diff，故没有套用该技能的差异审查流程，也没有另开代理或要求用户确认。
