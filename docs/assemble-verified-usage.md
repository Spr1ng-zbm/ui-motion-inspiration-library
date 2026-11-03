# 核验入库装配工具

`scripts/assemble_verified.py` 只产生暂存文件，不覆盖根目录来源 JSON、`library.json` 或页面。已采用 TDD 验证公开装配接口和 CLI，测试文件为 `tests/test_assemble_verified.py`。

## 运行

在仓库根目录执行（可以写成一行）：

```sh
python scripts/assemble_verified.py --candidate candidate_items_20261103.json --candidate candidate_items_round2.json --candidate candidate_video_round3.json --candidate-audit docs/audit-new-sites.json --candidate-audit docs/audit-new-videos.json --candidate-audit docs/audit-video-round3.json --audit-date 2026-11-03 --out-dir staging/verified-release
```

默认读取 `docs/full-audit-manifest.json` 和 `docs/full-audit.json`。可以用 `--manifest`、`--baseline-audit`、`--source-root` 改变输入位置。候选文件和候选最终核验文件均为显式、可重复参数，不会自动扫描或把旁证文件当成权威审查。

`--audit-date` 只是无逐条日期/批次日期时的明确日期后备值。优先级为逐条 `checked_at` > audit 对象的 `date` > CLI 日期。此脚本针对本轮发布，所有准入日期必须是 `2026-11-03`。不会从来源旧日期或候选 HTTP 元数据日期冒充浏览器核验日期。没有可用日期或日期不符的 pass 会被排除，并记录数据错误。浏览器名称缺失时保持缺失，不伪造。

## 输出与准入

- 原库按冻结 manifest 的 `source_file` 分组暂存，ID 保存为 `stable_id`。换主 URL 不改变收藏身份。
- `candidate_verified_items.json`：通过本轮核验的新候选。
- `assembled_items.json`：原库保留项与新增候选的完整集合。
- `assembly-report.json`：每条排除原因、数据错误、数量、实际读取的输入字节 SHA-256。
- `assembly-report.md`：便于阅读的移除/暂不收录清单。

只有 `result=pass` 且具有非空 `action`、`observed` 和核验日期的记录可进入暂存。`quality_recommendation=remove` 即使 pass 也排除；fail/blocked/pending 均排除。未核验候选是正常排除项，不是数据错误；冻结原库缺少对应 audit 记录或仍为 pending 则报告错误，仍生成暂存但退出码为 2。原库 173 条必须全部尝试后才能通过发布检查。

`release_ready=true` 只表示此次装配没有数据一致性错误，**不表示所有候选都已核验，也不表示已经发布**。最终是否发布由主流程审阅报告决定。

替代 URL、建议名称与建议描述来自实际 audit。媒体文件入口自动标为视频；替代视频入口的平台按地址明确为 B站、YouTube 或独立站。归一化沿用 `scripts/build.py` 的 `canonical_url`，保留 B 站 `p=2` 分集参数。

前端字段统一为 `verification_action`、`verification_observed`、`verification_notes`，同时保存完整 `audit`、`original_url` 和简洁的 `verification` 文案。`access_notes` 原样保留，避免自动改写研究者的访问限制；若其中存在过时的通用“待核验”提示，发布流程应明确处理，不能把它当成本次未通过。

## 重复与错误

- 同 URL 的矛盾 audit 直接报错，不能靠文件顺序选出一个 pass。
- 原库两条记录替换后落到同一 URL，直接报错，避免自动丢掉任一旧收藏身份。
- 新候选与已保留的最终 URL 重复时，保留原库/先出现候选，报告 `duplicate_final_url` 和保留 ID。这里只去重链接，不声称已完成跨平台同片/相似内容判断。
- 缺来源记录、孤立的 audit URL、冲突 ID、非法 URL 均明确报错。manifest 的保留 ID 必须符合构建器的 `ui-[0-9a-f]{12}` 格式。
- 命令行成功返回 0；数据错误返回 2。若装配中途报错，安全暂存目录中的 `assembly-report.json` 会标记失败，既有暂存文件可能属于上一次运行，不应继续发布。
- 输出目录不得是来源根目录，输出路径也不得覆盖任何输入文件。相同输入可重复运行，输出不加入随机时间戳。

## 本轮验证记录

2026-11-03，`python -m unittest discover -s tests -p test_assemble_verified.py`：9 项通过。按红→绿步骤覆盖：

1. 视频替代保留原 ID、应用建议字段并保留实际观察。
2. pass/action/observed/日期准入及 fail、blocked、pending、remove 排除。
3. 候选必须有自己的核验；与原库最终 URL 归一化去重。
4. 矛盾 audit、原库最终 URL 冲突报错。
5. 孤立 audit 与缺来源记录报错。
6. CLI 重跑结果一致、来源字节不变、拒绝输出覆盖来源。
7. 缺核验日期的 pass 报告具体缺失字段。
8. 原库 pending 阻止发布且 CLI 非零退出；候选 pending 正常排除。
9. 非法 stable_id 和旧 audit 日期无法进入暂存，不借用来源日期补通过。

首次以实际文件运行时，读取原库 173 条和三批候选 137 条，暂存通过 195 条、排除 115 条。随后根据发布审阅增加了“原库 pending 阻止发布”的条件。核验文件仍在更新，此数量只是一次输入快照，不是最终发布承诺；最终以重新运行的报告为准。
