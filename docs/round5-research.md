# 第五轮 UI 与动效候选来源研究

研究日期：2026-11-03。所有条目只是候选，没有浏览器画面或播放通过结论。

新增 35 条，35 个主机；全部原站 GET 200 且读取到对应作品标题/内容。已与写入时全部 candidate*.json 和 library.json 按构建器 canonical_url 去重，亦比较重定向后 URL。

## 选品和证据边界

优先补充服装、餐饮饮料、相机、汽车/卫星/无人机、文化、音频工作台、游戏 HUD 与电影目录。未收教程、占位模板或通用灵感导航。获奖资料只是选品证据，不能替代实际浏览器核验。

FWA 的原站页面包含公开脚本 `/assets/main_patched.min.js`，脚本明确使用 `/api/cases/` 与 `/api/cases/{slug}`；据此读取官方公开项目数据，并从其中实际 `url` 字段取得作品入口。没有猜测作品路由。原始响应保存于 `.cache/newresearch/round5-fwa-*.json`。每条来源链接及核查动作见下。

部分网页 HTML 含显卡不支持/加载失败的后备文本，HTML 读取不能判断该后备是否真的在屏幕上显示，故不将其误报为坏站。KINORIA 和 Aevion 保留概念/技术演示身份；A24 明确为个人非商业实验。

## 分类分布

- 品牌与产品界面：13 条
- 音频可视化：4 条
- 游戏与交互体验：7 条
- 作品集与展示：7 条
- 数据可视化：1 条
- 画廊与导航：2 条
- 文字与排版：1 条

## 候选明细

### 1. PixelVault：3D 服装商店

