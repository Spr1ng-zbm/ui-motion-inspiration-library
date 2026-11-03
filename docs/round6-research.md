# 第六轮 UI 与动效候选研究

2026-11-03。source-only：所有条目待实际浏览器核验，不是新增通过项。

共 28 条。3 条明确标为视频，3 条为 Codrops 独立纯演示入口，其他为独立互动作品/界面。已与生成时全部 candidate*.json + library.json 按 canonical_url 去重，检查最终重定向 URL。

## 来源与筛选

FWA 官方公开项目 API 的使用路径由其网页脚本明确给出，原始项目描述与直链保存在 `.cache/newresearch/round6-fwa-list.json`。读取原站标题、正文/元数据后，只保留文化档案、交互展馆、硬件展示、品牌小游戏与有明确界面概念的作品。未收泛目录、技术库或教程文章。

Codrops 文章只作作者证据；候选 url 全部指向文章实际 Demo 链接。3 个演示命令行 GET 403，但公开网页读取工具能读到具体主体/Replay/示例切换内容，访问限制已单独标注。不能据此判为好坏。

Gusto 与 OPERATOR 的直接 MP4 来自作者网页的真实媒体字段，HEAD 返回 200 和 video/mp4；没有下载视频，也没有播放，长度和是否足够展示核心界面仍需实际核查。D&G 视频读取 YouTube 公开元数据得到作者 AQuest、时长 123 秒与发布时间 2026-08-06，未播放。

Ruffle 档案必须进入体验后检查；活动品牌游戏即使入口仍 200，也可能已经结束，不能把标题存在算通过。Noho 是非商业重设计，OPERATOR 是原生空间 App 的录像。

## 分类

- 画廊与导航：7
- 游戏与交互体验：8
- 品牌与产品界面：6
- App 与硬件展示：3
- 文字与排版：3
- 图像与转场：1

## 逐条核查重点

### 1. 197 Historias Ilustradas：插画记忆档案

