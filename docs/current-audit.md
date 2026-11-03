# 当前版本逐项核验

更新：2026-11-03。主库 **300 条**；旧库 173 条全部尝试核查，保留 **158 条**，移出 **15 条**；新增 **142 条**。

主库每条均有实际画面依据和具体操作记录。静态界面可以作为 UI 参考；只有看到变化才描述为已验证动效。视频核验关键片段，不代表完整播放。

## 入库标准

保留具体 UI、交互演示、创意网站或高完成度展示视频。排除教程、泛导航、主体占位过多、低完成度小样及本轮无法确认核心画面的条目。链接修复后保留原收藏 ID。

“暂无法核验”仅描述本轮环境，不等于原站永久失效。候选文件与历史审计不属于推荐主库；当前推荐以 library.json / 在线浏览页为准。

## 分类

- 粒子与背景：18 条
- 完整界面：87 条
- 画廊与导航：28 条
- 微交互：60 条
- 游戏与趣味：9 条
- 图形与图标：9 条
- 3D与沉浸：45 条
- 滚动与叙事：14 条
- 文字与排版：10 条
- 组件与合集：2 条
- 应用界面展示：6 条
- 界面动效短片：5 条
- 作品集短片：2 条
- 游戏UI与HUD：2 条
- 声音与可视化：3 条

## 原有 173 条的逐项结果