- [作品直链](https://www.pixelvault.fit/) · [来源](https://thefwa.com/cases/pixelvault)
- 内容：服装品牌把夹克商品放进可旋转的三维展示与浏览器 AR 试穿流程。
- 待实际核查：查看商品切换、模型操控与购物界面；AR 入口需单独确认设备要求。
- 响应：HTTP 200；原站标题：PIXELVAULT | An Immersive Marketplace from 2047。

### 2. Nebulofi：星系音乐工作台

- [作品直链](https://nebulofi.vercel.app/) · [来源](https://thefwa.com/cases/nebulofi)
- 内容：以恒星与行星组织生成式氛围音乐；页面提供星系选择、行星与节奏控制。
- 待实际核查：选星进入场景，改变行星参数，确认画面和声音同步响应。
- 响应：HTTP 200；原站标题：Nebulofi。

### 3. The Aviator：飞行游戏 HUD

- [作品直链](http://aviator.yakudoo.games/) · [来源](https://thefwa.com/cases/the-aviator)
- 内容：浏览器飞行游戏，官方项目资料列出躲避与射击两种模式。
- 待实际核查：进入游戏并切换模式，检查分数、生命和游戏结束状态。
- 响应：HTTP 200；原站标题：Aviator。

### 4. Daiki Fujita：清醒与梦境作品集

- [作品直链](https://daikifujita.com/) · [来源](https://thefwa.com/cases/daiki-fujita-portfolio)
- 内容：设计师作品集以常规阅读和三维梦境两种呈现组织作品。
- 待实际核查：阅读作品并进入梦境模式，核查两种导航及返回入口。
- 响应：HTTP 200；原站标题：Daiki Fujita — Web & Interactive Designer。

### 5. Oh là là Ride：巴黎自行车竞速

- [作品直链](https://ohlalaride.com/) · [来源](https://thefwa.com/cases/oh-la-la-ride)
- 内容：以巴黎街景为背景的浏览器自行车竞速，官方说明含道具、加速和双人玩法。
- 待实际核查：检查开始界面、单人操控与 HUD；多人部分仅记录实际可验证范围。
- 响应：HTTP 200；原站标题：Oh là là Ride — jeu de vélo gratuit dans Paris, en ligne et sur mobile。

### 6. Junkyard King Arena：手绘招式界面

- [作品直链](https://junkyardking.io/) · [来源](https://thefwa.com/cases/junkyard-king-arena)
- 内容：街机格斗把绘制形状作为出招输入，页面包含连击、分数、怒气与技能状态。
- 待实际核查：完成一段操作教学，实际画出形状并观察技能和计分反馈。
- 响应：HTTP 200；原站标题：Junkyard King。

### 7. Griflan Labs：俯视作品世界

- [作品直链](https://labs.griflan.com/) · [来源](https://thefwa.com/cases/griflan-labs)
- 内容：工作室用可探索的俯视环境呈现品牌、数字体验和产品作品。
- 待实际核查：确认 WebGPU 主体加载，再打开作品；能力提示不等于实际加载失败。
- 响应：HTTP 200；原站标题：Griflan Labs。

### 8. The Lantern House：灯笼屋作品集

- [作品直链](https://www.dwaynekoh.com/) · [来源](https://thefwa.com/cases/the-lantern-house)
- 内容：Dwayne Koh 的作品集以灯笼建筑串联不同品牌项目与案例。
- 待实际核查：探索建筑并打开品牌作品，检查转场和返回操作。
- 响应：HTTP 200；原站标题：Dwayne Koh — The Lantern House。

### 9. EnduroSat：卫星服务叙事

- [作品直链](https://www.endurosat.com/space-service/) · [来源](https://thefwa.com/cases/endurosat-space-service)
- 内容：卫星服务页面围绕任务设计、载荷集成、发射与运行组织内容；官方获奖资料说明采用 WebGL。
- 待实际核查：滚动完整任务段落，尝试页面 Drag 提示对应的模型交互。
- 响应：HTTP 200；原站标题：Space Service – Satellite Mission Design, Launch & Operations。

### 10. Carter Ogunsola：印刷工坊作品集

- [作品直链](https://carterogunsola.com/) · [来源](https://thefwa.com/cases/carter-ogunsola-portfolio-2026)
- 内容：作者将作品集设计成印刷物：项目轮盘、悬挂证件和书信分别承担不同页面功能。
- 待实际核查：转动首页项目轮盘并打开项目；检查证件页，联系页只观察不发送。
- 响应：HTTP 200；原站标题：Carter Ogunsola :: Creative Developer & Brand Engineer。

### 11. Thomas Gertenbach：照片桌面作品集

- [作品直链](https://thomasgertenbach.com/) · [来源](https://thefwa.com/cases/thomas-gertenbach-portfolio)
- 内容：作品集以俯视石膏桌面与可拿起的照片组织项目，项目说明包含投影式影片呈现。
- 待实际核查：拿起照片、放入展示区域，观察投影与关闭操作；确认 WebGPU 条件。
- 响应：HTTP 200；原站标题：Thomas Gertenbach — Creative Developer。

### 12. FunTech Creativity：角色互动场景

- [作品直链](https://experience2026.funtech.inc/) · [来源](https://thefwa.com/cases/experience-funtech-creativity)
- 内容：FunTech 的年度展示用官方角色连接十个实时三维场景，并提供展示影片入口。
- 待实际核查：实际进入多个场景并执行对应操作，区分实时体验与影片模式。
- 响应：HTTP 200；原站标题：EXPERIENCE FUNTECH CREATIVITY。

### 13. INHERITED：乐队数字世界

- [作品直链](https://inherited.band/) · [来源](https://thefwa.com/cases/inherited)
- 内容：乐队官网将成员、唱片与乐队介绍整合到带互动表现的音乐品牌界面。
- 待实际核查：打开菜单、成员与唱片页面，确认实际转场与媒体呈现。
- 响应：HTTP 200；原站标题：INHERITED。

### 14. KINORIA：胶片相机概念界面

- [作品直链](https://kinoria.studio/) · [来源](https://thefwa.com/cases/kinoria)
- 内容：机械胶片相机的交互概念网站，官方描述包含选胶卷、取景、拍摄四张照片与冲洗归档。
- 待实际核查：选胶卷并完整拍摄一卷，查看冲洗和归档；这不是在售相机的官方产品保证。
- 响应：HTTP 200；原站标题：KINORIA。

### 15. Cyera AI Guardian：安全主题游戏界面

- [作品直链](https://secure-the-unknown.cyera.com/) · [来源](https://thefwa.com/cases/cyera-ai-guardian)
- 内容：安全产品微站以飞船与三个星球关卡呈现 Discover、Govern、Protect 三个主题。
- 待实际核查：进入关卡并完成至少一种小游戏，观察进度、导航和退出反馈。
- 响应：HTTP 200；原站标题：Cyera AI Guardian | Secure the Unknown。

### 16. Agrumea Farm：西西里农场食品界面

- [作品直链](https://www.agrumeafarm.it/en) · [来源](https://thefwa.com/cases/agrumea-farm)
- 内容：果酱与调味食品品牌网站结合产地故事、食品产品与三维呈现。
- 待实际核查：完整滚动并打开 Pantry/菜单，核查商品展示和转场。
- 响应：HTTP 200；原站标题：Agrumea Farm | Jams, pestos and flavours of Sicily。

### 17. No Mercy Michel：竞技场互动

- [作品直链](https://no.merci-michel.com/) · [来源](https://thefwa.com/cases/no-mercy-michel)
- 内容：Merci Michel 的独立竞技场体验，原站邀请访客进入战斗。
- 待实际核查：进入竞技场，操作角色并检查 HUD、失败和重新开始。
- 响应：HTTP 200；原站标题：No Mercy Michel。

### 18. Every Neuron：神经网络探索界面

- [作品直链](https://www.everyneuron.com/) · [来源](https://thefwa.com/cases/every-neuron)
- 内容：项目以果蝇神经系统连接图为数据对象，官方资料列出可实时浏览的细胞网络。
- 待实际核查：打开探索器、缩放和选择节点，核查标签、网络反馈与数据出处；不评价医学结论。
- 响应：HTTP 200；原站标题：Every neuron。

### 19. A24：三维唱片式电影目录概念

- [作品直链](https://a24.raviklaassens.com/) · [来源](https://thefwa.com/cases/a24)
- 内容：非商业实验作品以三维碟片形式重组 A24 电影目录；不是 A24 官方网站。
- 待实际核查：旋转或切换目录并打开电影详情，检查媒体展示和返回路径。
- 响应：HTTP 200；原站标题：A24 — Films。

### 20. Superlocal 2025：设计大会界面

- [作品直链](https://2025.superlocaldesign.com/) · [来源](https://thefwa.com/cases/superlocal)
- 内容：乌拉圭设计大会的年度页面，包含讲者阵容、活动时间表与视觉章节。
- 待实际核查：查看阵容、时间表与菜单；历史活动预约不作为必测功能。
- 响应：HTTP 200；原站标题：Superlocal。

### 21. Aevion：无人机点云产品演示

- [作品直链](https://drone.riotters.com/) · [来源](https://thefwa.com/cases/lidar-drone-scanning)
- 内容：Riotters 的无人机技术演示，将 LiDAR 扫描与硬件产品说明组织为三维页面。
- 待实际核查：滚动硬件章节，检查模型和点云切换；保留技术演示身份。
- 响应：HTTP 200；原站标题：Aevion — autonomous LiDAR inspection drone。

### 22. Squarespace Foundations：动态品牌系统

- [作品直链](https://brand.squarespace.com/) · [来源](https://thefwa.com/cases/squarespace-foundations)
- 内容：Squarespace 官方品牌系统网站设有 Logo、字体、色彩、摄影、Campaign 与 Motion 六章。
- 待实际核查：逐章切换并检查字体、颜色和动效实例；不是通用素材目录。
- 响应：HTTP 200；原站标题：Squarespace Foundations | Squarespace Foundations。

### 23. Order & Chaos：实验排版样本

- [作品直链](https://ordernchaos.aiziza.com/) · [来源](https://thefwa.com/cases/order-chaos)
- 内容：一组限定网格、字体与色彩的极简排版实验，页面提供三个具体样本。
- 待实际核查：依次打开三个样本，记录实际布局变化与操作。
- 响应：HTTP 200；原站标题：Order & Chaos。

### 24. Colonia Zacamil：公共艺术街区

- [作品直链](https://coloniazacamil.com/) · [来源](https://thefwa.com/cases/colonia-zacamil)
- 内容：公共艺术与社区共创项目，用独立作品条目展示街区中的艺术内容。
- 待实际核查：打开多件壁画作品，核查空间导航、图集与作品信息。
- 响应：HTTP 200；原站标题：Colonia Zacamil。

### 25. Overworld Audio：声音项目地图

- [作品直链](https://overworldaudio.com/) · [来源](https://thefwa.com/cases/overworld-audio)
- 内容：游戏声音工作室把作品组织成可拖动或滚动的地图，页面明确提示点击标记探索项目。
- 待实际核查：拖动地图并打开多个标记，检查媒体播放与声音开关。
- 响应：HTTP 200；原站标题：Overworld Audio。

### 26. Seunghyuk Kim：点线面连续作品空间

- [作品直链](https://seunghyuk.com/) · [来源](https://thefwa.com/cases/well-dots-lines-planes)
- 内容：平面设计师作品集将关键词、作品与退出过程组织为连续空间和点线面变化。
- 待实际核查：进入作品再退出，核查项目内容、粒子转场与返回导航。
- 响应：HTTP 200；原站标题：Seunghyuk Kim — Graphic Designer。

### 27. TILToooTILT：服装与重力互动

- [作品直链](https://tiltoootilt.tote.co.jp/) · [来源](https://thefwa.com/cases/tiltoootilt-everything-has-weight)
- 内容：时尚主题互动页面以物体重量、指针倾斜与声音组织视觉体验。
- 待实际核查：移动指针、倾斜场景并操作物件，确认成品视觉与声音反馈。
- 响应：HTTP 200；原站标题：TILToooTILT — Everything Has Weight。

### 28. Ceramic Beats：陶瓷音色序列器

- [作品直链](https://ceramic-beats.zui.ooo/) · [来源](https://thefwa.com/cases/ceramicbeats)
- 内容：将大都会艺术博物馆开放陶瓷藏品组织为节奏序列器；页面有速度、预设、重排与节拍保存。
- 待实际核查：点选格子并播放，修改速度与预设，检查音频和节拍高亮。
- 响应：HTTP 200；原站标题：Ceramic Beats — a sequencer of Met ceramics。

### 29. La Revoltosa：复古汽水滚动界面

- [作品直链](https://larevoltosa.es/) · [来源](https://thefwa.com/cases/la-revoltosa-p2)
- 内容：西班牙汽水品牌以三维产品、插画与滚动叙事重述品牌历史。
- 待实际核查：滚动品牌故事并切换饮料，检查产品模型、菜单和图文过渡。
- 响应：HTTP 200；原站标题：La Revoltosa | La burbuja Ibérica。

### 30. Spyker Cars：手工跑车数字体验

- [作品直链](https://spykercars.com/) · [来源](https://thefwa.com/cases/spyker-cars-p2)
- 内容：跑车品牌官网用产品呈现与一天驾驶生活的叙事组织车型与品牌故事。
- 待实际核查：滚动完整车型页面，尝试模型/场景入口；不提交预约或购买。
- 响应：HTTP 200；原站标题：Hand-Built Super Sports Cars Since 1880 | Spyker Cars。

### 31. Pegassi Ascension：电子音乐 EP 展示

- [作品直链](https://ascension.pegassi.be/) · [来源](https://thefwa.com/cases/ascension-pegassir)
- 内容：电子音乐人的四曲 EP 专属页面，以歌曲列表和音乐视觉表达组织发布内容。
- 待实际核查：逐一切换歌曲入口，确认实际站内声音、视觉变化及外链范围。
- 响应：HTTP 200；原站标题：Ascension — Pegassi。

### 32. Artem Shcherbakov：导演动态作品集

- [作品直链](https://artemartemartem.com/) · [来源](https://thefwa.com/cases/artem-shcherbakov-p3)
- 内容：CGI/VFX 导演作品集，官方获奖资料说明采用 WebGL 效果、动态字体与页面转场。
- 待实际核查：打开至少两个影片作品并返回，核查主体媒体和字体/图像转场。
- 响应：HTTP 200；原站标题：artem shcherbakov。

### 33. TBWA HAKUHODO：裂缝与动态网格

- [作品直链](https://www.tbwahakuhodo.co.jp/) · [来源](https://thefwa.com/cases/tbwahakuhodo-corporate-website-p2)
- 内容：广告公司官网通过裂缝、变形、变化的字体与显露网格表达其 Disruption 品牌理念。
- 待实际核查：滚动首页、展开菜单并打开作品，观察字体、网格和过渡。
- 响应：HTTP 200；原站标题：TBWA\HAKUHODO。

### 34. Khufu’s：金字塔餐厅数字体验

- [作品直链](https://khufus.com/) · [来源](https://monarqeg.com/case-studies/khufus/)
- 内容：餐厅官网以金字塔环境与餐饮影像建立氛围，并提供站内菜单与预约入口。
- 待实际核查：播放首页片段并浏览交互菜单；只观察预约界面，不提交预约。
- 响应：HTTP 200；原站标题：Khufu’s | Award-Winning Elevated Egyptian Dining At The Pyramids。

### 35. Neutra VDL：建筑文化编辑式界面

- [作品直链](https://neutra-vdl.org/) · [来源](https://neutra-vdl.org/)
- 内容：建筑博物馆官网以层级编号导航组织参观、项目、档案与建筑空间摄影。
- 待实际核查：展开层级导航，进入项目与档案，核查摄影浏览和页面过渡。
- 响应：HTTP 200；原站标题：Neutra VDL。

## 未纳入与边界

- [Cartier - Le Chœur des Pierres](https://www.cartier.com/en-fr/lechoeurdespierres)：本轮原站返回 403 或连接失败，暂留研究记录。
- [The Last Tango](https://www.thelasttango.com/)：本轮原站返回 403 或连接失败，暂留研究记录。
- [Santioni Spirits: The Notturno Experience](https://santionispirits.com/)：本轮原站返回 403 或连接失败，暂留研究记录。
- SBS The Boat：原站仍有互动图像小说元数据，但文本主体只剩页脚；这一轮未进一步确认核心资源，暂不添加。
- FWA 其他普通营销页、交互目录、未能明确落到作品本体的项目没有为了凑数添加。
- 本轮没有将官方获奖介绍或 HTTP 200 写成 pass；实际浏览器检查仍是入主库的必要步骤。