[作品](https://www.197historiasilustradas.com/) · [作者/官方来源](https://thefwa.com/cases/197-historias-ilustradas)

纪念档案以插画讲述 197 位失踪者的人生，原站提供网格、列表与画廊三种入口。

待核查：切换三种视图并打开一位人物，核查作品呈现与返回路径。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 2. i-move-u：动作与角色互动重制

[作品](https://i-move-u.alexandrajugovic.com/) · [作者/官方来源](https://thefwa.com/cases/reanimated-i-move-u)

Hi-ReS! 为 Mitsubishi 创作的历史互动项目重制页，提供角色选择、场景与重播入口。

待核查：选择角色与场景、重播完整体验，确认动画主体；这是档案重制而非新车产品页。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 3. Noho：家具电商界面重设计

[作品](https://noho.ink/) · [作者/官方来源](https://thefwa.com/cases/noho)

家具网站的非商业重设计概念，界面包含深浅主题与减少动画等显示选项。

待核查：检查商品呈现、主题与减弱动画开关；不提交订单。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。非商业个人重设计，非家具品牌官方商店。

### 4. 2Advanced Prophecy V4：科幻界面档案

[作品](https://v4prophecy.2advanced.com/) · [作者/官方来源](https://thefwa.com/cases/2advanced-studios-prophecy)

2004 年 Prophecy V4 网站由原工作室恢复，通过 Ruffle 在现代浏览器中运行。

待核查：点击 Enter Archive，加载后操作主导航并观察转场；确认不是只有档案说明页。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 5. Shaky Picks：环形卡牌选择

[作品](https://myshaky.com/picks) · [作者/官方来源](https://thefwa.com/cases/shaky-picks)

独立卡牌互动以环形选择、分类与抽取结果组成完整状态流程。

待核查：切换分类、拖动卡环并抽取卡牌，检查过渡和结果层。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 6. /zeroz：食品品牌三维章节

[作品](https://otsuka-air.jp/) · [作者/官方来源](https://thefwa.com/cases/zeroz-brand-site-p2)

大塚制药食品品牌站用三维视觉与分章结构呈现品牌、产品和相关内容。

待核查：滚动并切换章节，核查模型与内容过渡；不将品牌功效文案当作医学结论。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 7. Pedro Belleza：跨年代界面时光机

[作品](https://www.pedrobelleza.com/) · [作者/官方来源](https://thefwa.com/cases/pedro-bellezas-personal-website)

作者把作品集设计成从 1986 年 BBS 到 2046 年的界面风格旅行。

待核查：切换年代，比较导航、排版和交互方式，并确认可以返回。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 8. moshi-moshi：几何世界交互档案

[作品](https://moshi-moshi.alexandrajugovic.com/) · [作者/官方来源](https://thefwa.com/cases/reanimated-moshi-moshi)

Hi-ReS! 为 NTT Data 创作的历史项目重制页，以海洋、山脉与城市等几何场景组织体验。

待核查：选择场景、切换声音并重播，观察日夜与几何变化。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 9. evian Gallery of Youth：五室虚拟展馆

[作品](https://celebrating200.evian.com/) · [作者/官方来源](https://thefwa.com/cases/evian-gallery-of-youth)

依云 200 周年虚拟展馆通过五个房间组织品牌历史与阿尔卑斯山来源故事。

待核查：进入展馆并浏览多个房间，检查导航、展品展开和返回操作。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 10. Weekend Max Mara：Pasticcino 工艺互动

[作品](https://weekend-mm-2026-pasticcino-bag-master.monogrid.io/en/) · [作者/官方来源](https://thefwa.com/cases/weekend-max-mara-pasticcino-bag-world-tour-italian-roots)

MONOGRID 为品牌制作的包袋工艺体验，让访客通过互动了解 Pasticcino Bag 的制作。

待核查：等待脚本主体加载，完成至少一个工艺操作并检查进度与场景切换。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。HTML 是依赖 JavaScript 的入口壳，独立作品身份由 MONOGRID 的 FWA 项目资料确认；必须核查主资源是否仍正常。

### 11. OPERATOR：空间音乐 App 演示片段

[作品](https://cdn.prod.website-files.com/67e524877e11e4cccb01d63c%2F6904831ec2806809f29dc169_Operator_01-transcode.mp4) · [作者/官方来源](https://www.fun-and-awe.io/operator)

作者发布的空间音乐 App 片段；项目将模块排列、虚拟雕塑与音乐创作相结合。

待核查：播放并拖动进度，确认片段可见音乐模块和空间界面；不能称浏览器内可操作 App。
响应：HEAD 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。 此条是录像/片段，不能作为在线可操作组件。直接片段由作者 OPERATOR 项目页的 video source 提供；完整项目另有 Vimeo 展示入口。

### 12. Mosby’s Files：拟物档案夹导航

[作品](https://www.mosbyfiles.com/) · [作者/官方来源](https://thefwa.com/cases/mosbys-files)

建筑历史档案以 CSS 拟物文件夹承担导航，把分类和阅读组织成桌面档案体验。

待核查：打开文件夹和建筑师条目，检查层级、展开/收起与返回路径。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 13. Miu Miu：包袋探索之家

[作品](https://immersivebags.miumiu.com/) · [作者/官方来源](https://thefwa.com/cases/miumiu-a-house-that-we-shaped)

Miu Miu 官方包袋展示以可探索的房屋与物品交互引出新系列。

待核查：进入房屋，操作多个对象并打开包袋内容，检查声音和导航。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 14. FS 60P：实时腕表与页面互动

[作品](https://thewatch.60fps.fr/) · [作者/官方来源](https://thefwa.com/cases/the-watch)

60fps 工作室的腕表展示实验将实时 WebGL 表体与周围页面内容结合。

待核查：等待表体加载，滚动和尝试指针操作，确认模型如何与内容衔接。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 15. MechStorm：机甲射击游戏 HUD

[作品](https://www.mechstorm.io/) · [作者/官方来源](https://thefwa.com/cases/mechstorm-p2)

浏览器机甲射击游戏含操作说明、成绩、成就与游戏内 HUD；原站明确限定桌面设备。

待核查：用桌面进入游戏，核查操控、生命/计分与结束状态；不用移动端失败替代判断。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 16. Le Mans Classic：幕后摄影叙事

[作品](https://lemansclassic.richardmille.com/) · [作者/官方来源](https://thefwa.com/cases/le-mans-classic)

Richard Mille 的摄影项目以勒芒经典赛幕后工作人员与场景形成沉浸式摄影叙事。

待核查：完整浏览摄影章节，检查图像切换、文字和项目说明入口。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 17. Hearst：ELLE × Esquire 好莱坞摄影展

[作品](https://www.hollywoodexhibit2026.com/) · [作者/官方来源](https://thefwa.com/cases/elle-and-esquire-exhibit-2026)

Hearst 的联合摄影展数字页面，呈现 ELLE 与 Esquire 的好莱坞档案影像。

待核查：进入展览并切换摄影内容，核查作品信息和导航。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 18. FunTech：幻灯片式动态品牌系统

[作品](https://ci.funtech.inc/ja) · [作者/官方来源](https://thefwa.com/cases/funtech-brand-identity)

FunTech 十周年品牌更新页面以幻灯片形式呈现标志、理念与视觉动画。

待核查：逐张切换品牌章节，检查 Logo、排版和过渡的具体变化。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 19. Radian：电动越野车配置界面

[作品](https://www.rideradian.com/) · [作者/官方来源](https://thefwa.com/cases/radian)

电动越野摩托车产品页结合滚动章节、硬件信息和自定义配置入口。

待核查：滚动硬件章节并打开配置器，改变选项；不提交预订或付款。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 20. Lacoste Ace Breaker：品牌打砖块

[作品](https://members-play.lacoste.com/ace-breaker-rg/) · [作者/官方来源](https://thefwa.com/cases/lacoste-ace-breaker)

Lacoste 官方网球主题打砖块作品，原页面仍提供游戏标题与玩法说明。

待核查：检查活动结束后游戏能否独立游玩，验证操控、分数和重开；不提交抽奖资料。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 21. Lacoste Polo Factory：服装工厂互动

[作品](https://members-play.lacoste.com/polo-factory-experience/) · [作者/官方来源](https://thefwa.com/cases/lacoste-polo-factory)

Lacoste 官方互动工厂体验，用独立场景介绍 Polo 产品的诞生。

待核查：进入工厂并完成一个步骤，检查关卡提示、物品操作与进度反馈。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 22. Shaky Gotcha：3D 街机与收藏界面

[作品](https://myshaky.com/gotcha) · [作者/官方来源](https://thefwa.com/cases/shaky-gotcha)

独立街机作品含限时击打、连击、角色收藏与音乐控制，与 Shaky Picks 的抽牌流程不同。

待核查：开始一局并观察连击和结算，再查看收藏与音乐面板。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 23. Ten Years Away：工作室互动漫画

[作品](https://ten.375.studio/en) · [作者/官方来源](https://thefwa.com/cases/ten-years-away-p6)

Studio375 用互动漫画讲述自身十年经历，提供章节年份与声音体验。

待核查：开始漫画，推进多个章节并尝试年份导航，检查过渡与声音状态。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。

### 24. Dolce&Gabbana Velvet：香氛互动装置展示

[作品](https://www.youtube.com/watch?v=qxRuT8kRDvg) · [作者/官方来源](https://thefwa.com/cases/dg-velvet-collection)

AQuest 官方发布的香氛交互装置展示，以音乐与香气记忆组织个性化探索流程。

待核查：播放多个时间段，确认界面、输入方式与状态反馈；不是网页内可操作版本。
响应：GET 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。 此条是录像/片段，不能作为在线可操作组件。

### 25. Gusto：产品 UI 动效展示短片

[作品](https://ziwvaiplle7bdzaz.public.blob.vercel-storage.com/videos/h264/outpost-gusto-reel-v1-fallback.mp4) · [作者/官方来源](https://www.krystofjezek.com/work/outpost-gusto)

作者为 Outpost Studio 的 Gusto UI 制作的展示短片，将界面模块动画与桌面、笔电、手机场景衔接。

待核查：播放开头、中段与末段，观察界面模块、光标与转场；确认视频真实内容后再写观察结论。
响应：HEAD 200。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。 此条是录像/片段，不能作为在线可操作组件。视频 URL 来自作者页面公开媒体数据；未下载或代替实际播放。

### 26. Unwoven：图像丝带编织轮播

[作品](https://tympanus.net/Development/Unwoven/) · [作者/官方来源](https://tympanus.net/codrops/2026/09/05/building-an-infinite-loom-unravelling-images-into-threads-with-three-js/)

连续图像带被拆成多条丝带，在视口边缘编织与散开，中央重新组成完整照片。

待核查：等待自动运动，观察图像边缘条带与中间完整照片；检查连续循环。
响应：GET 403。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。 命令行 GET 触发连接验证；公开页面读取工具可读到演示标题和主体内容，仍需浏览器确认。

### 27. On-Scroll SVG Filter Text：滚动文字变形

[作品](https://tympanus.net/Development/OnScrollSVGFilterText/) · [作者/官方来源](https://tympanus.net/codrops/2024/08/22/scroll-based-svg-filter-animations-on-text/)

文字标题在滚动中使用不同 SVG 滤镜变化，每段提供独立 Replay 按钮。

待核查：滚动触发多个标题，再点击 Replay，确认具体变形而非只有静态字体。
响应：GET 403。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。 命令行 GET 触发连接验证；公开页面读取工具可读到演示标题和主体内容，仍需浏览器确认。

### 28. Gooey Text Hover：黏液文字菜单

[作品](https://tympanus.net/Development/GooeyTextHover/) · [作者/官方来源](https://tympanus.net/codrops/2020/04/28/morphing-gooey-text-hover-effect/)

菜单文字通过 SVG 滤镜在悬停时变形；作者提供三个不同的示例。

待核查：悬停不同菜单项，并切换 01/02/03 示例，检查变形与恢复。
响应：GET 403。来源研究候选；尚未浏览器查看主体、执行交互或播放，不计实测通过。 命令行 GET 触发连接验证；公开页面读取工具可读到演示标题和主体内容，仍需浏览器确认。

## 暂不收录

- [Orion Immersive Experience](https://vimeo.com/1192374692/81e5b2edba)：Vimeo 返回人机验证页；为便于直达，本轮暂不纳入。
- [ARGOS](https://vimeo.com/1219285189)：Vimeo 返回人机验证页；为便于直达，本轮暂不纳入。
- Wide：作者 Demo 链接重定向到 CodePen 编辑器/升级引导，暂不作为容易直达的独立演示。
- Repeating Image Transition：本轮未稳定取得实际 Demo 入口，未猜路由。

## 完成检查

- JSON 可解析，URL 批内唯一；全部 browser_verified=false、review_status=candidate。
- 没有改主数据、UI、构建脚本或审核通过记录。