| 条目 | 当前处理 | 本轮依据 / 移出原因 |
|---|---|---|
| [Discography：唱片式专辑浏览](https://dmtrbrl.github.io/discography) | 保留 | 唱片封面和3D盒体完整显示；由 Yeah Yeah Yeahs / Its Blitz 切换到 IAMX / The Alternative，中央封面与左右排列同步变化。 |
| [PRO Threads：光丝字形生成器](https://www.kubai.design/pro-threads) | 保留 | 光丝字形从PRO实时变成UI，形状与布局对应输入变化；材质与调参面板完整可见。 |
| [Linear：产品工作流与官网展示](https://linear.app) | 保留 | 任务详情/评论界面切换成指标卡、堆叠柱状图和项目表格；页面内演示可交互，未登录。 |
| [WebGL Fluid Simulation](https://paveldogreat.github.io/WebGL-Fluid-Simulation) | 保留 | 初始彩色旋涡随时间消散；拖动轨迹生成新的紫红色流体烟雾与涡卷。 |
| [Glass：液态玻璃图标](https://phileeppov.com/glass) | 保留 | 玻璃笑脸图标主体完整；预设切换后背景变黑、标志反白，彩色折射纹与材质参数对应变化。 |
| [LeafThrough：纸张翻阅](https://dmtrbrl.github.io/leafthrough) | 保留 | 封面先弯曲翻起，随后完整展开为第2–3页；页码和图文内容同步变化。 |
| [Atelier North：建筑工作室界面](https://atelier-north.crnacura.workers.dev) | 保留 | 奶油底与钴蓝大字首屏完整；导航定位到项目区，标题从重复错位收敛为Selected Works，建筑图像由像素块逐步清晰。 |
| [Amber Genetics：恐龙标本转盘](https://amber.isma.uy) | 保留 | 五只恐龙和实验转盘完整呈现；中心三角龙切换为霸王龙，转台排列与Rex.005/Predator档案标题同步更新。 |
| [Isle Thorne：家居电商展示](https://isle-thorne-collective.crnacura.workers.dev) | 保留 | 家居摄影与克制导航完整呈现；点击后出现空购物车浮层、Visit the shop入口及关闭控制，背景内容尺寸/布局响应。 |
| [Motion：App Store 卡片展开](https://examples.motion.dev/react/app-store) | 保留 | 山景卡片放大为中央详细面板，底部正文显现，背景变暗；不是跳到教程。 |
| [Fluid Pixel Cursor：像素流体光标](https://nestorrig.github.io/Fluid-Pixel-Cursor-Effect) | 保留 | 黑色点阵背景和像素标题正常；拖动后出现蓝紫像素拖尾，随后衰减。 |
| [Reel Flux：立体照片卷轴](https://saurow-reel.vercel.app) | 保留 | 完整照片带出现；滚轮后蛇/蒲公英画面移为蒲公英/天鹅，卡片边缘呈弯曲透视。 |
| [Apple Health：健康引导拼合](https://60fps.design/shots/apple-health-longevity-intro-animation) | 保留 | 彩色不规则健康图块收拢变为大小不同的圆形分类气泡，底部健康引导内容稳定。 currentTime 0.07→4.50秒，时长8.88秒，最终paused=false、readyState=4。 |
| [Liquid Lens：液态透镜](https://angelolibero.github.io/liquid-lens) | 保留 | 熔岩图片在不规则融合轮廓中呈现，前后画面轮廓及图像扭曲明显变化。 |
| [Runmo：里程圆环与统计切换](https://60fps.design/shots/runmo-distance-wheel-fill-interaction) | 保留 | 黑黄运动UI年度切换时，31KM局部圆环推进为59KM满圆，数字、刻度、统计卡同步变化。 currentTime 0.09→4.28秒，时长8.80秒，最终paused=false、readyState=4。 |
| [Airbnb：触感标签按钮](https://60fps.design/shots/airbnb-tactile-tab-button-interaction) | 保留 | currentTime 1.29→5.18秒，时长6.5秒，paused=false、readyState=4。Homes/Services标签切换时选中胶囊凹陷，未选中按钮凸起，内容列表同步换页。 |
| [3D Carousel：弯曲照片轮播](https://3d-carousel.thibaut-lefrancois.com) | 保留 | 初始雾中人物卡片显示悬停色散；滚动后切为湖畔房屋和人物卡片，透视弯曲轮廓随位置变化。 |
| [Earth：全球风场与海洋](https://earth.nullschool.net) | 保留 | 实际地球风场流线可见；温度选项选中且URL更新overlay=temp，蓝绿风速底色转黄红温度层；拖动后大陆经纬度视角改变。 |
| [Ripple：图像水纹悬停](https://ripple-effect-webgl.vercel.app) | 暂无法核验，移出 | 三张花朵图和页面正常，但多次指针移动后的截图未能明确辨认水波折射，不能声称核心特效通过。错误日志为空。 |
| [Pixel Scroll：图片像素揭示](https://pixelimageeffect.pages.dev) | 保留 | 北方探险编辑式图文首页完整；滚入下一组照片先出现黑白大像素块，随后还原为营地和山谷的清晰图片。 |
| [Vanta.js](https://www.vantajs.com) | 保留 | 彩色鸟群背景成功切换为低多边形起伏水面，URL切换effect=waves、对应参数面板更新。 |
| [Atropos](https://atroposjs.com) | 暂无法核验，移出 | 森林主体正常显示，但两次操作未见倾斜/视差，rotate和scale仍为单位矩阵。 |
| [Raycast：键盘与命令面板展示](https://www.raycast.com) | 保留 | 黑色磨砂导航与大标题，下方桌面框架中的命令/剪贴板历史面板；色值列表、预览区、信息分栏和键盘提示清晰。 |
| [Sonner](https://sonner.emilkowal.ski) | 保留 | 右下角出现三层通知卡片，前卡显示标题与说明，后两卡缩放层叠。 |
| [Vaul](https://vaul.emilkowal.ski) | 保留 | 白色抽屉滑出、后方页面缩小并变暗；下拉后抽屉关闭且页面恢复。 |
| [Motion：Coverflow 画廊](https://examples.motion.dev/react/gallery-coverflow) | 保留 | 中心红色冰棒切换到白红色冰棒，两侧图片保持透视倾斜并重新排列。 |
| [Kokonut：滑动确认](https://kokonutui.com/docs/buttons/slide-to-confirm) | 保留 | 滑块到右侧，暗色按钮变白并出现Paying及旋转指示，随后演示自动重置。 |
| [Kokonut：刻度旋钮](https://kokonutui.com/docs/inputs/detent-dial) | 保留 | Temperature由21变21.5再变27.5，内指针和外圈高亮刻度同步旋转。 |
| [Kokonut：液体仪表](https://kokonutui.com/docs/cards/liquid-gauge) | 保留 | Storage由72%变71%再到33%，白色填充高度下降，已用42.2GB和空余67%同步更新。 |
| [React Bits：Aurora 极光](https://reactbits.dev/assets/video/aurora.mp4) | 保留 | 首帧均匀垂落的绿蓝极光，在中段变成中央下沉、两侧抬高的流动光带。 |
| [Magic UI：Animated Beam](https://cdn.magicui.design/animated-beam.mp4) | 保留 | 官方录像由0.435秒播放到7.194秒，图标连线主体清楚，结束帧可见下方两条路径的紫色光束；改用录像作为主入口。 |
| [Aceternity：Container Scroll](https://ui.aceternity.com/live-preview/container-scroll-animation-demo) | 保留 | 原本向后倾斜的界面容器逐渐展开为更正面的矩形，内部Linear风格界面清楚可见。 |
| [Revolut：卡片就绪动画](https://60fps.design/shots/revolut-card-ready-animation) | 保留 | 紫红金属卡片特写缩小旋转，黑色叠片螺旋环绕，出现账户已就绪文案。 currentTime 0.60→4.85秒，时长9.18秒，最终paused=false、readyState=4。 |
| [Circle：头像气泡开场](https://60fps.design/shots/circle-splash-bubbles-pop-interaction) | 保留 | 社交头像气泡由稀疏分布变为成组排布，伴随小聊天标签和底部入门文案。 currentTime 0.13→14.45秒，时长20.17秒，最终paused=false、readyState=4。 |
| [Brick：翻转价值主张文字](https://60fps.design/shots/brick-intro-value-prop-text-flip-interaction) | 保留 | 实拍背景上的价值主张动词由playing翻换为connecting，按钮及固定文字保持稳定。 currentTime 0→4.96秒，时长8.20秒，最终paused=false、readyState=4。 |
| [Plasma：卡片展开为底部抽屉](https://60fps.design/shots/plasma-duo-style-bottom-sheet-open-interaction) | 保留 | 优惠卡片放大成圆角底部面板，再缩回；背景遮罩、模糊和边线清晰。 currentTime 3.50→5.49秒；时长12.97秒；最终paused=false、readyState=4。 |
| [Duolingo：雕塑奖励揭晓](https://60fps.design/shots/duolingo-sparkle-sculpt-pop-interaction) | 保留 | 未成形的石块在烟团、星光中揭示猫头鹰雕像，下面仍为任务进度条。 currentTime 0.03→1.60秒；时长4.00秒；最终paused=false、readyState=4。 |
| [CRED：票券滑杆](https://60fps.design/shots/cred-ticket-pop-on-slider-interaction) | 保留 | 黄色滑杆移动时小金票由滑块处飞起，票数由165变211，底部金额同步更新。 currentTime 0→1.17秒；时长3.45秒；最终paused=false、readyState=4。 |
| [Revolut：积分功能开通引导](https://60fps.design/shots/revolut-revpoints-feature-coachmark-border-pulse-interaction) | 保留 | 紫色发光RevPoints开通页转入积分首页，并显示赚取积分的新手提示。 currentTime 0.06→3.90秒；时长11.83秒；最终paused=false、readyState=4。 |
| [Run Receipt：手写签名收据](https://60fps.design/shots/run-receipt-signature-interaction) | 保留 | 拟物跑步收据上黑色手写签名逐步绘出，纸面、虚线分隔和数据保持稳定。 currentTime 0→3.22秒；时长5.13秒；最终paused=false、readyState=4。 |
| [X：活动点赞角色动画](https://60fps.design/shots/x-campaign-hashtag-based-grok-bot-like-button-interaction) | 保留 | 录像内X点赞位置的彩色角色团散开、收回为粉色爱心，未操作真实社交账户。 currentTime 1.26→5.35秒；时长5.37秒；最终paused=false、readyState=4。 |
| [Platen：拟物打字机引导](https://60fps.design/shots/platen-typewriter-intro-how-to-interaction) | 保留 | 暗色拟物打字机纸面上，灯具沿滑轨移动，聚光照亮文字并跟随位置变化。 currentTime 0→3.21→4.20秒；时长8.29秒；最终paused=false、readyState=4。 |
| [Airbnb：新功能开场叙事](https://60fps.design/shots/airbnb-new-intro-sequence) | 保留 | 朦胧的App缩略界面逐步清晰、上移成实体页面，房源卡片、分类图标、搜索栏与引导标题依次出现。 currentTime 0.20→5.12秒；时长8.03秒；最终paused=false、readyState=4。 |
| [Flighty：转机助手抽屉](https://60fps.design/shots/flighty-connection-assistant-sheet) | 保留 | 复核currentTime 0→1.45→0.81（循环），duration4.77秒，paused=false、readyState=4。换乘助手面板内有绿黄红风险时间轴，随后手写圈注与解释标记出现。 |
| [Flighty：护照黑光分享](https://60fps.design/shots/flighty-share-passport-blacklight-interaction) | 保留 | currentTime 0→1.89秒，duration2.32秒，paused=false、readyState=4。紫色黑光环境中的荧光世界地图护照切回浅色纸张与普通地图色，底部Blacklight按钮随状态变化。 |
| [Airbnb：叠放照片入场](https://60fps.design/shots/airbnb-photo-pop-and-slide-animation) | 保留 | 1.02秒微动画，currentTime 0→0.55，播放时paused=false、readyState=4；起始照片空白，随后三张叠放圆角照片出现于预约标题上方。后续循环重置到0并暂停。 |
| [拿了个国际小奖，我的个人网站演示](https://www.bilibili.com/video/BV1hYceeGEuq) | 保留 | 黑绿个人站的肖像扫描线与X光轮廓变换清晰可见，随后进入技能栏目。currentTime 78.67→84.04，paused=false、readyState=4。 |
| [Bruno Simon：可驾驶的 3D 作品集](https://bruno-simon.com) | 保留 | 完整卡通3D庭院、小车、灯光、树木与立体名字出现；按键后车与镜头移动，字母被碰撞散开并出现爆炸反馈。菜单内有地图/驾驶说明与个人介绍。 |
| [神兽管理局：中国神话交互网页](https://www.bilibili.com/video/BV1Ka4y1o7aS) | 保留 | 紫色神话网页中，档案卡片由箱子飞出；转为中式建筑与侧栏导航场景。currentTime 8.50→21.92→32.67秒，paused=false、readyState=4。 |
| [Lusion：3D 视觉叙事工作室](https://lusion.co) | 保留 | 蓝黑白高光3D管状构件持续改变朝向；首屏随滚动退出并揭示大字叙事，Menu展开右侧项目导航卡片。 |
| [UI 动效作品集：消消美食街](https://www.bilibili.com/video/BV1zSfPYwEev) | 保留 | 消除游戏中剪刀道具出现，随后为角色庆祝及救援成功横幅，旁边有动效设计思路排版。视频由0秒进入8.18秒，readyState=4；快进28.82秒截图显示成功反馈。 |
| [Anime.js：机械表盘与结构拆解](https://animejs.com) | 保留 | 环形机械表盘内线条和点阵发生变化；滚动后进入镜头结构拆解的三维爆炸图。 |
| [React Bits · 逐字分裂入场](https://reactbits.dev/assets/video/splittext.mp4) | 保留 | 早段只有半透明下移的He字符，随后完整Hello, you!进入并对齐。 |
| [Lenis：星空手部滚动叙事](https://lenis.dev) | 保留 | 黑粉配色的星空与手部三维背景出现，滚动后标题遮罩揭示、正文与背景构图联动。 |
| [React Bits · 文字从模糊中浮现](https://reactbits.dev/assets/video/blurtext.mp4) | 保留 | 约1秒处Isn't this呈现明显模糊且后半句尚未出现，完成帧整句清晰。 |
| [CPDD：搞怪个人介绍网页演示](https://www.bilibili.com/video/BV1Ne41177jP) | 保留 | 粉色爱心入口转为人物卡片、手写大字、黑色心形装饰及底部图标导航。currentTime 8.65→41.10→66.41→75.98，最终readyState=4、paused=false。 |
| [Gelatin Water：实时水体](https://gelatin.games/ultrawater) | 保留 | 海面波纹、岸边焦散与透明水体正常渲染；选择后切到水下视角，可见鱼群、海底与水面折射。 |
| [React Bits · 金属扫光文字](https://reactbits.dev/assets/video/shinytext.mp4) | 保留 | 灰色Shiny Text Effect在后段Effect位置出现明确白色亮带，其他字符仍灰色。 |
| [Stripe：支付产品的界面展示](https://stripe.com) | 保留 | 自动到zh-hk本地化页面；首屏彩色渐变，大型四列产品导航；下方实见终端付款、结账表单、Token用量柱状图和多产品卡片。 |
| [Ocarina：陶笛音乐交互](https://ocarina.thibaut-lefrancois.com) | 保留 | 二次访问成功进入复古像素风木屋和三维陶笛；按键后音符控件高亮，飞行精灵位置改变；Songs打开完整曲目/五线谱面板。 |
| [React Bits · 滚动悬浮字形](https://reactbits.dev/assets/video/scrollfloat.mp4) | 保留 | React Bits整句与中段从底部以错位/拉伸方式浮起的React字形均清晰可见。 |
| [2026 届游戏 UI 动效作品集](https://www.bilibili.com/video/BV1JybpzXESe) | 保留 | 城市赛事入口转为环形匹配玩家列表界面，透视场景与HUD菜单清晰。两次readyState=4、paused=false，currentTime持续增长。 |
| [Asteroid Field：小行星群穿行](https://instanced-mesh-showcase.vercel.app) | 保留 | 飞船穿过大量小行星，前后截图陨石位置变化；短按后可见爆破碎片，Destroyed由1增长至5。 |
| [React Bits · 弧面拖拽画廊](https://reactbits.dev/components/circular-gallery) | 保留 | 中央照片从Pier码头切到Clouds云层，两侧图片与弧形排列随拖动改变，图片主体正常加载。 |
| [curtains.js：全屏照片切换](https://curtainsjs.com/examples/multiple-textures/index.html) | 保留 | 演示全屏正常显示舞台灯光照片；点击后成功切换至多块灯光装置照片。 |
| [UI 动效：项目作品与 3D/2D 交互合集](https://www.bilibili.com/video/BV1vHUaBMEyr) | 质量移除 | 练习型航海UI小样，视觉完成度较低，本轮不保留在高质量主库。 |
| [Screen Studio：录屏产品演示](https://screen.studio) | 保留 | 实见深色录屏编辑器、时间轴、背景选择侧栏与嵌入表格画面；视频0.82→1.57秒，paused=false、readyState4，镜头放大表格并出现运动模糊。 |
| [React Bits · 可甩动的卡片堆](https://reactbits.dev/components/stack) | 保留 | 白房子照片置底，顶部换为树林木屋，AX显示Card 2，堆叠倾角及后方卡片随之变化。 |
| [React Three Rapier：三维落球板](https://react-three-rapier.pmnd.rs) | 保留 | 紫色竖直碰撞板及底部形状堆积显示；点击后新紫色球体从板顶落下，原物体落至底部。 |
| [APP 展示视频与动效练习：健康检测概念](https://www.bilibili.com/video/BV1Q54y1q7oi?p=2) | 保留 | 第二分集呈现手机引导页、设备搜索波纹、健康首页卡片与底部导航；0→11.39→17.90秒，paused=false、readyState=4，画面从搜索中切到首页。 |
| [Family：钱包 App 展示](https://family.co) | 保留 | 首屏彩色图形围绕大标题；功能卡中Backing Up变Back Up Now、交易状态时间轴重置、速度值及头像列变化。 |
| [React Bits · 球面无限菜单](https://reactbits.dev/components/infinite-menu) | 保留 | 拖动期间完整球面照片网格出现，释放后选中项由The Pier变为Rapeseed，标题和说明同步变化。 |
| [useAnimations](https://useanimations.com) | 保留 | 图标从带弧线的过渡状态切回三条菜单横线，点击响应及直接图标预览正常。 |
| [星际公民：飞船内部 FUI 与 HUD 界面](https://www.bilibili.com/video/BV1op4y1w7U5) | 质量移除 | 26分钟实机游玩，UI只占局部；用短而集中的界面展示替换。 |
| [Apple Vision Pro：空间界面与硬件叙事](https://www.apple.com/apple-vision-pro) | 保留 | 硬件人物大图和居中大字分段呈现；视频0.71→6.32秒、readyState4，房间中浮现空间App图标，随后切到沉浸城市环境。 |
| [Slop New York：城市漫游界面](https://mrdoob.github.io/slop-newyork) | 保留 | 纽约街道、出租车、雷达与导航HUD正常显示；日间城市切换夜景，路灯窗光及地面反射相应变化。 |
| [React Bits · 流线光丝背景](https://reactbits.dev/backgrounds/threads) | 保留 | 白色多层光丝发生明显形变，从下部波峰移到上部，线群弯曲与疏密变化可见。 |
| [Granim.js](https://sarcadass.github.io/granim.js) | 质量移除 | 背景确实由蓝色渐变为紫色，网页可用；主体是库介绍、文档与下载入口，展示仅基础双色渐变。 |
| [iPhone Air：产品细节展示](https://www.apple.com/iphone-air) | 保留 | 超薄机身侧面大图；亮点轮播从四色侧面切至前置相机人物画面，指示点/选中tab同步变化。 |
| [Cyber Web City：霓虹城市](https://greggman.github.io/cyber-web-city) | 保留 | 霓虹楼群、雪粒与飞行汽车实际渲染；C键后由外部追踪视角转入驾驶舱，构图和HUD提示更新。 |
| [React Bits · 虹彩流动背景](https://reactbits.dev/assets/video/iridescence.mp4) | 保留 | 紫蓝虹彩液面的斜向褶皱旋转、拉伸，中央紫色尖端位置明显变化。 |
| [CSS Loaders](https://css-loaders.com) | 暂无法核验，移出 | 12个加载卡片页面可见；观察到的前6个立方体在两次画面中没有明确动态变化。 |
| [Cuberto：数字产品与品牌案例](https://cuberto.com) | 保留 | 白底大排版与彩色产品视频首屏，进入/projects/后出现分类标签和错落案例封面，含手机、电商/品牌作品。 |
| [Sketch Material：手绘材质](https://r3f-sketch-material.vercel.app) | 保留 | 汽车、墓碑与THREE JS立体字均以蓝色手绘线条渲染；点击后场景逐步洗去为空白纸面，按钮变为REVEAL。 |
| [React Bits · 可推动的物理球池](https://reactbits.dev/backgrounds/ballpit) | 保留 | 白色球体被推开形成中央空隙并重新分布，确认推动碰撞反馈。未单独验证抓取抛掷模式。 |
| [Animista：文字字距展开](https://animista.net/play/text) | 保留 | 文字先呈灰色且字距压缩重叠，随后展开成清晰正常字距的Animista。 |
| [Instrument：品牌与产品作品集](https://www.instrument.com) | 保留 | 大号字标、衬线介绍与圆角两列项目展示实际加载；PRODUCT复选项变为选中且黑色标签激活，项目图片显示。 |
| [React Bits · 发光能量球](https://reactbits.dev/assets/video/orb.mp4) | 保留 | 光环高亮从右下移至左侧，紫色能量边缘同时变形。 |
| [Are.na：内容收集工具的界面表达](https://www.are.na) | 保留 | 黑色极简产品页面显示桌面界面与叠加手机；点击Arrange后从内容捕捉输入框切换为频道图片网格，Arrange高亮。 |
| [React Bits · 像素旋涡背景](https://reactbits.dev/backgrounds/balatro) | 保留 | 两次画面中的红蓝旋涡折叠形态与位置明显改变；减少动画偏好下仍有较慢流动和手动搅动。 |
| [Soft Labor：模糊文字聚焦](https://www.softlabor.biz) | 保留 | 桃色背景与颗粒模糊字标；About页面加载，标题聚焦后由颗粒字变清晰黑字，logo仍保留模糊颗粒。 |
| [Aceternity · Apple 风卡片展开](https://ui.aceternity.com/live-preview/apple-cards-carousel-demo) | 保留 | 卡片展开为带标题、正文与MacBook图像的详情层，Esc后回到横向卡片列；观察到展开/退场中间画面。 |
| [XK Studio：时间轴视频导航](https://xk.studio) | 保留 | 视频currentTime分别6.93/6.99/7.34后6.18/2.78/5.74（多条循环视频），paused均false、readyState升至4；滚动使选中项目从SHISEIDO转为XKR PROTECT，再转APPLE MACBOOK，主体由玫瑰转橙色机械雕塑、金属流体花朵。 |
| [Tokyo：城市模型与材质切换](https://jeantimex.github.io/tokyo) | 保留 | 车站、轨道、建筑与道路密集场景完整可见；点击模式后建筑表面由写实纹理切为浅色抽象块体。 |
| [Aceternity · 层叠人物推荐卡](https://ui.aceternity.com/live-preview/animated-testimonials-demo) | 保留 | Sarah Chen切为Michael Rodriguez，照片翻转、介绍文字逐段出现；主体人物卡与控件可见。 |
| [Tiger Dingsun：散落卡片与列表](https://tiger.exposed) | 保留 | 首页四栏分类文字索引，边缘散落倾斜作品卡片；项目页出现双列海报与固定右侧文字索引，点海报后大图居中、背景模糊并显示prev/next。 |
| [Under the Sea：月夜鱼群与钓鱼场景](https://underthesea.wawasensei.dev) | 保留 | 月夜水面、渔夫小舟、成群鱼粒与灯光反射可见；点击水面后渔夫抛竿，HUD进入Casting并出现Lure Cam小窗。 |
| [Aceternity · 滚动时间轴](https://ui.aceternity.com/live-preview/timeline-demo) | 保留 | 2024及Early 2023的图文区块正常显示，左侧紫蓝进度线随滚动延伸。 |
| [Oliver Du Puy：建筑摄影与错位网格](https://www.oliverdupuy.com) | 保留 | 首屏整幅静物摄影和宽字距品牌文字；随滚动图片淡出、标题移至固定顶栏，揭示留白很大的错位建筑照片网格与项目名。 |
| [Sakura Fantasy：樱花幻想](https://sakura.billpwchan.art) | 保留 | 笔触圆环与樱花入口进入山水河道；小舟前进、水波和灯笼倒影持续变化，标题淡出后主体仍正常。 |
| [Aceternity · 粘性滚动内容揭示](https://ui.aceternity.com/live-preview/sticky-scroll-reveal-demo) | 保留 | 右侧固定卡片从青绿 Collaborative Editing 切为橙黄 Version control，左侧对应段落随滚动进入。 |
| [Andrew Trousdale：节点式作品导航](https://andrewtrousdale.com) | 保留 | 左侧细线连接不同几何节点，右侧文字索引折叠展开；点击节点实际转/nodes/interactive-machines，关系图重新聚焦、节点变绿，右侧显示PATH和CONNECTIONS。 |
| [Smear Frames：拖影运动短片](https://smear.niccolofanton.dev) | 保留 | WebGPU实时短片由彩色几何物体切换到立体SMEAR排版，播放计时增长，具有可见运动与场景变化。 |
| [Aceternity · 悬浮 Dock 导航](https://ui.aceternity.com/live-preview/floating-dock-demo) | 保留 | 中央图标与邻近图标按距离放大，出现Aceternity UI提示文字；前后截图明显不同。 |
| [MUDA：伸缩的滚动导航](https://muda.co) | 质量移除 | 当前跳转https://muda.co/index/，首屏为方块MUDA字标和Dirk Koy展览图片，下方单列展览项目；未出现原描述的弹性拉伸/压缩导航。 |
| [Clearwater：清澈水面](https://aureliengmz.github.io/clearwater) | 保留 | 透明水面与海底石块完整，前后截图焦散纹理、波峰及阳光反射显著变化。 |
| [Aceternity · 路径流动光束](https://ui.aceternity.com/live-preview/background-beams-demo) | 保留 | 暗色路径中可见蓝紫亮线；同一路径渐变x1从67.01%变到98.40%，另一条从0.18%变到40.06%，确认光束持续运行。 |
| [Any Given Moment：表盘式导航](https://www.anygivenmoment.co) | 保留 | 首个CHANEL影片currentTime4.48→2.73循环，paused=false readyState=4，白色护肤品画面旋转；拖动拨盘后弧线文字旋转且当前项换为COCO CRUSH NECKLACE，右侧同步显示金色项链。 |
| [Aquarium：交互水族箱](https://aquarium.wawasensei.dev) | 保留 | 水族箱、水下地形、灯光与焦散完整可见；Space后前玻璃碎裂飞散、水流向外倾泻，HUD变为Shattered · spilling。 |
| [Aceternity · 黏液式搜索输入](https://ui.aceternity.com/live-preview/gooey-input-demo) | 保留 | 单个按钮伸展为获得焦点的搜索输入框，搜索图标分离到左侧圆形按钮。未提交搜索。 |
| [E.F Productions：联系表式作品集](https://www.erinfeeproductions.com) | 保留 | 初始砖红色巨型字标转白底；项目目录为横向接触印相表缩略图与标题，滚动可见多行，点击第三张进入W Magazine项目。 详情页最终加载红色沙发背景主图、底部8张缩略图与Credits，实际图像清晰。 |
| [Sandboard：可交互沙面](https://sand.scottsun.io) | 保留 | 细沙、树影与光点正常呈现；拖动后生成明确的凹槽和边缘堆沙阴影，与未绘制画面可直接比较。 |
| [Aceternity · 折射液态玻璃](https://ui.aceternity.com/live-preview/liquid-glass-demo) | 保留 | 圆形透镜变为胶囊形，文字与背景在透镜内呈现折射和RGB色散变化；控制面板有效。 |
| [Ballet National de Marseille：舞蹈式排版](https://www.ballet-de-marseille.com) | 保留 | 首页左侧巨型黑体导航固定，右侧虚线分区滚动；活动页大幅舞者照片上有3D环状白色标题，两次截图中文字环位置明显旋转。 |
| [Magic UI · 点阵旋转地球](https://magicui.design/docs/components/globe) | 保留 | 点阵球体、橙色位置标记正常显示；前后截图中的陆地和标记位置改变，确认球体在转动。 |
| [Archive for Space：层级空间布局](https://archiveforspace.com) | 保留 | 整屏多列建筑/家具摄影，左右边缘仍露出其他图层；底部导航固定，筛选菜单分层展开；选择Generative art后左列改为长城与抽象光线作品。 |
| [Magic UI · 逐条进入的通知列表](https://magicui.design/docs/components/animated-list) | 保留 | 列表先包含多条通知；重播后收缩为单张Payment received卡片，新的事件卡片按序插入并推动已有卡片。 |
| [iPhone Duo：折叠产品概念](https://emotion-iphone-duo.vercel.app) | 保留 | 手机从单块正面变为铰链展开的双屏，进度从0变为0.531，屏幕内容随透视展开。 |
| [Magic UI · 轨道环绕图标](https://magicui.design/docs/components/orbiting-circles) | 保留 | 内外两条圆形轨道上的品牌图标位置明显改变，外圈Notion由左上移到下方，确认持续环绕。 |
| [Magic UI · 放大式 Dock](https://magicui.design/docs/components/dock) | 保留 | GitHub图标区域放大，导航容器跟随扩宽，出现GitHub提示标签。未跳转或提交任何操作。 |
| [Footballs in Motion：足球材质展示](https://footballs.nestorrig.com) | 保留 | 首页PBR足球主体正常；Demo1载入足球群，移动后聚合球群散开、位置和尺度显著变化。 |
| [Magic UI · 鼠标聚光卡片](https://magicui.design/docs/components/magic-card) | 保留 | 原灰色边框在指针附近转为紫粉聚光边缘，卡片背景受光；未填写或提交登录表单。 |
| [Volatile Nexus：玻璃环与方块](https://dasprinzip.com/tinker/day42) | 保留 | 透明虹彩圆环、金色立方粒子及地板倒影正常出现，拖动后视角旋转且粒子位置改变。 |
| [Magic UI · 数字滚动计数](https://magicui.design/docs/components/number-ticker) | 保留 | 数字从100重置并逐渐增加，AX中捕获35、紧接截图59，确认不是静态终值。 |
| [ABYSSAL：海面与天空场景](https://token-gremlin.github.io/natural-disasters) | 保留 | 海面、天空与电影HUD完整；海浪纹理持续变化，按N从Dead Calm进入Sunrise，场景光照与镜头改变。 |
| [Magic UI · 流光边框](https://magicui.design/docs/components/border-beam) | 保留 | 紫橙色流光从顶部移动到右边缘；DOM中offset-distance随播放更新。未操作示例登录表单。 |
| [Garden Anomaly：透明球与花园折射](https://dasprinzip.com/tinker/day41) | 保留 | 梦幻花园背景与蓝色透明球正常出现；拖动后球体经纬线、折射纹理、轮廓朝向改变。 |
| [Magic UI · 彩纸庆祝反馈](https://magicui.design/docs/components/confetti) | 保留 | 按钮上方喷射出蓝、紫、黄、绿彩纸粒子，截图捕获散落过程。 |
| [WebGPU Glass：玻璃材质演示](https://webgpu-glass-material.vercel.app) | 保留 | 默认透明玻璃测试球正常显示折射与色散；切换后出现绿色透明凝胶立方体，内部骨架折射可见。 |
| [Dogstudio：艺术与技术工作室](https://dogstudio.co) | 保留 | 三维蓝紫色犬、枝叶与大型衬线标题完整；菜单展开时模型旋转至另一视角，出现五项全屏导航。 |
| [Predator Cloak：隐形折射材质](https://predator-material.vercel.app) | 保留 | 森林中的Predator角色完整加载；点击后按钮变Cloak Pinned，后续截图角色从金属实体变为透光折射轮廓。 |
| [KPR：科幻终端世界观](https://kprverse.com) | 保留 | 科幻角色插画、大型排版和终端风框线完整；滚动后首屏缩为不同尺寸图片卡片与分栏故事区，导航状态同步变化。 |
| [Ramen Dumplings：汤碗物理场景](https://spacemagik.github.io/dumplings) | 保留 | 雨夜暖光餐桌、汤碗、蒸汽和行走的拟人饺子完整；拖动可旋转场景，前后饺子位置和蒸汽明显变化。 |
| [Craftz.dog：简洁的个人主页](https://www.craftz.dog) | 保留 | 窄栏个人主页、头像与体素桌面人物完整；拖动后桌面和角色朝向改变，三维插画与正文布局正常共存。 |
| [The Boiler Room：手绘锅炉房与小生物](https://isaac-mason.github.io/the-boiler-room) | 保留 | 暖色手绘锅炉房与黑色煤块小生物完整；拖动后视角从正面变为俯视，生物分布与尘粒变化。 |
| [Resn：创意数字体验](https://resn.co.nz) | 暂无法核验，移出 | 黑色晶体持续转动、缩放可见；长按后文字导航消失，未进入可辨认的其他体验，View All Projects元素没有布局无法点击。 |
| [Lively Crossing：手绘街口与行人](https://isaac-mason.github.io/lively-crossing) | 保留 | 手绘风城市街口与数十名行人正常加载；后续画面行人持续前进，拖动后镜头转向街树和侧面道路。 |
| [makemepulse：动态项目呈现](https://www.makemepulse.com) | 保留 | 错落大型细体标题和媒体卡片正常；点击后卡片扩展为全屏项目详情背景，进入Brunello Cucinelli案例标题。 |
| [3D Wave Grid：立方体波浪](https://projects.arkon.digital/threejs/wavy-cubes) | 保留 | Franky.dev单页与白色立方网格完整；后续网格方块高度和紫色光影位置改变，指针经过后起伏继续变化。 |
| [Long Hoang：互动 3D 作品集](https://longhoang-lyo.com) | 保留 | 首屏为黑色等距城市、机器人与荧光绿大字；点击后发生黑场转场，进入有机器人、锥桶、紫树和成片草地的三维场景。 |
| [Volumetric Light：手部点阵与体积光](https://cullenwebber.github.io/three-volumetric-light) | 保留 | 真实手部模型托起发光点阵，斜向体积光与空气粒子正常；后续画面点阵轮廓、手指姿态及颗粒位置变化。 |
| [Jordan Breton：空间式作品集](https://jordan-breton.com) | 保留 | 发光描边森林启动后渐变成彩色草地、巨树、瀑布与浮岛；拖动后树干和瀑布位置改变，粒子与水流在多帧中持续变化，完整探索导航出现。 |
| [Boing-boing Box：透明箱中的软球](https://dasprinzip.com/tinker/day38) | 保留 | 透明立方体内蓝黄软球完整可见；操作后箱体旋转，内部球体重新分布并改变形状，地面反射同步变化。 |
| [Teahu：浮岛与路径视角转场](https://www.teahu-experience.com) | 保留 | 初始整座低多边形浮岛，点击Home后镜头推进到岛上路径第一人称视角；房屋、街灯和发光传送门完整渲染。 |
| [WebGPU：页面形变转场](https://page-transitions-with-webgpu-vanilla-js.crnacura.workers.dev) | 保留 | 山岳照片卡片完整显示；点击后路由变/3，周边卡片淡出，所选照片留在中央并进入左侧文字详情布局，捕获中间与完成画面。 |
| [Bilal：三维个人作品集](https://bilal.show) | 暂无法核验，移出 | 持续停留于粉红背景bilal show与三点加载动画，未进入作品主体。 |
| [Soo-ah：可探索的房间作品集](https://www.sooahs-room-folio.com) | 保留 | 欢迎卡片缩入三维空间后移开，显现粉紫小房间、书桌、电脑、玩偶与木质导航牌；拖动过程中视角和电脑屏幕内容有变化。 |
| [Three Particles：彩色粒子团](https://cullenwebber.github.io/three-particles) | 保留 | 彩色粒子团与中央标题正常；后续粒子从紧密团块扩散为多臂结构，球体位置和拖影持续变化。 |
| [Merouane Bali：3D 作品集](https://merodev.net) | 暂无法核验，移出 | 深色等距网格和悬浮发光方块有升降动画，作者与控制面板出现；本轮始终未看到完整作品内容。 |
| [CMS Cube Gallery：立方体图集](https://gsap-cubic-scrollable-image-gallery.webflow.io) | 保留 | Reina Takagi背景、立方小图和姓名切为Ayaka Mizuno，立方体移动至上方且图片换面。 |
| [Keychron：三维键盘配色体验](https://keyboard.jingfu.design) | 保留 | 完整白色木侧框键盘渲染；滚动产生镜头缩放，点击深色色块后整套键帽变成黑色，色块选中环同步移动。 |
| [Gravity Trail：重力图片轨迹](https://madewithgsap.com/codrops) | 保留 | 移动后出现多张图片的指针拖尾，图片下落移出画面，主体文字及Demo控件正常。 |
| [磁轴键盘开关：透明结构与模型运动](https://jingfu.design/work/keyboard-switch) | 保留 | 透明紫色磁轴开关完整渲染，在黑色大字背景前由底部移至中央并改变朝向，透明外壳与内部弹簧清晰。 |
| [Palantir：球面轨迹透镜](https://palantir-seven.vercel.app) | 保留 | 夕阳荒草地、透明球和环境反射完整；拖动后视角改变，球旁出现橙色发光尾迹及地面照明。 |
| [CD 光谱衍射：可转动唱片](https://jingfu.design/work/cd) | 保留 | 正面大面积蓝绿虹彩光带随拖动旋转成倾斜银色盘面，反射与细长彩色衍射条带明显改变；透明盘心和盘缘完整。 |
| [iMoss：数字苔藓球](https://imoss.bio) | 保留 | 高密度绿色纤维球完整渲染；拖动后球体位移、旋转和轮廓压缩改变。 |
| [Patatap：声音与形状触发](https://patatap.com) | 暂无法核验，移出 | 由0/26载入界面进入Press anywhere提示，操作后提示消失；随后截图持续灰色，未捕获预期几何形状动画。 |
| [Video Wall：三维视频墙](https://threejs-video-wall.vercel.app) | 保留 | Start后出现环状发光方块，随后镜头进入三维矩阵视频墙；两帧视频内容、墙块位置和光照明显改变。 |
| [Typatone：会发声的文字界面](https://typatone.com) | 暂无法核验，移出 | 完整屏幕键盘和蓝绿渐变输入区可见，背景颜色持续变化；点击后出现光标，但没有确认输入文字出现。 |
| [False Earth：宇航员与银色草海](https://false-earth.mingjyunhung.com) | 保留 | 宇航员置身银色草海与星空，草叶起伏；按W后角色移动，按C从第三人称切为第一人称，HUD同步改变。 |
| [Oimo Bubbles：互动泡泡](https://oimo.io/works/bubbles) | 质量移除 | 建议降级到实验参考或移出高质量主推荐：画面极小且非常简朴，功能通过不代表符合用户高视觉完成度要求。 |
| [Ink Whale：线描鲸鱼](https://the-ink-whale.vercel.app) | 保留 | 白底灰色鲸鱼轮廓正常；拖动后姿态从横向侧面变为竖向俯视，鳍尾位置与描边变化。 |
| [Fluid Particles：粒子流体](https://david.li/fluid) | 保留 | 空线框容器变成密集蓝色三维粒子体；拖动后粒子体朝向和表面轮廓改变，Edit/Fluidity/Speed控制出现。 |
| [Astro Barba：连续页面转场](https://page-transitions-astro-barba-gsap.crnacura.workers.dev) | 质量移除 | 建议从高质量视觉主库移除或降级：主体是教程配套的占位布局，视觉信息量明显低于其他成品。 |
| [Resend：开发者产品官网](https://resend.com) | 保留 | 黑色衬线大标题、半透明按钮与暗色光照完整；首屏出现立体分块结构，滚动进入精细信封图标、金色标题和多语言标签界面。 |
| [Music Player：立体播放列表](https://gobzzzmusicplayer2024.vercel.app) | 保留 | 专辑卡片以三维圆环形式显示；点击Next后The Strokes切为Toploader，卡片旋转、标题动画与播放状态同步改变。 |
| [Supabase：数据产品界面展示](https://supabase.com) | 保留 | 深色绿色强调的产品卡片和品牌墙完整；Table Editor切换SQL Editor后选中描边移动，演示内容从数据列设置变成SQL编辑器布局。 |
| [Framer：画布与网站编辑器展示](https://www.framer.com) | 保留 | 蓝色发光视频画面在多个时间点改变；下方展示完整三栏设计画布，页面层级、代理输入与中心网页构图清楚。 |
| [Async Transitions：异步页面转场](https://async-page-transitions.crnacura.workers.dev) | 质量移除 | 建议从高质量主库移除或降级：是教程配套的简约转场示例，视觉信息量偏低。 |
| [Cursor：多界面产品演示](https://cursor.com) | 保留 | 桌面任务列表、内容面板与叠加CLI窗口完整；多帧中从构建落地页切换到Mission Control任务与规划内容。 |
| [Shoe Finder：球面球鞋图库](https://shoe-finder-wine.vercel.app) | 保留 | 球面排列的鞋款缩略图和底部胶囊筛选条完整；点击后Nike图集淡出重排为New Balance图集，捕获过渡与完成状态。 |
| [Portal：滚动空间穿越](https://r3f-lusion-portal.vercel.app) | 保留 | 宇航员位于发光网格隧道中央；滚动后紫色灯带转为蓝色，宇航员姿态、喷射光和隧道视角变化。 |
| [Glass Attraction：玻璃拼片球](https://r3f-rapier-ball-of-glass.vercel.app) | 保留 | 透明多边形拼片组成单个球体；拖动后球体转向且局部拼片轮廓变形，再次观察趋于完整球形。 |

## 新增条目逐项记录

| 作品 | 实际操作 | 实际所见 |
|---|---|---|
| [Igloo Inc.：品牌官网](https://igloo.inc) | 等待三维场景加载后多次向下滚动。 | 雪山中的发光冰屋完整渲染，冰块从分离悬浮状态收合并再次裂开；角落排版带字符扰动。 |
| [monopo London：创意机构界面](https://monopo.london) | 加载首页后将指针从中部拖至右上方。 | 橙蓝噪点渐变波形持续变化；玻璃球随指针移动，球内出现日文与折射色边，球外仍是英文标题。 |
| [Blobmixer：虹彩雕塑轮播](https://blobmixer.14islands.com) | 等待17%加载页结束，点击Next blob。 | Fomosphere虹彩扭曲造型切换成Discobrain，背景色、三维表面形态和大字标题同步变化。 |
| [Clay：数字产品与品牌案例](https://clay.global) | 滚动至作品视频，点击播放，并通过播放器方向键抽查。 | 首页展示三屏移动App界面；作品录像实际播放至28秒，出现Marqeta紫色支付产品网页及卡片三维展示。 |
| [Rive：3D 车辆与座舱控制面板概念录像](https://framerusercontent.com/assets/gJRDfn586X2wZK2eEhDhmpR2lng.mp4) | 从官网 TRY IT LIVE 进入车辆演示；live截图连续超时，改看官网引用的官方16秒MP4并点击重播。 | 录像2秒为车辆80%电量圆弧、天气与柱状图；12秒变为媒体封面面板；末帧是导航地点列表与宽幅3D地图。车辆镜头与环境光同步变化。video currentTime=2.98、paused=false、readyState=4。 |
| [Three.js：周期表空间排列](https://threejs.org/examples/css3d_periodictable.html) | 查看平面周期表，点击SPHERE，再点击HELIX并观察完成后的布局。 | 青色半透明元素卡片由平面表格聚成球面，随后重排为多圈螺旋；卡片透视、重叠和位置共同变化。 |
| [Rauno · Vanish Input](https://rauno.me/craft/vanish-input) | 输入Motion design后按Enter | 文字真实显示后，从右侧碎裂成细小白色颗粒逐渐消散。 |
| [House of Corto — 可拖动家具画廊](https://www.houseofcorto.com) | 观察矩形开场并拖动画廊 | 层叠绿色矩形收缩后露出家具图片矩阵；拖动后整组图片位置明显变化。 |
| [Lando Norris 官方网站](https://landonorris.com) | 等待首屏加载并比较两个时间点 | 人物正面肖像上叠加头盔部件，面罩横过脸部后消失，线框头盔上移，背景等高线也变化。 |
| [Active Theory：数字体验工作室](https://activetheory.net) | 等待首屏加载，点击Work并向下滚动。 | 金属环形标志、漂浮粒子和有机形态完整渲染；滚动时镜头转向并穿行场景，粒子分布和高光持续变化。 |
| [14islands：产品与品牌作品集](https://www.14islands.com) | 滚动浏览首页标题、宽幅影像及项目网格。 | 大字号非对称排版、宽幅点阵人物影像、Cartier与Cogent双列项目卡完整呈现，文字随滚动揭示。 |
| [Makepill：产品机构官网](https://makepill.com) | 首屏完成加载后向下滚动。 | 黑色首屏中透明胶囊包裹虹彩头盔；滚动切为浅色段落与黑色圆形物体，标题以遮罩方式展开。 |
| [Immersive Garden：数字体验官网](https://immersive-g.com) | 等待加载100%后连续滚动两段。 | 浅色雕花浮雕场景出现，衬线标题被逐步揭示，随后出现飞机与地球主题项目展示画面。 |
| [Studio Freight：品牌项目编排](https://studiofreight.com) | 首页滚动，选择Telemetric项目卡。 | 白底衬线排版、悬浮散布的图片卡及中央项目标题联动；点击进入对应项目路由。 |
| [Studio Herrström：音乐与文化品牌展示](https://studioherrstrom.com) | 关闭非必要cookie提示并滚动浏览项目网格。 | 黑底衬线大标题、细线分栏网格和Spotify/Milkshake品牌视觉完整显示；图像和说明交替编排。 |
| [Ramotion × Descript：产品网站与品牌界面](https://www.ramotion.com/descript-brand-identity-and-web-design) | 从首页进入Descript案例，多次滚动查看品牌与网页展示。 | 蓝色品牌动效、编辑器窗口和手机响应式网页稿均完整显示，含深蓝首屏、功能卡片和格式导出界面。 |
| [Robb Owen：创意开发者作品集](https://robbowen.digital) | 打开首页，移动指针后点击MENU。 | 浅蓝紫色线描人物与衬线标题完整显示，菜单展开成全屏浅蓝导航与双列说明。 |
| [Seán Halpin × Help Scout：AI 编辑器界面](https://www.seanhalpin.xyz/work/ai) | 查看首页并进入Help Scout AI案例，向下滚动。 | 首页为浅绿渐变与圆角彩色项目卡；案例显示AI编辑器中的紫色生成占位、浮动结果卡和操作按钮。 |
| [Henry Heffernan：个人作品集](https://henryheffernan.com) | 等待BIOS资源完成，点击START，再点Click anywhere to begin | 完整灰白3D办公桌场景出现，镜头从全景推近CRT显示器；屏幕内是复古窗口、桌面图标与个人作品集。 |
| [Rauno · 横向海报导航](https://rauno.me) | 等待首屏入场后向下滚动一屏 | 黄色圆形配巨大黑字的个人简介卡，滚动后横向滑到橙色圆形与巨大DD字样卡，顶端细刻度进度条随卡片移动。 |
| [abeto：实时交互作品集](https://abeto.co) | 等待白屏入场完成后滚动观察 | 金黄色手绘花朵从白底逐步展开，带纸张颗粒纹理；花瓣轮廓持续变形，覆盖白色大字和底部联系文字。 |
| [Aristide Benoist：动效开发作品集](https://aristidebenoist.com) | 等待入场，滚动条带并点击P&H缩略图 | 黑白细条图片横向移动，点击后展开为大幅灰白照片轮播，巨大P&H字形叠在图片上；相邻项目在两侧留出预览。 |
| [Chiara Luzzana：声音设计作品集](https://www.chiaraluzzana.com) | 等待字体入场，点击进入，然后拖动指针经过雕塑区域 | 空心与实心衬线文字的黑色序幕转成米白主场景；层叠圆片构成的球形雕塑改变朝向，PURITY与NOISE大字跨在前后，右上菜单轮廓持续变形。 |
| [Pitch：演示文稿产品界面展示](https://pitch.com) | 打开首页，滚动并定位Slide editor产品展示区 | 紫色渐变首屏与演示稿封面背景，随后看到AI输入面板、三栏幻灯片编辑器缩略界面、样式浮层和协作头像提示。 |
| [Superhuman Mail · 邮件与AI助手界面](https://superhuman.com/products/mail) | 从主页Looking for Superhuman Mail链接进入产品页，定位Respond faster展示区 | 可见分组收件箱列表、标签状态与右侧邮件/AI建议浮层；浅色界面叠在紫蓝渐变背景上。 |
| [Reflect：笔记产品界面展示](https://reflect.app) | 浏览紫色光环首屏，定位并点击官方launch film，观察14秒至35秒播放状态 | 深紫色粒子光环背景、深色三栏笔记编辑器预览与居中播放按钮；52秒官方片实际推进，见紫色星空片头和深色Markdown编辑/终端窗口。 |
| [CleanShot · 截图编辑器界面](https://cleanshot.com/screenshots) | 浏览产品首页，进入Explore screenshots具体截图功能页 | 可见完整截图编辑窗口：顶部密集图标工具条，左侧渐变背景缩略网格，右侧带投影的卡片画布；首页另有截图浮层和三张标注/遮挡/背景示例。 |
| [Things · 任务清单与项目界面](https://culturedcode.com/things/features) | 进入Features页并滚动查看桌面与手机界面 | 手机Today清单与桌面项目窗口并列；清晰的彩色分组图标、分区标题、勾选框、日期标记、弱化标签和底部工具条。 |
| [Notion Calendar：日历产品展示](https://notion.com/product/calendar) | 查看桌面周视图与手机三日视图，并打开 Vimeo 介绍录像。 | 桌面日历有多列彩色日程块、左侧日历分组；手机展示三日排布。Vimeo900932859可播放但主要为人物介绍，因此保留产品UI展示页。 |
| [Spline：3D 设计产品展示](https://www.spline.design) | 查看首屏3D城市编辑器，点击 Show inspector。 | 城市模型、选择框及Agent步骤可见；Show inspector打开右侧属性检查面板。 |
| [tldraw：即时白板界面](https://tldraw.com) | 在空白画布选择矩形并拖拽绘制，再点紫色及浅色填充。 | 画布生成紫色轮廓浅紫填充矩形；底部浮动工具栏与右侧颜色、填充、线型、字体属性同时呈现，选形状后面板增加对齐和字体选项。 |
| [Excalidraw：手绘风白板界面](https://excalidraw.com) | 在空画布选择菱形拖拽绘制，点击浅蓝背景颜色。 | 出现手绘黑色轮廓、浅蓝填充的圆角菱形及紫色选择框；左侧展开颜色、填充、粗细、线条风格等上下文属性。 |
| [Song Maker：音乐网格创作界面](https://musiclab.chromeexperiments.com/Song-Maker) | 点击四个不同高度的网格音符并播放，再观察两个时刻的画面，最后停止。 | 黄绿紫橙色块即时加入网格，Play变Stop，淡蓝竖向播放列从最左侧推进到中部。底部圆形乐器按钮和速度滑杆清晰。 |
| [Elastic Man：可拉扯回弹的 3D 面部](https://d21u3ic0kp9e91.cloudfront.net/elasticman/0/index.html) | 原候选重定向作者首页，沿Elastic Man原作链接进入Adult Swim；外层拖动反馈不清，打开页面内嵌作品地址并拖动右侧面颊。 | 独立画布出现脸颊与额头褶皱、下巴拉扯变形，随后回弹成光滑面部；眼睛跟随指针朝右下看。 |
| [Fluid Paint：流体绘画](https://david.li/paint) | 拖拽绘制绿色笔触，再在色环选择橙色并交叉绘制。 | 画布出现带细密刷毛纹理、柔软边缘的绿色与橙色笔触，交叠处随绘制产生流体颜料痕迹。 |
| [Ocean Wave Simulation：海浪模拟](https://david.li/waves) | 查看持续变化的海面，并拖动CHOPPINESS滑杆由1.5到2.3。 | 蓝色海面有细密高光波纹和不断变化的波峰，倾斜摆放的波形图、风向与尺度UI环绕场景；尖锐度数值与曲线一起变化。 |
| [Things 3：待办编辑卡插入列表](https://60fps.design/shots/things-3-drag-to-create-to-do-interaction) | 逐页播放主录像，读取两次媒体状态并查看截图 | 空白项目页变成插入新待办的编辑卡片，卡片悬浮阴影、上下行让位和键盘入场清晰。 currentTime 0→4.15秒；时长7.58秒；paused=false、readyState=4。 |
| [Perplexity：模型选择抽屉形变](https://60fps.design/shots/perplexity-model-selection-sheet-morph-interaction) | 逐页播放主录像，读取两次媒体状态并查看截图 | 模型选择圆角底部弹层上移扩展，拖动条、关闭按钮、模型列表及背景模糊保持连续。 currentTime 0→4.99秒；时长16.63秒；paused=false、readyState=4。 |
| [Snapseed：照片散落叠放](https://60fps.design/shots/snapseed-photos-pop-shuffle-effect) | 实际播放并补抓核心动效帧，读取媒体状态 | 全屏骑行照片与黑底产品说明转为多张有阴影、倾角和层次的照片散落叠放；底部添加照片入口出现。 currentTime 0.06→3.90秒；时长4.30秒；最终paused=false、readyState=4。 |
| [Airbnb：立体分类图标入场](https://60fps.design/shots/airbnb-tab-icon-animation) | 逐页播放主录像，读取两次媒体状态并查看截图 | 搜索栏下方空白区域出现房屋、热气球、服务铃三枚立体分类图标及标签；当前体验图标更大。 currentTime 0→2.00秒；时长2.42秒；paused=false、readyState=2。 |
| [Pokémon TCG：卡包拆封动效](https://60fps.design/shots/poke-mon-tcg-pocket-swipe-packet-to-reveal-card-interaction) | 实际播放并补抓核心动效帧，读取媒体状态 | 紫色卡包由小变大，顶部亮线扫过，包装封条沿横向切口剥离，金属反光与袋口清晰。 currentTime 0→3.81→9.37秒；时长12.43秒；最终paused=false、readyState=4。 |
| [Chrome：下拉操作导航](https://60fps.design/shots/google-chrome-pull-down-to-reload-and-new-tab) | 播放主录像，核对媒体时间推进与关键状态截图 | Chrome首页下拉时整页内容下移，顶部出现新增、刷新、关闭三项，刷新圆形背景高亮。 currentTime 0.15→4.37秒；时长8.82秒；最终paused=false、readyState=4。 |
| [CRED：账单卡堆轮换](https://60fps.design/shots/cred-autopay-bills-stack-animation) | 播放主录像，核对媒体时间推进与关键状态截图 | 底部弹层内账单卡片呈层叠队列，电费卡退位为宽带账单，付款按钮与金额随卡片切换。 currentTime 0.07→4.31秒；时长9.47秒；最终paused=false、readyState=4。 |
| [Swatch This：拟物相机与色样展示](https://60fps.design/shots/swatch-this-3d-camera-flip-interaction) | 播放主录像，核对媒体时间推进与关键状态截图 | 拟物黑色相机采色界面转到小型相机镜头与银色色样纸片，带立体阴影与完成星光。 currentTime 0→3.81→8.82秒；时长9.07秒；最终paused=false、readyState=4。 |
| [Recollect：收藏面板转为照片卡片](https://60fps.design/shots/recollect-value-prop-morph-interaction) | 播放主录像，核对媒体时间推进与关键状态截图 | 紫橙渐变引导中，小型收藏操作面板变为照片卡片，底部价值主张同步替换。 currentTime 0.12→6.16秒；时长9.17秒；最终paused=false、readyState=4。 |
| [Monogram：语音输入液态模糊反馈](https://60fps.design/shots/monogram-tap-and-hold-mic-liquid-blur-pulse-interaction) | 播放主录像，核对媒体时间推进与关键状态截图 | 语音交互激活后下部内容被液态弯曲、模糊遮罩覆盖；底部胶囊转成黑色Thinking加载状态。 currentTime 0.04→4.01→10.14秒；时长16.97秒；最终paused=false、readyState=4。 |
| [Currency Converter：手写货币符号筛选](https://60fps.design/shots/currency-simple-converter-draw-symbol-interaction) | 播放主录像，核对媒体时间推进与截图；需要时滚动查看视频下半部 | 币种选择器中出现手写黑色符号，下方币种列表随着识别结果实时替换；顶部圆角分类栏保持稳定。 currentTime 0→4.45→5.82秒；时长9.03秒；最终paused=false、readyState=4。 |
| [Linear：问题编辑操作弹层](https://60fps.design/shots/linear-issue-actions-popup-interaction) | 播放主录像，核对媒体时间推进与截图；需要时滚动查看视频下半部 | 黑色Inbox空态转为任务新建面板，键盘升起，状态/优先级/负责人/标签工具行横向移动。 currentTime 0.05→4.03→8.48秒；时长14.43秒；最终paused=false、readyState=4。 |
| [Lumy：位置选择抽屉](https://60fps.design/shots/lumy-select-location-sheet-interaction) | 播放主录像，核对媒体时间推进与截图；需要时滚动查看视频下半部 | 深蓝机舱窗引导与荧黄色地点按钮转为黑色城市列表面板，纽约、伦敦等条目出现。 currentTime 0.73→4.35秒；时长9.73秒；最终paused=false、readyState=4。 |
| [Google：搜索入口转入 AI 页面](https://60fps.design/shots/google-ai-mode-search-morph-interaction) | 播放主录像，核对媒体时间推进与截图；需要时滚动查看视频下半部 | Google深色首页的搜索入口转为AI Mode页面，输入区与键盘出现，背景信息卡退场。 currentTime 0→3.06秒；时长6.99秒；最终paused=false、readyState=4。 |
| [Find My：搜索物品放大镜动画](https://60fps.design/shots/apple-find-my-searching-items-sheet-animation) | 播放主录像，核对媒体时间推进与截图；需要时滚动查看视频下半部 | 地图上白色圆角查找面板内放大镜移动，镜下由耳机图标变为箱形物品，灰色物品底纹隐约可见。 currentTime 0→4.39秒；时长12.01秒；最终paused=false、readyState=4。 |
| [Opal：敲开宝石奖励](https://60fps.design/shots/opal-tap-to-reveal-gem-interaction) | 播放录像并对照关键帧，读取两次以上媒体状态 | 黑色洞穴中石壳破裂，彩色透明宝石完整出现，奖励名称、稀有度与解锁信息浮现。 currentTime 4.45→8.22秒；时长9.41秒；paused=false、readyState=4。 |
| [Good Air：天气时间滑杆](https://60fps.design/shots/good-air-time-slider-dynamic-weather-interaction) | 播放录像并对照关键帧，读取两次以上媒体状态 | 天气背景由蓝天转为橙红夕阳，温度29变28；底部刻度选中6PM并与背景联动。 currentTime 0.04→4.88秒；时长18.17秒；paused=false、readyState=4。 |
| [Cosmos：主题切换预览](https://60fps.design/shots/cosmos-theme-switcher-interaction) | 播放录像并对照关键帧，读取两次以上媒体状态 | 外观选择页的图片网格预览、页面背景及按钮由浅色转为黑色；暗色选项显示选中。 currentTime 0.05→5.52；复核0.77暗色秒；时长5.53秒；paused=false、readyState=4。 |
| [Apple Astronomy：行星壁纸切换](https://60fps.design/shots/apple-astronomy-wallpaper-3d-planets-morph-swipe-interaction) | 播放录像并对照关键帧，读取两次以上媒体状态 | 锁屏配置中灰色岩石星体变为蓝色地球，球面纹理、光照、大小以及时间文字色调同步变化。 currentTime 0.01→5.75秒；时长16.04秒；paused=false、readyState=4。 |
| [Ben Journal：天气背景切换](https://60fps.design/shots/ben-journal-weather-toggle-background-animation) | 播放录像并对照关键帧，读取两次以上媒体状态 | 底部天气选择器从晴天切到雪，天空云层变暗，细密雪粒落下，选择按钮同步高亮。 currentTime 0.03→5.68秒；时长12.00秒；paused=false、readyState=4。 |
| [The Outsiders：进度图表配色切换](https://60fps.design/shots/the-outsiders-progress-graph-color-change-interaction) | 实际播放主录像，读取媒体状态并核对不同阶段画面 | 运动汇总从绿色距离指标切到青色爬升指标，图表圆点、数值、选中胶囊和背景渐变协调变化。 currentTime 0→7.27秒；时长9.87秒；最终paused=false、readyState=4。 |
| [Apple：摄影风格卡片预览](https://60fps.design/shots/apple-photographic-styles-carousel-swipe-interaction) | 实际播放主录像，读取媒体状态并核对不同阶段画面 | 相机设置转入摄影风格选择页，圆角人像轮播卡展示Cool风格，照片下方色调参数和说明卡跟随出现。 currentTime 0.01→5.18秒；时长10.38秒；最终paused=false、readyState=4。 |
| [Moods Faster：心情胶囊展开](https://60fps.design/shots/moods-faster-pills-morph-expand-interaction) | 实际播放主录像，读取媒体状态并核对不同阶段画面 | 五个彩色情绪胶囊中蓝色Neutral胶囊拉长放大，旁边胶囊缩小退让，背景光晕随选中项变化。 currentTime 0→5.55秒；时长6.99秒；最终paused=false、readyState=4。 |
| [Okuri：拟物日历翻页](https://60fps.design/shots/okuri-page-flip-interaction) | 实际播放主录像，读取媒体状态并核对不同阶段画面 | 日历纸面卷起形成真实曲面折页与软阴影，背面文字透出，下页日期信息揭开。 currentTime 0.08→5.73秒；时长6.57秒；最终paused=false、readyState=4。 |
| [Apple Wallet：卡片全息光泽](https://60fps.design/shots/apple-wallet-card-gyro-pattern-color-change-interaction) | 实际播放主录像，读取媒体状态并核对不同阶段画面 | Apple Cash黑色卡面圆点纹理由暗灰反射为粉橙光泽，光带在纹理上变化。 currentTime 0.11→4.52→0.22（循环）秒；时长4.57秒；最终paused=false、readyState=4。 |
| [Avec：语音录音状态反馈](https://60fps.design/shots/avec-hold-and-speak-interaction) | 播放主录像，核对媒体时间推进和实际内容变化 | 邮件撰写界面的底部蓝色语音区变为红色录音状态，波形与松开发送生成提示出现；内容区保持原位。 currentTime 0.04→6.41秒；时长12.13秒；最终paused=false、readyState=4。 |
| [Find My：AirPods 空间搜寻界面](https://60fps.design/shots/apple-find-my-finding-airpods-case-gyroscope) | 播放主录像，核对媒体时间推进和实际内容变化 | 黑底方向箭头指示8ft，接近后整屏变绿，箭头变成同心圆，距离降到0.7ft。 currentTime 0.06→5.54秒；时长14.45秒；最终paused=false、readyState=4。 |
| [Elevate：答案词高亮反馈](https://60fps.design/shots/elevate-correct-answer-words-morph-interaction) | 播放主录像，核对媒体时间推进和实际内容变化 | 深绿答题页从空场转为大字号英文句子，正确词shoes高亮为青绿块，底部答题进度和判断按钮稳定。 currentTime 0.04→5.09秒；时长8.03秒；最终paused=false、readyState=4。 |
| [Cosmos：图片集拖放反馈](https://60fps.design/shots/cosmos-cluster-drag-and-drop-interaction) | 播放主录像，核对媒体时间推进和实际内容变化 | 图片集网格中缩小缩略卡随拖动悬浮到另一图片集上，目标卡有虚线轮廓和移动提示。 currentTime 0→4.60秒；时长9.50秒；最终paused=false、readyState=4。 |
| [Pinterest：商品详情面板横滑切换](https://60fps.design/shots/pinterest-shared-sheet-swipe-interaction) | 播放主录像，核对媒体时间推进和实际内容变化 | 白色商品详情底部面板上方的蝴蝶纽扣切到金色星星，放大商品突出面板边缘，商品名、说明、相似推荐同步切换。 currentTime 0→3.67秒；时长9.82秒；最终paused=false、readyState=4。 |
| [Three.js：可扰动水面](https://threejs.org/examples/webgl_gpgpu_water.html) | 点击并拖动浅蓝水池中央。 | 水面出现大范围椭圆涟漪与反射扭曲，黄色小鸭随水流移动；右侧可见水面参数控制。 |
| [Three.js：海面与天空](https://threejs.org/examples/webgl_shaders_ocean.html) | 查看海面与浮动方块，并将天空elevation由2改为12。 | 初始是日落金色反光、暗色海浪与旋转浮块；改变太阳高度后整体转为明亮白昼，水面高光、天空颜色及方块光照同步改变。 |
| [Three.js：透射玻璃材质](https://threejs.org/examples/webgl_materials_physical_transmission.html) | 查看玻璃球壳，将thickness改为1，再将roughness从0改为0.4。 | 薄片球壳能透过背景并带高光；roughness0.4后壳体变成明显磨砂，背景影像在壳内模糊。 |
| [Three.js：发光后处理](https://threejs.org/examples/webgl_postprocessing_unreal_bloom.html) | 查看离子引擎线框，修改bloom strength从1到0。 | 红黄蓝线框与旋转环在默认值下有大范围柔光；设为0后光晕消失，仅保留细线结构，区别明确。 |
| [Evan Wallace：可交互水池](https://madebyevan.com/webgl-water) | 在方形水池水面横向拖拽。 | 平静水面立刻产生交叠涟漪，水下球体、池底瓷砖和侧壁出现随波变化的明亮焦散光网，球体倒影被扭曲。 |
| [glfx：漩涡与六边形图像滤镜演示](https://evanw.github.io/glfx.js/demo) | 下拉选择Swirl和Hexagonal Pixelate两个滤镜并查看同一照片。 | 山地照片先在中心形成漩涡扭曲，再变成六边形色块拼贴；页面同时展示对应参数滑杆。 |
| [deck.gl：纽约出租车轨迹](https://deck.gl/examples/trips-layer) | 等待曼哈顿轨迹与建筑数据载入，通过Trail滑杆Home和End比较长短尾迹。 | 10.0K行程、3.9K建筑与897.2K顶点数据加载完成，黑色立体城市上橙绿轨迹流动；Trail缩短后变为分散亮点，调长后形成连续街道线网。 |
| [deck.gl：六边形空间聚合](https://deck.gl/examples/hexagon-layer) | 等待英国事故数据载入，将Radius滑杆调至最大。 | 140.1K数据加载完成，地图显示蓝绿黄六边形柱体；半径增大后细密点柱重组成明显的大六边形，柱体高度与颜色仍有层次。 |
| [Rauno · Exclusion Tabs](https://rauno.me/craft/exclusion-tabs) | 点击Changelog标签 | 白色胶囊选中态从Community移动至Changelog，文字反色随选中改变。 |
| [Rauno · Wheel Input](https://rauno.me/craft/wheel-input) | 在日期滚轮上滚动 | 月份由January移动到February，前后日期沿弧面渐隐，中央选中条保持固定。 |
| [Rauno · Vercel Footer](https://rauno.me/craft/vercel-footer) | 在Vercel字标区域拖动指针 | 暗色描边字标被渐变光照局部照亮，三角形与V字显现明暗填充。 |
| [Rauno · Logo Carousel](https://rauno.me/craft/logo-carousel) | 观察标志列表并切换慢动作 | 初始descript、duolingo、FAIRE、Clearbit一列，后续帧出现另一组品牌，并捕获模糊溶解切换过程。 |
| [Rauno · Radial Menu](https://rauno.me/craft/radial-menu) | 按住并沿圆环拖动 | 菜单扇区和外圈高亮，中心出现Reload，证实旋转选择反馈。 |
| [Rauno · Minimap](https://rauno.me/craft/minimap) | 沿刻度横向拖动并观察多帧 | 橙色游标旁的短线刻度出现局部波峰，波峰随着指针移动向右传播。 |
| [Rauno · Fractional Slider](https://rauno.me/craft/fractional-slider) | 按提示横向拖动 | 中央固定蓝点与刻度滑移联动，中心从0变为负数附近，区间刻度变蓝。 |
| [Rauno · Precision Slider](https://rauno.me/craft/precision-slider) | 拖动Volume滑块 | 细线滑块扩展成宽大圆角条，白色填充同步增长，AX值由26变56。 |
| [Rauno · Flashlight Tabs](https://rauno.me/craft/flashlight-tabs) | 点击Settings | 发光胶囊从Deployments滑动到Settings，外框光照与文字高亮同步移动。 |
| [Rauno · Copy & Paste](https://rauno.me/craft/copy-paste) | 点击源图，移动至右侧目标，再右键触发 | 源图生成随指针移动的小缩略图；目标区最终展开完整相同照片，完成复制粘贴视觉闭环。 |
| [shadcn · Dashboard 01 完整数据界面](https://ui.shadcn.com/view/new-york-v4/dashboard-01) | 切换Last7days图表范围 | 完整侧栏、四张指标卡与面积图可见，点击后图表由密集尖峰变为七日简化曲线。 |
| [shadcn · Login 03 认证界面](https://ui.shadcn.com/view/new-york-v4/login-03) | 在Email输入演示地址 | 居中暗色认证卡片完整，输入后文字可见且焦点描边明显。 |
| [Warp Terminal](https://www.warp.dev/terminal) | 滚动并点击Features锚点 | 点阵网格、等宽大标题与电蓝色吸顶导航完整；功能区呈现叠放终端、分支选择器和侧栏窗口。 |
| [Zed Industries：多栏编辑器与产品展示](https://zed.dev) | 观察首屏多帧并滚动 | Zed Industries双产品品牌区与三栏编辑器展示完整，差异代码在多帧中滚动变化。 |
| [Obsidian 知识工作台](https://obsidian.md) | 滚动检查桌面和手机产品展示 | 深色紫色强调官网，笔记树、文章、知识图谱与手机待办完整展示。 |
| [AFFiNE 文档与白板](https://affine.pro) | 滚动查看产品示例并关闭Cookie横条 | 手写Draw与勾选图标构成首屏排版；文档正文、彩色标注、嵌入表格和进度条完整。 |
| [HEY 邮件与日历](https://www.hey.com) | 滚动查看首屏与The Screener示例 | 深蓝圆角页面、紫粉渐变大字与白色邮件界面完整，邮件筛选、头像和分类入口清楚。 |
| [Evervault 支付产品界面](https://evervault.com) | 观察首屏多帧，尝试滚动 | 深紫官网、居中胶囊导航、底部交易状态列表和品牌条正常；品牌轮播在不同时间点改变。 |
| [Felt 地图工作台](https://felt.com) | 在浏览器恢复后重试，首屏和下滚产品界面截图 | 水彩农田道路图叠加状态标记、协作头像和评论卡；下方出现完整深色地图工具栏与地形线路。 |
| [Cal.com 预约日程](https://cal.com) | 首屏截图后滚动并返回首屏比较 | 日历预约卡由Ethan学业咨询变成Isabella摄影预约，头像、时长、地点及选中日期相应改变。 |
| [Notion 工作空间](https://www.notion.com) | 滚动检查并用文档区域截图复核工作台 | 蓝色强调首屏、插画人物和完整四列任务看板；浅色状态分组、侧栏层级及卡片密度清楚。 |
| [Figma Design 产品界面](https://www.figma.com/design) | 首屏、滚动及主展示区域截图复核 | 粉紫噪点背景内出现Museum app设计画布，建筑海报、移动端地址和票务界面并排，底部浮动工具条。 |
| [Penpot 设计工作台](https://penpot.app) | 关闭Cookie并滚动检查完整页面 | 深色编辑器侧栏、属性面板与音乐App多画板完整，亮黄、紫色界面和旅行卡片示例可见。 |
| [Tana — 会议助手与协作面板](https://tana.inc) | 首屏及滚动后完整页面截图比较 | 首屏视频会议四宫格旁的深色助手面板，从文本摘要变化到蓝色柱状图和任务对话。 |
| [Capacities 知识工作台](https://capacities.io) | 点击Discover Product查看产品UI | 深色首页周围漂浮对象卡片；产品页展示多栏笔记、人物对象、关系图谱、日历和白板。 |
| [Playdate 产品官网](https://play.date) | 首屏与向下滚动后产品叙事截图 | 大型黄色掌机、灰色背景、白色图标导航与双色超大play/date字样完整。 |
| [Daylight DC-1 产品官网](https://daylightcomputer.com) | 首屏观察、打开视频模态并关闭、滚动复核 | 自然草地上的平板首屏由白屏花卉画变为琥珀色屏幕，悬浮玻璃导航和橙色按钮完整。 |
| [teenage engineering 产品官网](https://teenage.engineering) | 首屏及滚动截图 | 黑底工业器材大图、细线图标导航、白色窄体字与橙色硬件细节完整。 |
| [Opal 专注应用](https://opalapp.com) | 首屏及两次下滚截图比较 | 黑色洞穴背景、悬浮胶囊导航；下滚文案从灰色逐段变亮，时间计数器数字持续滚动。 |
| [Atmos Gallery 配色工作台](https://atmos.gallery) | 点击Create并跳过导览，查看内置配色列表 | 暖色柔软旋涡背景、薄描边导航；进入工具后出现色带列表、对比度数值和胶囊筛选。 |
| [Aardvark Book Club](https://www.aardvarkbookclub.com) | 等待品牌开场后滚动，完整页面截图 | 紫色开场转为亮黄波浪首页；夸张粗体、手写标注和倾斜书籍卡片可见，粉紫青色区块连续。 |
| [MoMoney 博物馆官网](https://museumofmoney.com) | 首屏多帧、滚动查看叙事与图片卡 | 荧光黄标题牌、黑色硬阴影和紫色票务按钮；奶油底叙事与倾斜彩边照片卡完整。 |
| [MANA Yerba Maté](https://manayerbamate.com) | 等待开场，点击首页右箭头 | 绿色薄荷西瓜饮料罐切换为黄色葡萄柚罐，背景人物、颜色和口味标签同步变化。 |
| [TrueKind 护肤品牌](https://truekindskincare.com) | 观察加载进度及两个首屏视频画面 | 数字开场完成后进入皮肤微距影像；随后切到滴管精华画面，衬线斜体与无衬线标题混排。 |
| [Slack Canvas：文档协作界面](https://www.youtube.com/watch?v=wJ80ip-buXc) | 播放约87秒正片，观察开场及约20至34秒界面段，并用播放滑块前进。 | 彩色通信图标进入 Slack 工作区；Project Alpha 文档由频道右上角浮出，随后展开资源和成员卡片，卡片布局与背景色同步切换。 |
| [Linear Agent：原生工作区展示](https://www.youtube.com/watch?v=mRql2VJ99gM) | 播放55秒正片，核查开场、任务列表中段与约43秒的结果卡片。 | 深色悬浮工作区以倾斜镜头推进，Ask Linear 输入文字后出现带状态图标的问题列表；后段生成带文档图标的 Optimistic loading refactor 计划卡片。 |
| [Framer 3.0：画布与协作展示](https://www.youtube.com/watch?v=6aioEoCdBJw) | 播放75秒正片，查看开场、约25秒多尺寸画布与约43秒 CMS 工作台。 | 开场以蓝光描边强调编辑器顶栏；随后桌面、平板、手机三个页面画布并排呈现，后段展示深色内容表格与右侧 Agent 面板。 |
| [Pitch 2.0：演示编辑器短片](https://www.youtube.com/watch?v=tqfeE5G36tM) | 跳过片前广告后播放82秒正片，查看AI输入、配色选择和约38秒编辑器段。 | 白色AI输入面板配紫色按钮；自行车主题幻灯片旁出现胶囊配色条，选中色有紫色描边；编辑器保留左侧缩略图和内容工具栏。 |
| [Google：Material Design 原始短片](https://www.youtube.com/watch?v=Q8TXgCzxEnw) | 播放官方48秒短片，查看约12秒纸片层级和34秒应用界面；自动播放跳到其他视频后明确回到原片复查。 | 开场彩色矩形卡片与圆形按钮组合，12秒变为带投影的白色分层面板，34秒展示Kodaline专辑封面、浮动播放按钮和曲目列表。原片time34.64、duration48.82、paused=false、readyState4。 |
| [Microsoft Design：OneDrive 界面更新](https://www.youtube.com/watch?v=DzXBdc8Dfmg) | 等待15秒前贴片广告结束后实际播放正式60秒视频，查看约13秒和22秒画面。 | 正式片13秒展示浅色文件列表、推荐卡片、头像与Office筛选标签；22秒转为透明玻璃状几何体和小球的柔光空间。time12.93到22.31，paused=false、readyState4。 |
| [Ordinary Folk：Introducing Spline](https://www.youtube.com/watch?v=sIfP9h-H23s) | 重载后播放85秒正片，观察开场并跳转约41秒。 | 开场紫色地景中人物与叶片产生层次运动；约43秒出现带紫色控制点的青色立方体与双手，展示三维造型操作的视觉隐喻。 |
| [Ordinary Folk：Webflow 新时代短片](https://www.youtube.com/watch?v=eEW2gr7K7kc) | 播放104秒正片并用滑块前进，观察开场及约20秒三维页面段。 | 白色空间内蓝紫几何体与半透明面板穿插；镜头随后转为斜俯视的网页卡片阵列，内容图层抬升、叠放，球体和渐变色块贯穿其中。 |
| [Windows 11：系统界面发布短片](https://www.youtube.com/watch?v=Uh9643c2P6k) | 播放163秒官方发布片，抽查开场、约49秒桌面与约65秒主题选择界面。 | 开场透明晶体沿面板边缘生长；后续笔记本画面呈现居中开始菜单和蓝色壁纸，主题选择器用六宫格缩略图与亮色描边表现选中状态。 |
| [Figma Slides：协作演示界面](https://www.youtube.com/watch?v=p-B--SGq_ZQ) | 播放95秒官方短片，核查约13秒演示编辑器及约43秒精细设计模式。 | 橙色外背景中展示左侧缩略图、中央绿色几何幻灯片、右侧主题面板与底部工具栏；中段选中文字后出现蓝色控制框，右侧转为布局和颜色属性。 |
| [Cuberto：2024 工作室作品集](https://www.youtube.com/watch?v=bK8eUJ65LyY) | 播放128秒合集并跳转中后段，观察授权弹窗、三维图标和网页案例镜头。 | 斜向平板画面中黑色授权卡片与立体指纹/角色图标叠合；随后出现黄色旅行箱和白底网页中的青紫立方体美元符号，包含产品界面与品牌三维图形。 |
| [Shakib：35秒 UI/UX 作品集](https://www.youtube.com/watch?v=_CKnqRhebYg) | 跳过片前广告后播放35秒正片，查看早段三维设计场景并跳转中段手机产品界面。 | 三维手势围绕设计画布与彩色工具图形运动；中段两块圆角手机界面展示紫色耳机、竖向色点选择、黄色数量控件和底部参数区。 |
| [Foundation：科幻游戏 UI 概念](https://www.bilibili.com/video/BV1rT411u7hC) | 打开后观看18秒自动静音播放，比较开场、约13秒目的地选择及结尾任务确认弹窗。 | 发光黑洞开场过渡到金黑星球选择界面，左侧目的地列表、右侧摘要卡、底部FIGHT按钮；结尾展开带徽章、任务列表和OK按钮的横向弹窗。 |
| [UE5：卡通商店、活动与领奖动效](https://www.bilibili.com/video/BV1LHVT6EEW9) | 观看44秒正片的商店、活动主页及约22秒奖励弹窗段。 | 木质商店框架搭配蓝色商品板与卡片；活动主页改为蓝紫星夜背景、环绕角色的任务入口；领奖时黄色斜向横条压在暗化背景上，标题与奖励图标分层出现。 |
| [NAWA / MIX发布：AI 回复卡片动效](https://www.bilibili.com/video/BV125VB6WEYt) | 播放36秒短片，并返回原片复看AI回复卡片的近景与全景。 | 薄荷绿背景上浮出深色圆角社交回复卡片；AI Response区域有绿色描边和流动亮条，近景转全景后可见Approve/Edit按钮；片尾为NAWA标识。 |
| [Lookbook：时装图片悬停](https://tympanus.net/Demos/LookbookHoverEffects) | 打开六张时装图集，分别将指针置于第1和第5张照片。 | 静态为左侧大衬线品牌字与右侧2×3照片网格；指针进入后照片转为钴蓝色卡片，出现大号Look编号、服装说明及细碎的人像轮廓，移出后恢复照片。 |
| [Cinema Seat Preview：影院选座视角](https://tympanus.net/Demos/CinemaSeatPreview) | 等待影院加载，打开Seat map并选择Row F, seat 11, best view。 | 三维红座椅影院正常渲染；选座浮层用弧形座位图、占用颜色和Best view框区分位置；选F11后浮层收起，镜头移至中部座位，屏幕变大，底部显示座位编号和Add/Stand up控件。 |
| [Clip Menu：裁切展开的游戏菜单](https://tympanus.net/Development/EaseReverseClipMenu) | 点击Open menu，观察矩形裁切区域逐步扩至全屏，再点击Close menu收起。 | 黑底漂浮图卡和HUMAN ZERO像素字切换为人像特写背景的全屏菜单；NEW GAME、MISSIONS等七项白色像素文字在裁切区域内显露，关闭时矩形边界向内收缩。 |
| [Glass Xylophone：玻璃木琴](https://tympanus.net/Tutorials/Xylophone) | 等待玻璃琴键加载，点击不同位置并沿螺旋琴键连续拖动。 | 淡紫渐变背景上的半透明圆管形成螺旋木琴；划过后多根琴键依次变成青、蓝、紫、粉的高饱和颜色，随后逐渐退回透明材质。 |
| [Thumbnail Flow：缩略图路径展开](https://tympanus.net/Tutorials/MotionPathTransition) | 打开默认演示并点击+ Open，观察缩略图从左下角叠放，经底部弧线移动至右侧列。 | 单张小图展开为中央主图与14张缩略图；移动中图卡沿弯曲路径接续出现，最终收成右侧竖列，中央保留Close控制。 |
| [SVG Mask：百叶窗图片转场](https://tympanus.net/Tutorials/SVGMaskScrollTransition) | 向下滚动进入第一张建筑图，再继续滚动至第二张图，查看两图交替的中间态。 | 首图为水面上的方形建筑，随后横向条带逐段揭开低矮橙光建筑；转场中上方保留细横线残影，底部三段进度线随滚动推进。 |
| [Maison Orée 概念：黑金界面与刻字聚光](https://tympanus.net/Demos/MuseumOfMotion/vibes/luxury) | 从展项页进入Full page，滚动查看三款首饰、横向图列，并将指针置于刻字戒面。 | 黑金配色、衬线大字与线描首饰形成简洁商品页面；图列延伸到右侧，刻字戒面原为暗金色，指针进入后局部变亮并显露Pour toujours等文字。 |
| [Paper Moon Press 概念：双色印刷与纸张剥离](https://tympanus.net/Demos/MuseumOfMotion/vibes/printed) | 进入Full page，点击SEE THE DRYING RACK，拖走第一张纸，再点击HANG THEM BACK UP。 | 米色纸张背景搭配黑色粗字和蓝粉双色网点海报；拖动时纸张翻出浅色背面，露出下层植物印刷图；重置后月亮海报返回顶层。 |
| [Squoosh：图片前后对比与浮动参数面板](https://squoosh.app) | 打开自带Large photo示例，将Quality滑块调至0，并拖动中央对比分割线。 | 画布两侧呈现同一小熊猫照片，原图清晰、低质量副本出现明显色块；分割线可左右移动，右下压缩率和体积同步更新，设置面板悬浮于图像上。 |
| [Haikei：图形预览与参数编辑工作台](https://app.haikei.app) | 从Wave切换至Blurry Gradient，将第二颜色改为FF8844并点击骰子生成按钮。 | 左侧为带图示的效果选择卡，中间大画布，右侧随类型切换参数；预览从蓝色波形切换到紫绿模糊渐变，再更新为橙绿渐变构图。 |
| [PatternPad：几何纹样编辑器](https://patternpad.com/editor.html) | 打开编辑器，点击 Refresh 并切换 Customize。 | 粉红蓝色几何拼贴完整渲染；刷新后块状组合变化，自定义区展开间距、密度、分割比例设置，图标随后正常加载。 |
| [OKLCH：色域与颜色工作台](https://oklch.com) | 开启 Show 3D，拖动 Hue 色相滑块。 | 颜色从暖黄变成蓝色，色块、代码、色域图与三维色域表面同步变化；黑底圆角分区完整呈现。 |
| [Plausible：公开网站分析仪表盘](https://plausible.io/plausible.io) | 打开官方实时演示，点击来源 Google，再向下浏览数据卡片。 | 深色统计卡、紫色面积折线、来源及页面排名正常显示；点击后顶部出现 Source is Google 筛选标签，页面排名更新。 |
| [Roland50 Studio：电子乐器控制台](https://roland50.studio) | 点击 ENTER，关闭入门说明，点击 TR-808 START。 | 左右双仪器完整出现，黑底橙黄圆点与灰底三角音符矩阵并置；START 变成 STOP，圆点节拍状态变化，底部有拟物旋钮和拨片。 |
| [Music Lab：声音频谱画布](https://musiclab.chromeexperiments.com/spectrogram-service) | 分别选择长笛与鸟鸣内置样本，拖动频谱区域并观察连续画面。 | 黑底中逐步生成紫蓝绿黄色的立体频谱峰，切换样本后谱线密度和峰形变化；底部声源图标高亮。 |
| [Motion：滑动指示器标签页](https://examples.motion.dev/react/smooth-tabs) | 依次点击 Overview、Activity、Settings 标签。 | 白色选中胶囊从左移到中间，卡片由紫色概览图标与统计数字切换成粉色活动图标和另一组数据。 |
| [Motion：轮播与灯箱共享导航](https://examples.motion.dev/react/carousel-lightbox) | 点击照片打开灯箱，再点击 Thumbnail 5。 | 横向黑白骑行照片带进入大图遮罩，底部出现六张缩略图导航及选中描边，原图带在暗化背景中保留。 |
| [Duolingo：官方角色与界面录像](https://framerusercontent.com/assets/RT0g2f4dz5zYO4UphLss616U4.mp4) | 播放 14.4 秒视频并观察前后两段画面。 | 三个倾斜手机同时演示火焰连续学习天数、棋盘答题反馈和紫发角色通话表情；火焰伸缩发光，数字及答题状态变化。 |
| [Spotify Wrapped：官方年度回顾动效录像](https://framerusercontent.com/assets/KzXZgGGMns7LaW6Bz5BAJj7Nw.mp4) | 播放 18 秒官方案例视频，观察初始与约 9 秒画面。 | 绿色场景中四个倾斜手机展示年度听歌数字、同心圆艺人封面、圆点时间图和黑白条纹徽章；内容持续切换并缩放运动。 |

## 数据依据

[完整主库](../library.json) · [旧库原始清单](full-audit-manifest.json) · [旧库逐项审计](full-audit.json) · [新增网站审计](audit-new-sites.json) · [新增展示录像审计](audit-new-videos.json) · [第二轮审计](audit-round2-sites.json) · [第三轮视频审计](audit-video-round3.json)

小红书连接未就绪，未取得可核验笔记，因此没有以搜索摘要补数。第三方网站、图像、视频和代码的权利归原作者；本库只整理入口与参考点。
