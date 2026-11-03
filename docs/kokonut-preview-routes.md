# Kokonut UI 三个组件的独立预览路由调查

核查日期：2026-11-03。目标：Slide to Confirm、Detent Dial、Liquid Gauge。**结论：本轮未发现官方提供、可替换文档链接的独立纯演示页。** 没有试探 `/preview`、`/view` 或其他猜测地址，也没有自部署组件。保留原文档 URL 比编造替代地址可靠。

这是只读的页面和官方源码调查。主代理已完成原文档内交互实测；本报告不重复或覆盖那个结果，也不声称本子线程播放或操作过组件。

| 组件 | 已取得的官方页面 | 原页 GET | 独立纯演示链接 |
|---|---|---:|---|
| Slide to Confirm | [官方文档](https://kokonutui.com/docs/buttons/slide-to-confirm) | 200 | 未发现 |
| Detent Dial | [官方文档](https://kokonutui.com/docs/inputs/detent-dial) | 200 | 未发现 |
| Liquid Gauge | [官方文档](https://kokonutui.com/docs/cards/liquid-gauge) | 200 | 未发现 |

## 原作者源码证据

本次读取官方仓库树的完整结果 `truncated=false`，固定提交为 `4d497b7b03f02ffd07225e638c0b9ace3f892dbb`。[完整树 API](https://api.github.com/repos/kokonut-labs/kokonutui/git/trees/4d497b7b03f02ffd07225e638c0b9ace3f892dbb?recursive=1)。

1. 三个 MDX 都设置 `full: false`，并将组件直接放入 `<Preview>`；没有提供 `useIframe`、`previewLink` 或独立 URL：
   - [Slide to Confirm MDX，第6–13行](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/content/docs/buttons/slide-to-confirm.mdx#L6)
   - [Detent Dial MDX，第6–14行](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/content/docs/inputs/detent-dial.mdx#L6)
   - [Liquid Gauge MDX，第6–13行](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/content/docs/cards/liquid-gauge.mdx#L6)
2. 通用 Preview 默认 `useIframe=false`，在同一个 `figure` 中绘制安装栏，随后直接渲染 `children`。[Preview 默认参数](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/components/mdx/preview.tsx#L39)、[安装栏与演示主体](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/components/mdx/preview.tsx#L57)。这解释了为何主体周围仍有安装信息。
3. Preview 的确保留了一条 iframe 分支，但其路径表达式使用 `PRE_PATH="@kokonutui"` 拼出相对字符串，且本次三个 MDX 都未启用这条分支。不能从这段代码推断存在有效 `/preview/<name>` 路由，更不能把字符串当作已验证独立页。[常量](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/components/mdx/preview.tsx#L32)、[条件 iframe 分支](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/components/mdx/preview.tsx#L73)。
4. `PreviewTemplate` 有 Live Preview 外链，但它接收外部 `previewLink` 和 `videoUrl`，用于模板预览；三个目标 MDX 使用的是 `Preview`，并非这个组件。不能挪用模板的功能作为这三个组件拥有纯预览页的证据。[PreviewTemplate 定义](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/components/mdx/preview-template.tsx#L6)。
5. 页面路由树仅发现首页、文档 catch-all 和 OG 实验室页面，没有 preview、view 或 demo 页面路由。文档页的 `full` 来自 MDX 数据，而非 URL 查询参数。[DocsPage 构造](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/app/docs/%5B%5B...slug%5D%5D/page.tsx#L151)。没有发现可通过 URL 启用的全屏开关。
6. 配置中的 rewrites 仅将文档 `.md` 指向 Markdown 输出；proxy 只做 Markdown 内容协商，并不创建演示页。[next.config.mjs rewrites](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/next.config.mjs#L56)、[proxy](https://github.com/kokonut-labs/kokonutui/blob/4d497b7b03f02ffd07225e638c0b9ace3f892dbb/proxy.ts#L14)。

## 原页链接检查

三个实际页面 HTML 都未提供含 preview、demo 或 view 的外部预览链接；能看到官方 GitHub 仓库链接。原始 HTTP 与链接记录保存在忽略目录 `.cache/newresearch/kokonut-pages.json`，完整源文件在 `.cache/newresearch/kokonut-src/`。

[官方首页](https://kokonutui.com/)提供大量现场演示的目录，但它仍是组件集合，无法充当这三个组件各自的纯演示链接。`/r/<name>.json` 是安装注册表数据，也不是可观看界面。

## 对主库的建议

- 暂时不替换这三个已实测的文档 URL；可明确标记“文档内交互演示”，不称独立全屏体验。
- 如果当前入库标准严格禁止任何文档外壳，应暂时移到候选/待替代区；不能通过猜路由或自部署伪装为官方演示。
- 本次“未发现”限定于上述固定提交、已读取的现行官方页面和链接；未来官方新增路由后可以重新核查。
