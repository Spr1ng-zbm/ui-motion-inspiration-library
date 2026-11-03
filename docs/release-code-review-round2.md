# 发布代码复审 · 第二轮

2026-11-03，基于本次读取时的工作区代码。审查覆盖 `scripts/build.py`、`scripts/assemble_verified.py`、`web/app.js`、筛选模块与相关测试。以下行号对应修复前快照；主代理已授权随后用 TDD 修复第一项，本文保留发现时的触发条件。

## 发现

### P1：正式构建入口可以绕过核验准入

位置：`scripts/build.py:85–100`，首个生成文件写入在 `:98`；全数实测文案在 `:105`。

`build()` 直接读取来源 JSON，再调用通用 `merge_items()`，没有验证 `audit.result`、action/observed、日期、browser_verified 或 quality_remove。独立装配脚本中的门槛并不约束直接构建。

触发条件：有人把候选/blocked 记录误拷到正式来源文件、漏跑装配，或装配失败后继续运行构建。该记录仍进入 `library.json` 和页面，生成的 README/limitations 却称正式库全部实测。

纯内存复现已确认：`review_status=candidate, browser_verified=false, audit.result=blocked` 的记录经过 `merge_items()` 后正常保留。通用合并器本身可以保持宽松，但正式构建必须在写任何生成物之前验证所有原始输入，不能等去重后再验证，否则被合并的无效记录可能被掩盖。

建议：在正式入口要求当前 audit 为 pass、操作与观察非空、当轮日期一致、browser_verified 严格为 true、无 remove 建议；随后完成 URL/ID 合并校验，再写来源说明与生成物。以临时目录调用公开 `build()` 接口测试“无效输入不会改写任何产物”。

### P2：同 URL 的冲突身份在构建器内会静默丢弃

位置：`scripts/build.py:51–56`，先命中 URL 合并后就 continue，绕过 `:58–60` 的身份处理。

触发条件：两个正式来源记录拥有相同规范化 URL，但不同 `stable_id`。目前合并器保留第一条，既不报错，也不说明另一收藏身份被丢弃。例如同一 `https://same.example` 分别携带 `ui-111111111111` 与 `ui-222222222222`，输出只有前一个 ID。另一个 ID 的收藏随后会被 `web/app.js:7` 当失效记录移除。

本轮正常经过 `assemble_verified.py` 的暂存集合不会出现这个问题：原库最终 URL 合流会报错，候选最终 URL 重复会记录去重并保留原库。风险在于正式来源被额外手工合并或重跑路径未经过装配。建议在正式构建入口拒绝同 URL 的冲突稳定 ID；无需破坏通用 merge_items 对普通重复来源的合并行为。

## 已确认有效的修复

- `build.py:58` 尊重 `stable_id`；装配在 `assemble_verified.py:43–45` 先保留原身份、再应用最终 URL。现有换 MP4 / 独立预览的路径不会单纯因换 URL 重算收藏 ID。
- 显式 `browser_verified=false` 不再被旧 `visual_verified=true` 覆盖。
- 装配拒绝原库 pending；日期限定本轮，缺 action/observed 的 pass 不准入。候选 pending 可以正常排除，原库与候选按最终规范化 URL 去重，并留下排除原因。
- `web/app.js:40` 已显示核验操作、观察及补充说明，使用 textContent，未引入 HTML 拼接。装配 `:59–61` 正确生成对应扁平字段与完整 audit。
- `web/app.js:58–62` 会从实际平台集合补充选项，YouTube 等新平台不再需要逐个写入模板；GitHub 保留为源码筛选。当前筛选实现仍与此约定一致，没有发现功能冲突。
- CSV 已包含 ID、操作、观察、补充和访问说明；来源 Markdown 重建范围已扩大到六个正式来源组。

## 小项与测试边界

- `web/app.js:43` 链接所在栏已叫“资料来源”，按钮仍叫“打开核验来源”。若 evidence_url 指向官方首页或源码，它提供的是出处而非本轮实际观察；改成“打开资料来源”更准确。这是文案小项，详情中的实际证据字段已可独立表达范围。
- 现有浏览器测试尚未覆盖“旧版本收藏 ID → 修复 URL 后新版本”的装载过程，也没有断言新证据字段及动态平台选项。Python 已验证保留身份与显式 false，仍建议页面最终检查至少抽查一条修复入口、一条视频和一个新平台筛选。
- `tests/browser.cjs:17` 固定搜索“React 背景”，`:34` 固定要求加载后 60 条，属于旧选品假设。当前大库未必触发，但后续精简集合或改名会使测试错误失败。
- 本次没有发现现有暂存集合本身包含冲突稳定 ID；上面的第二项是可复现的构建边界缺口，不是宣称已经发生收藏丢失。

## 验证

- `python -m unittest discover -s tests`：19 项通过。
- `node --test tests/catalog.test.cjs`：5 项通过。
- 额外只读、纯内存复现了无准入记录仍保留和同 URL 不同稳定 ID 被静默合并。
- 未运行会改写预览图的浏览器脚本，未构建或改写正式库。随后获授权修复第一项时，仅修改 `build.py` 和 `tests/test_build.py`，另行报告新增测试结果。
