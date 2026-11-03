# 第二轮 UI / 动效候选研究

核查日期：2026-11-03。最终保存 41 条候选，覆盖 26 个域名：26 个完整界面、15 个具体在线演示；全部 `candidate`、`browser_verified=false`。

本轮沿用 research 技能，以原作者页面和官方产品页面为证据。GET 200 只表示取得页面，不表示视觉或交互通过；没有操作浏览器，没有给任何条目补写实测结果。

去重范围：site_items.json、ui_example_items.json、code_items.json、direct_demo_items.json、video_items.json 与 candidate_items_20261103.json。URL 忽略 www 和末尾斜杠，另外检查实际重定向目标。第一轮79条未被改写。

## 发现路径与选择标准

- [Rauno Craft 原作者列表](https://rauno.me/craft)：跟随页面的具体原型链接，保留独立控件；排除内容以实现文章为主的 Graph Slider。
- [shadcn 官方 Blocks](https://ui.shadcn.com/blocks)：直接读取页面已提供的 `/view/new-york-v4/…` 链接，只收具体全屏预览，不收组件导航页。
- 商业产品：直接读取官方产品页，明确区分产品展示网页与需要账号/下载的应用；不声称免费应用操作已通过。
- [Made With GSAP 项目展示](https://madewithgsap.com/showcase)：仅作发现入口，跟随作者列出的实际作品域名，再用作品自己的页面内容核对主题；不把展示列表加入库，也不依据入选标签宣称本次看到动画。

## 候选明细

| 作品与原始来源 | 类型 | 已有内容证据 / 推荐核查点 |
|---|---|---|
| [Rauno · Exclusion Tabs](https://rauno.me/craft/exclusion-tabs) · [原始请求](https://rauno.me/craft/exclusion-tabs) | 导航与微交互 / 在线演示 | 原作者的标签导航原型，页面提供 All Posts、Engineering、Community 等选项。 待核查：点击不同标签，检查选中背景、文字与切换过渡。 |
| [Rauno · Vanish Input](https://rauno.me/craft/vanish-input) · [原始请求](https://rauno.me/craft/vanish-input) | 导航与微交互 / 在线演示 | 原作者的消隐输入原型，页面明确提示输入文字后按 Enter。 待核查：输入短句并按 Enter，确认消隐反馈和再次输入。 |
| [Rauno · Wheel Input](https://rauno.me/craft/wheel-input) · [原始请求](https://rauno.me/craft/wheel-input) | 导航与微交互 / 在线演示 | 独立日期滚轮原型，页面提供月、年、日的连续选项。 待核查：分别拖动或滚动三个选择列，检查居中状态和吸附。 |
| [Rauno · Vercel Footer](https://rauno.me/craft/vercel-footer) · [原始请求](https://rauno.me/craft/vercel-footer) | 导航与微交互 / 在线演示 | 原作者的 Vercel 页脚原型，另附官方演示录像。 待核查：用指针移动和触碰主体，确认页脚反馈；必要时播放原页录像。 |
| [Rauno · Logo Carousel](https://rauno.me/craft/logo-carousel) · [原始请求](https://rauno.me/craft/logo-carousel) | 导航与微交互 / 在线演示 | 原作者的独立 Logo Carousel 原型页，可供品牌标志展示参考。 待核查：观察完整周期，再检查指针进入前后是否有状态变化。 |
| [Rauno · Adaptive Precision](https://rauno.me/craft/adaptive-precision) · [原始请求](https://rauno.me/craft/adaptive-precision) | 导航与微交互 / 在线演示 | 带 1 PM 至 5 PM 刻度的精度控制原型，附作者演示录像。 待核查：按住并拖动控件，结合原页录像核查精度变化。 |
| [Rauno · Radial Menu](https://rauno.me/craft/radial-menu) · [原始请求](https://rauno.me/craft/radial-menu) | 导航与微交互 / 在线演示 | 原作者的径向菜单，页面指引按住并旋转。 待核查：按住旋转并松开，检查菜单展开、当前项和收起。 |
| [Rauno · Minimap](https://rauno.me/craft/minimap) · [原始请求](https://rauno.me/craft/minimap) | 滚动与版式 / 在线演示 | 原作者的独立 Minimap 界面原型。 待核查：检查主体内容与缩略导航是否联动，并记录可用操作。 |
| [Rauno · Fractional Slider](https://rauno.me/craft/fractional-slider) · [原始请求](https://rauno.me/craft/fractional-slider) | 导航与微交互 / 在线演示 | 带 -90 至 90 刻度的滑动原型，页面明确支持滚动或拖动。 待核查：分别用滚轮和拖动调整数值，确认刻度位移与选中反馈。 |
| [Rauno · Precision Slider](https://rauno.me/craft/precision-slider) · [原始请求](https://rauno.me/craft/precision-slider) | 导航与微交互 / 在线演示 | 独立精度滑块原型，页面指引按住并拖动。 待核查：按住拖动检查数值调整、反馈及释放状态。 |
| [Rauno · Flashlight Tabs](https://rauno.me/craft/flashlight-tabs) · [原始请求](https://rauno.me/craft/flashlight-tabs) | 导航与微交互 / 在线演示 | 原作者的标签原型，包含 Home、Projects、Deployments、Members、Settings。 待核查：移动指针并切换标签，分别检查悬停与选中状态。 |
| [Rauno · Copy & Paste](https://rauno.me/craft/copy-paste) · [原始请求](https://rauno.me/craft/copy-paste) | 导航与微交互 / 在线演示 | 原作者的复制粘贴界面原型，另附官方演示录像。 待核查：使用指针检查主体提供的复制粘贴反馈；不读取系统剪贴板中的现有内容。 |
| [shadcn · Dashboard 01 完整数据界面](https://ui.shadcn.com/view/new-york-v4/dashboard-01) · [原始请求](https://ui.shadcn.com/view/new-york-v4/dashboard-01) | 应用与数据界面 / 完整界面 | 官方完整预览包含收入与用户指标、访客时间范围和可定制列的数据表。 待核查：切换图表时间范围、表格视图和侧栏；验证主体不是文档截图。 |
| [shadcn · 可折叠应用侧栏](https://ui.shadcn.com/view/new-york-v4/sidebar-07) · [原始请求](https://ui.shadcn.com/view/new-york-v4/sidebar-07) | 应用与数据界面 / 在线演示 | 官方应用侧栏预览含工作区、分组菜单、项目与账户区域。 待核查：折叠侧栏并展开菜单，检查图标模式和弹出层。 |
| [shadcn · 文档目录侧栏](https://ui.shadcn.com/view/new-york-v4/sidebar-03) · [原始请求](https://ui.shadcn.com/view/new-york-v4/sidebar-03) | 应用与数据界面 / 在线演示 | 官方目录侧栏预览包含入门、应用构建、API 与架构分组。 待核查：切换目录分组和侧栏开关，检查长目录层级与布局。 |
| [shadcn · Login 03 认证界面](https://ui.shadcn.com/view/new-york-v4/login-03) · [原始请求](https://ui.shadcn.com/view/new-york-v4/login-03) | 应用与数据界面 / 完整界面 | 官方登录预览展示 Apple、Google 登录入口与邮件密码表单。 待核查：只核对布局、聚焦和表单状态，不提交账户信息或调用第三方登录。 |
| [shadcn · Login 04 认证界面](https://ui.shadcn.com/view/new-york-v4/login-04) · [原始请求](https://ui.shadcn.com/view/new-york-v4/login-04) | 应用与数据界面 / 完整界面 | 另一套官方认证界面，含邮件密码字段、第三方入口和注册提示。 待核查：对比桌面与窄屏排版，检查输入聚焦；不要实际注册。 |
| [Warp Terminal](https://www.warp.dev/terminal) · [原始请求](https://www.warp.dev/terminal) | 完整界面 / 完整界面 | 官方终端产品页，专门展示终端而非当前首页的软件工厂平台。 待核查：检查产品主体和终端展示素材，区分录制示例与实际可输入控件。 |
| [Zed 编辑器](https://zed.dev/) · [原始请求](https://zed.dev/) | 完整界面 / 完整界面 | 官方编辑器产品页介绍代码编辑、协作和代理工作流。 待核查：核对编辑器截图、面板层次及页面的产品展示。 |
| [Obsidian 知识工作台](https://obsidian.md/) · [原始请求](https://obsidian.md/) | 完整界面 / 完整界面 | 官方私人笔记产品页，提供应用功能与多设备展示入口。 待核查：检查笔记编辑、关系视图等实际展示素材及页面导航。 |
| [AFFiNE 文档与白板](https://affine.pro/) · [原始请求](https://affine.pro/) | 完整界面 / 完整界面 | 官方页面展示文档、白板和数据库在同一知识工作区中的定位，并提供首屏视频占位。 待核查：核对首屏产品视频、文档/白板界面展示及滚动内容。 |
| [HEY 邮件与日历](https://www.hey.com/) · [原始请求](https://www.hey.com/) | 完整界面 / 完整界面 | 37signals 的邮件与日历产品页，原页提供 overview 产品图片与演示视频。 待核查：查看产品总览、邮件和日历界面，确认视频可播放。 |
| [Evervault 支付产品界面](https://evervault.com/) · [原始请求](https://evervault.com/) | 完整界面 / 完整界面 | 官方支付基础设施产品站，围绕卡片收集、数据保护和支付能力展开。 待核查：核对首屏、产品模块、卡片或流程展示的实际质量。 |
| [Felt 地图工作台](https://felt.com/) · [原始请求](https://felt.com/) | 完整界面 / 完整界面 | 官方地图产品站介绍资产与现场业务地图，页面提供地图主题首屏视频。 待核查：检查地图工作区展示和叠加信息层；区分录制素材与可操作地图。 |
| [Cal.com 预约日程](https://cal.com/) · [原始请求](https://cal.com/) | 完整界面 / 完整界面 | 官方排程产品站，围绕个人、团队与组织的预约界面展开。 待核查：检查日期、时间段与预约流程展示，不实际创建预约。 |
| [Notion 工作空间](https://www.notion.com/) · [原始请求](https://www.notion.com/) | 完整界面 / 完整界面 | 官方工作空间产品页包含产品模块与首屏演示媒体。 待核查：查看具体工作空间演示，检查模块切换与页面层级。 |
| [Figma Design 产品界面](https://www.figma.com/design/) · [原始请求](https://www.figma.com/design/) | 完整界面 / 完整界面 | Figma 的具体 Design 产品页，聚焦设计与原型协作。 待核查：检查画布、工具栏和协作展示素材，不以导航中其他产品数量计数。 |
| [Penpot 设计工作台](https://penpot.app/) · [原始请求](https://penpot.app/) | 完整界面 / 完整界面 | 官方设计平台页，展示设计、代码及协作功能定位。 待核查：核对编辑器主体素材、面板和多用户设计场景。 |
| [Tana 会议工作台](https://tana.inc/) · [原始请求](https://www.tana.inc/) | 完整界面 / 完整界面 | 当前 Tana 官方产品为代理会议平台，页面含会议首屏视频；不是旧版 Supertags 笔记产品。 待核查：检查会议界面与任务展示，不沿用旧笔记产品的描述。 |
| [Capacities 知识工作台](https://capacities.io/) · [原始请求](https://capacities.io/) | 完整界面 / 完整界面 | 官方介绍以相互连接的对象组织知识，并提供桌面与移动端产品入口。 待核查：核对对象卡片、内容组织和多设备界面的实际展示。 |
| [Playdate 产品官网](https://play.date/) · [原始请求](https://www.play.date/) | 完整界面 / 完整界面 | Panic 的掌机官网，以设备、游戏和购买信息组成完整产品页面。 待核查：检查设备与游戏展示、页面滚动和视频；不进行购买。 |
| [Daylight DC-1 产品官网](https://daylightcomputer.com/) · [原始请求](https://www.daylightcomputer.com/) | 完整界面 / 完整界面 | DC-1 设备的官方产品页，包含设备介绍与分段产品文案。 待核查：检查设备视觉、滚动呈现及文字处理，不把文案分字自动当作动画已通过。 |
| [teenage engineering 产品官网](https://teenage.engineering/) · [原始请求](https://www.teenage.engineering/) | 完整界面 / 完整界面 | 官方音乐设备站，包含产品、商店和设备内容的完整导航。 待核查：检查产品图、目录排版和菜单，不提交购买。 |
| [Opal 专注应用](https://opalapp.com/) · [原始请求](https://www.opal.so/) | 完整界面 / 完整界面 | Opal 官方专注产品页，展示专注评分与屏幕使用场景，并含桌面/移动首屏录像。 待核查：播放首屏素材，检查应用界面和评分展示；原域名已跳转至 opalapp.com。 |
| [Atmos Gallery 配色工作台](https://atmos.gallery/) · [原始请求](https://atmos.gallery) | 应用与数据界面 / 在线演示 | 具体图片取色工具，官方描述提供五色提取、对比度检查及设计格式导出。 待核查：先使用页面现有示例检查调色板和导出界面；不要上传私人图片。 |
| [Aardvark Book Club](https://www.aardvarkbookclub.com/) · [原始请求](https://aardvarkbookclub.com) | 完整界面 / 完整界面 | 图书订阅品牌官网，包含当月书目、书籍详情和订阅内容。 待核查：检查书目展示、菜单和滚动布局；不订阅或购买。 |
| [MoMoney 博物馆官网](https://museumofmoney.com/) · [原始请求](https://www.museumofmoney.com) | 完整界面 / 完整界面 | 达拉斯 Museum of Money 的官方网站，含展览、参观及活动信息。 待核查：检查展览内容、页面滚动与菜单；不把实体展览的互动性当成网站交互证据。 |
| [House of Corto 家具作品](https://www.houseofcorto.com/) · [原始请求](https://www.houseofcorto.com) | 完整界面 / 完整界面 | Jessica Mille 的家具品牌站，提供具名桌椅作品、品牌信息及购物袋。 待核查：检查家具展示、菜单与购物袋样式；正文含占位文本，若在画面可见应降级或剔除。 |
| [Lando Norris 官方网站](https://landonorris.com/) · [原始请求](https://landonorris.com) | 滚动与版式 / 完整界面 | 车手官方站含赛道内外内容、赛事日历及锁定/返回滚动提示。 待核查：检查加载后主体、滚动导航与页面所提示的锁定操作。 |
| [MANA Yerba Maté](https://manayerbamate.com/) · [原始请求](https://manayerbamate.com) | 完整界面 / 完整界面 | 魁北克马黛茶品牌站，以口味分类、产品和订阅组成完整电商界面。 待核查：检查口味切换、产品展示、语言菜单和滚动；不购买。 |
| [TrueKind 护肤品牌](https://truekindskincare.com/) · [原始请求](https://truekindskincare.com) | 完整界面 / 完整界面 | 护肤品牌官网含产品、品牌理念、画廊与购物车，原页包含视频元素。 待核查：检查首屏视频、商品展示和菜单，不将备用视频提示直接判为失败。 |

## 剔除或暂缓

- https://read.cv/：实测 GET 402，未纳入。
- https://ui.shadcn.com/examples：GET 404；改用官方 Blocks 明确给出的全屏预览。
- https://v3.shadcn.com/examples/mail：本轮请求超时，未纳入。
- https://www.lumenartspace.com：本轮请求超时，未纳入。
- https://rauno.me/craft/graph-slider：页面主体有较多实现说明和代码，不符合本轮减少教程文章的方向，未纳入。
- https://www.framer.com/ 与 https://www.cleanshot.com/：与已有来源重复（包含 www 跳转差异），未纳入。
- Warp 首页已经转向软件工厂平台，改跟随原页的 /terminal 链接核查具体终端展示。

## 必须保留的限制

- House of Corto 的 HTML 有占位文本，主流程应优先检查其是否可见；若画面影响质量应直接剔除。
- Atmos Gallery 原页说明会向 Anthropic 发送缩小图片进行命名。核查仅使用网站已有公开示例，不上传私人素材。
- Rauno 中 Vercel Footer、Adaptive Precision、Copy & Paste 明示需要指针设备，并提供原作者录像；不要仅凭移动端静态画面判为坏链。
- Tana 当前官网内容为会议平台，未沿用其旧版笔记产品身份。Opal 实际跳转为 opalapp.com，Playdate 与 teenage engineering 等统一使用真实最终域名。
- OG 封面不是浏览器截图；`official_media_urls` 仅表示媒体 URL 出现在原页，不表示已经播放。
- 原始 HTTP 记录、HTML 和生成脚本在忽略目录 `.cache/newresearch/round2-*`，不需要发布下载的页面内容。

## 数据核验结果

41 个最终条目的 GET 状态均为 200，curl 请求完成；归一化 URL 无内部重复，且与现有五个来源文件及第一轮79候选无重复。JSON 必填字段、候选标记和原始证据链接均已检查。浏览器实际画面核验数仍为 0。
