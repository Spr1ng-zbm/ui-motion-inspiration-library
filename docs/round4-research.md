# 第四轮：具体界面、工具工作台与差异化动效候选

研究日期：2026-11-03。本轮 35 条，仅为候选；没有浏览器操作、截图核验或视频播放通过。没有修改正式库、发布数据或入库状态。

## 选择与证据边界

- 目标从普通营销首页转向实际可操作界面：影院选座、菜单、图集、布局重排、图像/路径/配色编辑器、音序与频谱、公开分析面板，以及 Rive 的真实演示。
- 去重基线为原 173 条 manifest 与前三轮 79 + 41 + 17 条候选，统一调用已有 URL 规范化规则。35 条均没有规范化 URL 重复。另人工检查入口含义：Music Lab 只选与旧 Song Maker 不同的两项；Museum of Motion 只选三个具体场景，不收录导航首页、不拆同一演示变体凑数。
- HTTP 证据：23 条 HTML GET 200；10 条 Codrops 直链在命令行 GET 返回 403 连接验证，但公开网页读取工具可读到对应演示主体/控件信息；2 条 Rive 官方视频仅做 HEAD，均 200 且 Content-Type=video/mp4。GET/HEAD 都不等于可见效果通过。
- Codrops 的 /Tutorials/ 是部署演示使用的路径；本轮所列为实际演示页面，带图像、画布或操作控件，文章只作为旁边的外链。没有把教程正文当作品收录。访问验证须由后续正常浏览器确认，不尝试绕过。
- UI质量、运动流畅度和移动端适配仍需浏览器审核。依官方描述形成的核查重点已逐条存入 browser_audit_focus，不标成观察结果。

## 优先核查建议

优先 RiveBox、Shoe configurator、Cinema Seat Preview、Rearrange、Motion Smooth Tabs，以及 Squoosh、Haikei、Plausible 的主体与关键控件。影院演示官方注明需要 WebGPU 或 WebGL 2。音频项目优先使用内置素材，不需要麦克风或私人文件。

## Rive：首页链接不是全部都指向可操作项目

