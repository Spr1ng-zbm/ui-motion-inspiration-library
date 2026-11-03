# 具体 UI 与动效补充来源

日期：2026-11-03。目标是具体作品和直接预览，排除课程与纯教程。
候选 53 项，GET 与页面检查通过 50 项，未通过 3 项。

## 方法

全部目标逐项请求 GET，要求 HTTP 200、非空 HTML、页面标题不是错误或挑战页、最终地址没有跳登录。组件页以官方组件目录/站点地图确认真实路由，Aceternity/Magic UI 页面提取 Preview 结构线索；React Bits 的独立标题与官方路由已确认，但 Preview 由客户端渲染。组件正文同时存在代码说明。没有把 HTTP 200 视为已实际播放或运行动画。
React Bits 路由与说明：[官方站点地图](https://reactbits.dev/sitemap.xml)、[官方组件清单](https://reactbits.dev/llms.txt)。Aceternity：[官方组件 API](https://ui.aceternity.com/api/components)。Magic UI：[官方组件站点地图](https://magicui.design/sitemap.xml)。独立三维作品的发现来源：[Bruno 的精选](https://threejs-journey.com/selection/1)，目标链接仍直接指向作品。
限制：本轮核验页面和入口，没有浏览器实测。所有记录 browser_verified=false；需要后续浏览器复核排除长期loading、黑屏、运行异常。WebGPU 专项已明确标注浏览器要求。缩略图来自官方页面元数据，没有下载搬运第三方素材。

## 收录条目

### React Bits · 逐字分裂入场
- [直接打开](https://reactbits.dev/text-animations/split-text) — 文字拆为字母或单词，错开节奏进入；适合首屏标题和段落揭示。
- [来源](https://reactbits.dev/text-animations/split-text)；HTTP 200；标题：Split Text — React Text Animation | React Bits
- 最终地址：https://reactbits.dev/text-animations/split-text

### React Bits · 文字从模糊中浮现
- [直接打开](https://reactbits.dev/text-animations/blur-text) — 文字逐步从模糊变清晰，以柔和的焦点变化替代硬切换。
- [来源](https://reactbits.dev/text-animations/blur-text)；HTTP 200；标题：Blur Text — React Text Animation | React Bits
- 最终地址：https://reactbits.dev/text-animations/blur-text

### React Bits · 金属扫光文字
- [直接打开](https://reactbits.dev/text-animations/shiny-text) — 窄光带扫过文字表面，适合按钮、状态标签和低强度强调。
- [来源](https://reactbits.dev/text-animations/shiny-text)；HTTP 200；标题：Shiny Text — React Text Animation | React Bits
- 最终地址：https://reactbits.dev/text-animations/shiny-text

### React Bits · 滚动悬浮字形
- [直接打开](https://reactbits.dev/text-animations/scroll-float) — 标题随滚动逐字浮起，参考字形位置与阅读进度的配合。
- [来源](https://reactbits.dev/text-animations/scroll-float)；HTTP 200；标题：Scroll Float — React Text Animation | React Bits
- 最终地址：https://reactbits.dev/text-animations/scroll-float

### React Bits · 弧面拖拽画廊
- [直接打开](https://reactbits.dev/components/circular-gallery) — 图片排成弯曲的连续画廊，可拖拽和滚动浏览，适合项目展示。
- [来源](https://reactbits.dev/components/circular-gallery)；HTTP 200；标题：Circular Gallery — React Component | React Bits
- 最终地址：https://reactbits.dev/components/circular-gallery

### React Bits · 可甩动的卡片堆
- [直接打开](https://reactbits.dev/components/stack) — 卡片支持拖拽和甩动，被移开的卡片回到队尾，适合故事与内容选择。
- [来源](https://reactbits.dev/components/stack)；HTTP 200；标题：Stack — React Component | React Bits
- 最终地址：https://reactbits.dev/components/stack

### React Bits · 球面无限菜单
- [直接打开](https://reactbits.dev/components/infinite-menu) — 将图像入口组织成可拖拽的球面空间，适合少量高视觉项目的探索。
- [来源](https://reactbits.dev/components/infinite-menu)；HTTP 200；标题：Infinite Menu — React Component | React Bits
- 最终地址：https://reactbits.dev/components/infinite-menu

### React Bits · 流线光丝背景
- [直接打开](https://reactbits.dev/backgrounds/threads) — 细密线条构成可随指针变化的光丝场，适合轻盈科技风背景。
- [来源](https://reactbits.dev/backgrounds/threads)；HTTP 200；标题：Threads — React Background | React Bits
- 最终地址：https://reactbits.dev/backgrounds/threads

### React Bits · 虹彩流动背景
- [直接打开](https://reactbits.dev/backgrounds/iridescence) — 柔和虹彩在平面上流动，适合克制的产品首屏和抽象色彩参考。
- [来源](https://reactbits.dev/backgrounds/iridescence)；HTTP 200；标题：Iridescence — React Background | React Bits
- 最终地址：https://reactbits.dev/backgrounds/iridescence

### React Bits · 可推动的物理球池
- [直接打开](https://reactbits.dev/backgrounds/ballpit) — 柔光球体可受指针推动、抓取和抛掷，适合有触感的互动开场。
- [来源](https://reactbits.dev/backgrounds/ballpit)；HTTP 200；标题：Ballpit — React Background | React Bits
- 最终地址：https://reactbits.dev/backgrounds/ballpit

### React Bits · 发光能量球
- [直接打开](https://reactbits.dev/backgrounds/orb) — 以流动光带构成球形视觉中心，适合 AI 状态、语音助手和首屏主视觉。
- [来源](https://reactbits.dev/backgrounds/orb)；HTTP 200；标题：Orb — React Background | React Bits
- 最终地址：https://reactbits.dev/backgrounds/orb

### React Bits · 像素旋涡背景
- [直接打开](https://reactbits.dev/backgrounds/balatro) — 旋转的像素色带形成复古动态底纹，适合游戏或实验性视觉。
- [来源](https://reactbits.dev/backgrounds/balatro)；HTTP 200；标题：Balatro — React Background | React Bits
- 最终地址：https://reactbits.dev/backgrounds/balatro

### Aceternity · Apple 风卡片展开
- [直接打开](https://ui.aceternity.com/components/apple-cards-carousel) — 横向大卡片轮播与详情展开，适合产品功能分组和编辑式内容展示。
- [来源](https://ui.aceternity.com/components/apple-cards-carousel)；HTTP 200；标题：Apple Cards Carousel | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/apple-cards-carousel

### Aceternity · 层叠人物推荐卡
- [直接打开](https://ui.aceternity.com/components/animated-testimonials) — 堆叠照片与文字同步切换，可参考图像层级和内容变化的衔接。
- [来源](https://ui.aceternity.com/components/animated-testimonials)；HTTP 200；标题：Animated Testimonials | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/animated-testimonials

### Aceternity · 滚动时间轴
- [直接打开](https://ui.aceternity.com/components/timeline) — 长时间轴把节点、图片和说明组织在滚动路径上，适合历程与项目过程。
- [来源](https://ui.aceternity.com/components/timeline)；HTTP 200；标题：Timeline Component for React & Tailwind CSS | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/timeline

### Aceternity · 粘性滚动内容揭示
- [直接打开](https://ui.aceternity.com/components/sticky-scroll-reveal) — 滚动文本与固定视觉区域联动，适合功能介绍和连续故事段落。
- [来源](https://ui.aceternity.com/components/sticky-scroll-reveal)；HTTP 200；标题：Sticky Scroll Reveal | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/sticky-scroll-reveal

### Aceternity · 悬浮 Dock 导航
- [直接打开](https://ui.aceternity.com/components/floating-dock) — 图标在指针靠近时放大，适合轻量工具栏和常用入口。
- [来源](https://ui.aceternity.com/components/floating-dock)；HTTP 200；标题：Floating Dock | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/floating-dock

### Aceternity · 路径流动光束
- [直接打开](https://ui.aceternity.com/components/background-beams) — 多条渐变光束沿曲线路径移动，适合表单或首屏背后的纵深氛围。
- [来源](https://ui.aceternity.com/components/background-beams)；HTTP 200；标题：Background Beams Animation for React | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/background-beams

### Aceternity · 黏液式搜索输入
- [直接打开](https://ui.aceternity.com/components/gooey-input) — 搜索控件借助黏连形变展开，参考紧凑按钮到输入状态的过渡。
- [来源](https://ui.aceternity.com/components/gooey-input)；HTTP 200；标题：Gooey Input | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/gooey-input

### Aceternity · 折射液态玻璃
- [直接打开](https://ui.aceternity.com/components/liquid-glass) — 玻璃表面折射背后内容并带有弯曲边缘与色散，适合材质化界面参考。
- [来源](https://ui.aceternity.com/components/liquid-glass)；HTTP 200；标题：Liquid Glass | Aceternity UI
- 最终地址：https://ui.aceternity.com/components/liquid-glass

### Magic UI · 点阵旋转地球
- [直接打开](https://magicui.design/docs/components/globe) — 点阵地球旋转并显示位置标记，适合全球业务、社区或网络节点主视觉。
- [来源](https://magicui.design/docs/components/globe)；HTTP 200；标题：Globe | React Components & Templates
- 最终地址：https://magicui.design/docs/components/globe

### Magic UI · 逐条进入的通知列表
- [直接打开](https://magicui.design/docs/components/animated-list) — 通知条目依次进入并推动列表，参考实时活动、订单和消息流的节奏。
- [来源](https://magicui.design/docs/components/animated-list)；HTTP 200；标题：Animated List | React Components & Templates
- 最终地址：https://magicui.design/docs/components/animated-list

### Magic UI · 轨道环绕图标
- [直接打开](https://magicui.design/docs/components/orbiting-circles) — 多层图标沿圆形轨道环绕，可用于生态集成、连接关系和功能群。
- [来源](https://magicui.design/docs/components/orbiting-circles)；HTTP 200；标题：Orbiting Circles | React Components & Templates
- 最终地址：https://magicui.design/docs/components/orbiting-circles

### Magic UI · 放大式 Dock
- [直接打开](https://magicui.design/docs/components/dock) — 沿横向工具栏的图标随指针距离缩放，适合快捷操作区。
- [来源](https://magicui.design/docs/components/dock)；HTTP 200；标题：Dock | React Components & Templates
- 最终地址：https://magicui.design/docs/components/dock

### Magic UI · 鼠标聚光卡片
- [直接打开](https://magicui.design/docs/components/magic-card) — 卡片表面光晕跟随指针，适合低干扰的交互反馈与卡片群。
- [来源](https://magicui.design/docs/components/magic-card)；HTTP 200；标题：Magic Card | React Components & Templates
- 最终地址：https://magicui.design/docs/components/magic-card

### Magic UI · 数字滚动计数
- [直接打开](https://magicui.design/docs/components/number-ticker) — 数字以滚动方式更新，适合指标、统计摘要和里程碑展示。
- [来源](https://magicui.design/docs/components/number-ticker)；HTTP 200；标题：Number Ticker | React Components & Templates
- 最终地址：https://magicui.design/docs/components/number-ticker

### Magic UI · 流光边框
- [直接打开](https://magicui.design/docs/components/border-beam) — 亮色光束沿卡片边框移动，可用于突出选中项或关键内容。
- [来源](https://magicui.design/docs/components/border-beam)；HTTP 200；标题：Border Beam | React Components & Templates
- 最终地址：https://magicui.design/docs/components/border-beam

### Magic UI · 彩纸庆祝反馈
- [直接打开](https://magicui.design/docs/components/confetti) — 触发彩纸喷发的即时庆祝反馈，适合任务完成与里程碑。
- [来源](https://magicui.design/docs/components/confetti)；HTTP 200；标题：Confetti | React Components & Templates
- 最终地址：https://magicui.design/docs/components/confetti

### Dogstudio：艺术与技术工作室
- [直接打开](https://dogstudio.co/) — 工作室的完整品牌站与项目视觉组合，适合艺术导向的首屏和作品导航。
- [来源](https://dogstudio.co/)；HTTP 200；标题：Dogstudio. Multidisciplinary Creative Studio.
- 最终地址：https://dogstudio.co/

### KPR：科幻终端世界观
- [直接打开](https://kprverse.com/) — 终端命令、文件、阵营与世界观构成完整科幻界面，适合 HUD 和叙事网站参考。
- [来源](https://kprverse.com/)；HTTP 200；标题：KPR | Story
- 最终地址：https://kprverse.com/

### Craftz.dog：简洁的个人主页
- [直接打开](https://www.craftz.dog/) — 紧凑的个人资料、作品与 3D 场景入口结合，适合轻量而有个性的个人站。
- [来源](https://www.craftz.dog/)；HTTP 200；标题：Takuya Matsuyama - Homepage
- 最终地址：https://www.craftz.dog/

### Resn：创意数字体验
- [直接打开](https://resn.co.nz/) — 工作室的实验性全屏体验入口，适合观察非传统网站导航和场景化表达。
- [来源](https://resn.co.nz/)；HTTP 200；标题：Resn - Creative Digital Agency | Ideation, Design, and Development
- 最终地址：https://resn.co.nz/

### makemepulse：动态项目呈现
- [直接打开](https://www.makemepulse.com/) — 大画面项目与简洁的分区导航组合，适合创意工作室的整体界面参考。
- [来源](https://www.makemepulse.com/)；HTTP 200；标题：makemepulse — Global Creative Studio
- 最终地址：https://www.makemepulse.com/

### Long Hoang：互动 3D 作品集
- [直接打开](https://longhoang-lyo.com/) — 将产品设计与互动 3D 场景结合的个人作品集，含图形环境不支持时的文本入口。
- [来源](https://threejs-journey.com/selection/1)；HTTP 200；标题：Long Hoang (Lyo) – Designer & Developer
- 最终地址：https://longhoang-lyo.com/

### Jordan Breton：空间式作品集
- [直接打开](https://jordan-breton.com/) — 可触摸转动视角、点击进入探索的空间作品集，适合沉浸场景和内容入口设计。
- [来源](https://threejs-journey.com/selection/1)；HTTP 200；标题：Jordan Breton - Freelance Fullstack Software Engineer
- 最终地址：https://jordan-breton.com/

### Teahu：宇宙视听旅程
- [直接打开](https://www.teahu-experience.com/) — 分幕宇宙视听体验，配合暂停、重启和章节选择，适合场景叙事与播放器界面。
- [来源](https://threejs-journey.com/selection/1)；HTTP 200；标题：Teahu experience
- 最终地址：https://www.teahu-experience.com/

### Bilal：三维个人作品集
- [直接打开](https://bilal.show/) — 由 Three.js Journey 精选的独立三维作品集，适合沉浸式自我介绍的视觉参考。
- [来源](https://threejs-journey.com/selection/1)；HTTP 200；标题：Bilal El Moussaoui
- 最终地址：https://bilal.show/

### Soo-ah：可探索的房间作品集
- [直接打开](https://www.sooahs-room-folio.com/) — 用可旋转缩放的房间展示作品与个人内容，房间里的钢琴也可互动。
- [来源](https://threejs-journey.com/selection/1)；HTTP 200；标题：수아's Room Folio
- 最终地址：https://www.sooahs-room-folio.com/

### Merouane Bali：3D 作品集
- [直接打开](https://merodev.net/) — 由 Three.js Journey 精选的场景式作品集，适合空间探索与个人品牌表达。
- [来源](https://threejs-journey.com/selection/1)；HTTP 200；标题：Merouane Bali
- 最终地址：https://merodev.net/

### Keychron：3D 键盘配置体验
- [直接打开](https://keyboard.jingfu.design/) — 可改键帽配色与 RGB、逐层拆解并敲击发声的三维键盘；适合交互式产品展示。
- [来源](https://keyboard.jingfu.design/)；HTTP 200；标题：Keychron Q1 HE & K2 HE — Interactive 3D Keyboard Showcase
- 最终地址：https://keyboard.jingfu.design/

### 磁轴键盘开关：滚动拆解
- [直接打开](https://jingfu.design/work/keyboard-switch) — 滚动驱动磁轴开关组装和拆解，用材质与结构变化讲解实体产品。
- [来源](https://jingfu.design/work/keyboard-switch)；HTTP 200；标题：Magnetic Keyboard Switch in 3D | Jingfu Design
- 最终地址：https://jingfu.design/work/keyboard-switch

### CD 光谱衍射：可转动唱片
- [直接打开](https://jingfu.design/work/cd) — 拖拽转动光盘观察虹彩变化，可缩放、翻面与换封面，适合真实材质交互参考。
- [来源](https://jingfu.design/work/cd)；HTTP 200；标题：CD Rainbow Diffraction Shader | Jingfu Design
- 最终地址：https://jingfu.design/work/cd

### Patatap：声音与形状触发
- [直接打开](https://patatap.com/) — 按键或触摸触发几何动画和声音，适合即时反馈与有节奏的视觉互动。
- [来源](https://patatap.com/)；HTTP 200；标题：Patatap
- 最终地址：https://patatap.com/

### Typatone：会发声的文字界面
- [直接打开](https://typatone.com/) — 输入文字同时生成音乐，将键盘输入变为视听反馈，适合轻量创意工具。
- [来源](https://typatone.com/)；HTTP 200；标题：Typatone
- 最终地址：https://typatone.com/

### Oimo Bubbles：互动泡泡
- [直接打开](https://oimo.io/works/bubbles/) — 独立泡泡互动实验，适合透明球体、碰撞感和游玩式动态画面。
- [来源](https://oimo.io/works/bubbles/)；HTTP 200；标题：Bubbles
- 最终地址：https://oimo.io/works/bubbles/

### Fluid Particles：粒子流体
- [直接打开](https://david.li/fluid/) — 粒子呈现液体流动的独立演示，适合动态流场和密集粒子的视觉参考。
- [来源](https://david.li/fluid/)；HTTP 200；标题：Fluid Particles
- 最终地址：https://david.li/fluid/

### Resend：开发者产品官网
- [直接打开](https://resend.com/) — 产品功能、发送状态与界面示例形成统一的开发者官网，适合信息清晰的商业 UI。
- [来源](https://resend.com/)；HTTP 200；标题：Resend · Email for developers
- 最终地址：https://resend.com/

### Supabase：数据产品界面展示
- [直接打开](https://supabase.com/) — 表格编辑器、SQL 和权限界面切换展示，适合复杂后台产品的官网表达。
- [来源](https://supabase.com/)；HTTP 200；标题：Supabase | The Postgres Development Platform
- 最终地址：https://supabase.com/

### Framer：画布与网站编辑器展示
- [直接打开](https://www.framer.com/) — 围绕可编辑画布和真实网站组织产品演示，适合设计工具的复杂界面展示。
- [来源](https://www.framer.com/)；HTTP 200；标题：Framer: Free website builder and AI design agent
- 最终地址：https://www.framer.com/

### Cursor：多界面产品演示
- [直接打开](https://cursor.com/) — 官网内展示桌面和命令行界面、任务状态与审阅流程，适合软件产品的互动说明。
- [来源](https://cursor.com/)；HTTP 200；标题：AI Coding Agent for Building Ambitious Software | Cursor
- 最终地址：https://cursor.com/

## 未通过候选

- https://dennissnellenberg.com/ — 状态/页面内容未通过
- https://locomotive.ca/en — ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
- https://unseen.co/ — 状态/页面内容未通过

## 浏览器复核交接

所有 50 条均未经过浏览器视觉实测，`browser_verified=false`。为避免共享 IAB 干扰，按主代理指示停在 HTTP 与预览结构核验。

优先复核：Resn、Bilal、Merouane、Oimo Bubbles、Fluid Particles，以及需要 WebGPU 的三个 Jingfu 项目。其次复核 React Bits 12 页，页面 HTML 只有具体标题和官方路由，效果由客户端渲染。Aceternity 8 页和 Magic UI 8 页均在 HTTP HTML 找到公开 Preview 控件结构，仍不能据此保证客户端动画正常运行。

第二次 GET 中 Locomotive 从成功变为服务器主动断连，已保守移出本批；另外两项 Dennis Snellenberg 403 和 Unseen 软403 未收录。