来源链由 [Rive 首页](https://rive.app/) 的实际 script_main 脚本，进入首页模块，再进入 [HeroRotator.956b8Ttf.mjs](https://framerusercontent.com/sites/3Hh1SxuP94sycwmlcNuNRW/HeroRotator.956b8Ttf.mjs)。其中明确列出 title、playUrl、video、poster、sourceUrl 等配对数据，并非猜测部署域名。

- Rive City、Rocket Squadron、RiveBox、Shoe configurator：主入口为真实 rive.to 部署地址，四者 GET 200；各自的官方源码仓库也保存在条目中。
- Duolingo、Spotify Wrapped：playUrl 指向官方案例文章，本轮改选相同数据对象中的 MP4 作为录像候选；未称文章可交互，未播放录像。
- Dashboard（车载概念）由主代理负责，不重复纳入本批。其官方 MP4 为 [Dashboard 录像](https://framerusercontent.com/assets/gJRDfn586X2wZK2eEhDhmpR2lng.mp4)。官方说明这是面向 BMW 的非官方概念，不应标为量产车机。该录像只提供给主代理后续实际核验，本轮未核验播放。
- official_showcase_seconds 是轮播配置值，不是读取媒体后测得的时长，不能替代播放器时长证据。

## Music Lab：从官方配置找到纯画布入口

[原站 app.js](https://musiclab.chromeexperiments.com/js/app.js) 实际请求 [landing.json](https://musiclab.chromeexperiments.com/bin/data/landing.json)，其中 Spectrogram / Kandinsky 的 projectUrl 分别指向本批使用的 spectrogram-service 和 kandinsky-service。两者 GET 200。说明文案另核对了 [官方英文语言文件](https://gweb-musiclab-site.appspot.com/static/locales/en/locale-music-lab.json)：频谱图比较声音随时间变化；Kandinsky 将绘图转换成声音。没有猜路由，也没有把动态首页壳误当作品主体。

## 不纳入与暂缓

- cmdk.paco.me 当前重定向至 GitHub README，不再作为独立命令菜单预览入库。
- Umami 官网没有找到当前公开演示链接，因此不拿营销首页充数。
- Grafana 搜索结果中多条 dashboard 明确返回 Not found；另一些示例大量 No data，本轮不纳入。
- A Drift、Custom-Shaped Cursor Trail、Pointer Square Lens、Depth Gallery、Sticky Grid Scroll：虽找到具体页面，但为控制同站与同类效果占比，本轮暂缓；不是判定作品质量差。
- 808303.studio 已跳转至 Roland50.studio，按新版实际入口收录，避免旧项目和新入口重复计数。
- Photopea 初次 HTTP 超时，重试后 GET 200；以最终实际检查记录为准。

## 候选逐项列表

以下“参考点”来自原作者页面、页面元数据或官方公开配置，不是本轮浏览器实测观察。

| # | 作品 | 分类 | 参考点 | 来源证据 | HTTP范围 |
|---|---|---|---|---|---|

| 1 | [Lookbook：时装图片悬停](https://tympanus.net/Demos/LookbookHoverEffects/) | 画廊与导航 | 具体时装图集的 WebGL 悬停演示，主体有六组服装照片与对应 Look 标注。 | [官方来源](https://tympanus.net/Demos/LookbookHoverEffects/) | GET 403；未浏览器核验 |
| 2 | [Seam：森林图集滚动转场](https://tympanus.net/Demos/SeamTransitions/) | 滚动与叙事 | 以森林再生项目为内容的滚动转场演示，含完整标题、照片与项目年份编排。 | [官方来源](https://tympanus.net/Demos/SeamTransitions/) | GET 403；未浏览器核验 |
| 3 | [Cinema Seat Preview：影院选座视角](https://tympanus.net/Demos/CinemaSeatPreview/) | 完整界面 | 影院座位选择原型，原页提供座位状态、视角预览提示和添加票券控件。 | [官方来源](https://tympanus.net/Demos/CinemaSeatPreview/) | GET 403；未浏览器核验 |
| 4 | [Clip Menu：裁切展开的游戏菜单](https://tympanus.net/Development/EaseReverseClipMenu/) | 画廊与导航 | 带菜单开关和中断速度控制的裁切菜单演示，以游戏任务和设置作为导航内容。 | [官方来源](https://tympanus.net/Development/EaseReverseClipMenu/) | GET 403；未浏览器核验 |
| 5 | [Glass Xylophone：玻璃木琴](https://tympanus.net/Tutorials/Xylophone/) | 声音与可视化 | 原作者的独立玻璃木琴演示，页面提供声音开关，结合三维琴键与音乐交互。 | [官方来源](https://tympanus.net/Tutorials/Xylophone/) | GET 403；未浏览器核验 |
| 6 | [Thumbnail Flow：缩略图路径展开](https://tympanus.net/Tutorials/MotionPathTransition/) | 画廊与导航 | 图像列表与 Open/Close 控件组成的独立演示，主题是沿 MotionPath 排列与展开缩略图。 | [官方来源](https://tympanus.net/Tutorials/MotionPathTransition/) | GET 403；未浏览器核验 |
| 7 | [SVG Mask：百叶窗图片转场](https://tympanus.net/Tutorials/SVGMaskScrollTransition/) | 滚动与叙事 | 独立演示将图片分成水平矩形遮罩，随滚动逐段展开至下一张图。 | [官方来源](https://tympanus.net/Tutorials/SVGMaskScrollTransition/) | GET 403；未浏览器核验 |
| 8 | [Museum of Motion：Luxury 完整动效场景](https://tympanus.net/Demos/MuseumOfMotion/exhibits/luxury/) | 滚动与叙事 | 独立场景组合遮罩文字入场、图片狭缝揭示、横向固定画廊与聚光细节。 | [官方来源](https://tympanus.net/Demos/MuseumOfMotion/exhibits/luxury/) | GET 403；未浏览器核验 |
| 9 | [Museum of Motion：Printed 印刷场景](https://tympanus.net/Demos/MuseumOfMotion/exhibits/printed/) | 文字与排版 | 独立场景结合油墨文字、印刷套色错位、刷印揭示和纸角揭起。 | [官方来源](https://tympanus.net/Demos/MuseumOfMotion/exhibits/printed/) | GET 403；未浏览器核验 |
| 10 | [Museum of Motion：Rearrange 布局重排](https://tympanus.net/Demos/MuseumOfMotion/exhibits/rearrange/) | 微交互 | 提供 Layout、List、Shuffle、Shared、Shape 五种切换控件的布局重排演示。 | [官方来源](https://tympanus.net/Demos/MuseumOfMotion/exhibits/rearrange/) | GET 403；未浏览器核验 |
| 11 | [Photopea：完整图像编辑工作台](https://www.photopea.com/) | 完整界面 | 可在浏览器运行的图像编辑器，官方列出图层、蒙版、路径与矢量编辑能力。 | [官方来源](https://www.photopea.com/) | GET 200；未浏览器核验 |
| 12 | [Squoosh：双侧图像压缩比较](https://squoosh.app/) | 完整界面 | 图像优化工具，原页提供照片、插画、设备画面等示例，以及压缩前后的比较流程。 | [官方来源](https://squoosh.app/) | GET 200；未浏览器核验 |
| 13 | [Haikei：SVG 图形生成工作台](https://app.haikei.app/) | 完整界面 | 在线 SVG 设计工具，官方提供波浪、山峰、团块、网格等生成器及画布参数。 | [官方来源](https://haikei.app/) | GET 200；未浏览器核验 |
| 14 | [PatternPad：几何纹样编辑器](https://patternpad.com/editor.html) | 完整界面 | 可调整颜色与形状参数的几何图案工具，入口由原站 Create Your Pattern 按钮明确提供。 | [官方来源](https://patternpad.com/) | GET 200；未浏览器核验 |
| 15 | [SVG Path Editor：路径与锚点编辑](https://yqnn.github.io/svg-path-editor/) | 完整界面 | 作者公开部署的 SVG 路径编辑器，适合研究画布、路径命令与精确控制之间的关系。 | [官方来源](https://github.com/Yqnn/svg-path-editor) | GET 200；未浏览器核验 |
| 16 | [cubic-bezier：缓动曲线比较](https://cubic-bezier.com/) | 微交互 | 贝塞尔曲线工具提供时长控制、Go 预览及不同曲线的并列比较。 | [官方来源](https://cubic-bezier.com/) | GET 200；未浏览器核验 |
| 17 | [Polotno Studio：海报与图形编辑器](https://polotno.com/studio) | 完整界面 | 实际在线设计编辑器，可用于社交图片、视频和印刷图形；主入口为工作台而非产品介绍页。 | [官方来源](https://polotno.com/studio) | GET 200；未浏览器核验 |
| 18 | [OKLCH：色域与颜色工作台](https://oklch.com/) | 完整界面 | 颜色转换与选择工具，提供 OKLCH/LCH 切换、P3 色域提示和 sRGB 回退颜色。 | [官方来源](https://oklch.com/) | GET 200；未浏览器核验 |
| 19 | [Plausible：公开网站分析仪表盘](https://plausible.io/plausible.io) | 完整界面 | 由 Plausible 官网 View live demo 明确链接的公开分析面板，用于参考指标、趋势与筛选层级。 | [官方来源](https://plausible.io/) | GET 200；未浏览器核验 |
| 20 | [Roland50 Studio：电子乐器控制台](https://roland50.studio/) | 声音与可视化 | Roland 与 Yuri Suzuki 合作的数字乐器界面；原 808303 项目现跳转至这一升级版。 | [官方来源](https://roland50.studio/about) | GET 200；未浏览器核验 |
| 21 | [Blob Opera：拖动声部合唱](https://artsandculture.google.com/experiment/blob-opera/AAHWrq360NcGbw) | 声音与可视化 | 四个歌剧声部的实时交互作品，官方说明上下拖动改变音高、前后拖动改变元音。 | [官方来源](https://artsandculture.google.com/experiment/blob-opera/AAHWrq360NcGbw) | GET 200；未浏览器核验 |
| 22 | [Music Lab：声音频谱画布](https://musiclab.chromeexperiments.com/spectrogram-service/) | 声音与可视化 | 用频谱显示声音随时间的变化，官方提供多种乐器样本供比较。 | [官方来源](https://musiclab.chromeexperiments.com/bin/data/landing.json) | GET 200；未浏览器核验 |
| 23 | [Music Lab：Kandinsky 图形作曲](https://musiclab.chromeexperiments.com/kandinsky-service/) | 声音与可视化 | 将绘制的线条、圆形、三角和涂鸦转换成声音的画布作品。 | [官方来源](https://musiclab.chromeexperiments.com/bin/data/landing.json) | GET 200；未浏览器核验 |
| 24 | [AudioMass：波形编辑工作台](https://audiomass.co/) | 完整界面 | 完整浏览器音频与波形编辑器，可研究时间线、音频选择和工具面板。 | [官方来源](https://audiomass.co/) | GET 200；未浏览器核验 |
| 25 | [BeepBox：音序与循环编辑器](https://www.beepbox.co/) | 声音与可视化 | 通过音符网格、分段图案和循环范围编辑器组织器乐音乐的在线工具。 | [官方来源](https://www.beepbox.co/) | GET 200；未浏览器核验 |
| 26 | [Motion：滑动指示器标签页](https://examples.motion.dev/react/smooth-tabs) | 微交互 | 官方示例为分段标签控件，使用滑动指示器与带方向感的内容转场。 | [官方来源](https://examples.motion.dev/react/smooth-tabs) | GET 200；未浏览器核验 |
| 27 | [Motion：Base UI 下拉菜单](https://examples.motion.dev/react/base-menu) | 微交互 | 基于 Base UI 的下拉菜单动效示例，提供独立公开预览页面。 | [官方来源](https://examples.motion.dev/react/base-menu) | GET 200；未浏览器核验 |
| 28 | [Motion：轮播与灯箱共享导航](https://examples.motion.dev/react/carousel-lightbox) | 画廊与导航 | 官方轮播示例可点击照片打开灯箱；灯箱内继续提供轮播与缩略图导航。 | [官方来源](https://examples.motion.dev/react/carousel-lightbox) | GET 200；未浏览器核验 |
| 29 | [Motion：随滚动方向隐藏页头](https://examples.motion.dev/react/scroll-hide-header) | 滚动与叙事 | 固定页头随向下滚动隐藏、向上滚动重新出现的官方独立演示。 | [官方来源](https://examples.motion.dev/react/scroll-hide-header) | GET 200；未浏览器核验 |
| 30 | [Rive City：城市与矢量 HUD](https://rive-city-cr4bhd.rive.to/) | 游戏与趣味 | 在同一场景中结合三维城市与矢量界面的官方演示。 | [官方来源](https://framerusercontent.com/sites/3Hh1SxuP94sycwmlcNuNRW/HeroRotator.956b8Ttf.mjs) | GET 200；未浏览器核验 |
| 31 | [Duolingo：官方角色与界面录像](https://framerusercontent.com/assets/RT0g2f4dz5zYO4UphLss616U4.mp4) | 完整界面 | Rive 官方首页用于展示 Duolingo 中角色、UI 和棋类课程的短录像。 | [官方来源](https://framerusercontent.com/sites/3Hh1SxuP94sycwmlcNuNRW/HeroRotator.956b8Ttf.mjs) | HEAD 200；未播放 |
| 32 | [Rocket Squadron：飞行游戏界面](https://rocket-squadron-1cu9sz.rive.to/?fit=layout) | 游戏与趣味 | 官方轨道射击演示，将二维飞行员与三维世界放在同一个 Rive 文件中。 | [官方来源](https://framerusercontent.com/sites/3Hh1SxuP94sycwmlcNuNRW/HeroRotator.956b8Ttf.mjs) | GET 200；未浏览器核验 |
| 33 | [Spotify Wrapped：官方年度回顾动效录像](https://framerusercontent.com/assets/KzXZgGGMns7LaW6Bz5BAJj7Nw.mp4) | 完整界面 | Rive 官方首页展示 Spotify Wrapped 2025 数据驱动动画的短录像。 | [官方来源](https://framerusercontent.com/sites/3Hh1SxuP94sycwmlcNuNRW/HeroRotator.956b8Ttf.mjs) | HEAD 200；未播放 |
| 34 | [RiveBox：游戏主机界面](https://rivebox-yrdeql.rive.to/) | 完整界面 | 游戏主机仪表盘演示，将可操作菜单面板映射到三维空间，包含游戏库和音乐播放器主题。 | [官方来源](https://framerusercontent.com/sites/3Hh1SxuP94sycwmlcNuNRW/HeroRotator.956b8Ttf.mjs) | GET 200；未浏览器核验 |
| 35 | [Rive：鞋款配置器](https://living-print-2b8mhd.rive.to/?fit=layout) | 完整界面 | 将三维产品与响应式矢量 UI 结合的产品配置演示。 | [官方来源](https://framerusercontent.com/sites/3Hh1SxuP94sycwmlcNuNRW/HeroRotator.956b8Ttf.mjs) | GET 200；未浏览器核验 |

## 分布与交付

- 数据：`candidate_items_round4.json`，35 条。
- 分类：画廊与导航 4；滚动与叙事 4；完整界面 14；声音与可视化 6；文字与排版 1；微交互 4；游戏与趣味 2。
- 记录明确保留 review_status=candidate、browser_verified=false；两条视频另保留 playback_verified=false。
- 原始 HTTP、官方配置摘取和生成脚本保存在忽略目录 `.cache/newresearch/`；报告与 JSON 中的官方来源 URL 可独立复核。
- 正式入库必须由主流程补实际动作与观察；本轮不因来源权威、HTTP 200 或官方宣传直接授予 pass。
