# 独立演示补充批次 — 2026-11-03

## 范围与核验分级

从 Codrops 官方 Creative Hub 的实际出站链接发现候选，逐个访问原作者部署站；不把教程文章、源码仓库或合集首页当作具体效果。发现来源：

- https://tympanus.net/codrops/hub/all/
- https://tympanus.net/codrops/hub/all/page/2/
- https://tympanus.net/codrops/hub/all/page/3/

检查71个候选HTTP入口。提交54条候选，其中13条浏览器截图见到主体画面，其余仅HTTP和页面信息核验，不能称为已经实测有效。实际交互未完整测试。

逐项真实GET保存在 direct_http_audit.json。HTTP 200不等于动态代码正常；verification和visual_verified严格区分。

浏览器抽检后开启多个GPU场景出现CDP截图及导航超时，因此后续候选没有伪称浏览器通过；主库可以只合并visual_verified为true的条目，其余进入待复核候选。

## 浏览器实际画面通过

- [Discography：唱片式专辑浏览](https://dmtrbrl.github.io/discography/)：专辑封面与唱片盒画廊已渲染。
- [PRO Threads：光丝文字壁纸](https://www.kubai.design/pro-threads/)：光丝文字画面与设置面板已渲染；第三方赞助脚本报错不影响已见主体。
- [Glass：液态玻璃图标](https://phileeppov.com/glass)：玻璃图标与折射控制面板已渲染。
- [LeafThrough：纸张翻阅](https://dmtrbrl.github.io/leafthrough/)：纸张封面、页码与翻页控件已渲染。
- [Atelier North：建筑工作室界面](https://atelier-north.crnacura.workers.dev/)：建筑工作室首屏大字体与导航已渲染。
- [Amber Genetics：恐龙标本转盘](https://amber.isma.uy/)：等待资源后五件恐龙转盘与档案界面已渲染。
- [Isle Thorne：家居电商展示](https://isle-thorne-collective.crnacura.workers.dev/)：全幅家具照片和导航已渲染。
- [Fluid Pixel Cursor：像素流体光标](https://nestorrig.github.io/Fluid-Pixel-Cursor-Effect/)：像素点阵和标题已渲染；未完成鼠标轨迹交互核验。
- [Reel Flux：立体照片卷轴](https://saurow-reel.vercel.app/)：三张照片与卷轴浏览首屏已渲染。
- [Liquid Lens：液态透镜](https://angelolibero.github.io/liquid-lens/)：流体透镜、图片和设置界面已渲染。
- [3D Carousel：弯曲照片轮播](https://3d-carousel.thibaut-lefrancois.com/)：等待资源后弯曲照片轮播已渲染。
- [Ripple：图像水纹悬停](https://ripple-effect-webgl.vercel.app/)：等待资源后花卉图片已渲染；未完成悬停交互核验。
- [Pixel Scroll：图片像素揭示](https://pixelimageeffect.pages.dev/)：滚动后已见图像像素揭示画面。

## 仅HTTP与页面内容核验候选

- [Gelatin Water：实时水体](https://gelatin.games/ultrawater) — GET 200，尚未浏览器实测。
- [Ocarina：陶笛音乐交互](https://ocarina.thibaut-lefrancois.com/) — GET 200，尚未浏览器实测。
- [Asteroid Field：小行星群穿行](https://instanced-mesh-showcase.vercel.app/) — GET 200，尚未浏览器实测。
- [Slop New York：城市漫游界面](https://mrdoob.github.io/slop-newyork/) — GET 200，尚未浏览器实测。
- [Cyber Web City：霓虹城市](https://greggman.github.io/cyber-web-city/) — GET 200，尚未浏览器实测。
- [Sketch Material：手绘材质](https://r3f-sketch-material.vercel.app/) — GET 200，尚未浏览器实测。
- [Procedural Tokyo：程序化东京](https://jeantimex.github.io/tokyo/) — GET 200，尚未浏览器实测。
- [Under the Sea：鱼群水下世界](https://underthesea.wawasensei.dev/) — GET 200，尚未浏览器实测。
- [Sakura Fantasy：樱花幻想](https://sakura.billpwchan.art/) — GET 200，尚未浏览器实测。
- [Smear Frames：拖影运动短片](https://smear.niccolofanton.dev/) — GET 200，尚未浏览器实测。
- [Clearwater：清澈水面](https://aureliengmz.github.io/clearwater/) — GET 200，尚未浏览器实测。
- [Aquarium：交互水族箱](https://aquarium.wawasensei.dev/) — GET 200，尚未浏览器实测。
- [Sandboard：可交互沙面](https://sand.scottsun.io/) — GET 200，尚未浏览器实测。
- [iPhone Duo：折叠产品概念](https://emotion-iphone-duo.vercel.app/) — GET 200，尚未浏览器实测。
- [Footballs in Motion：足球材质展示](https://footballs.nestorrig.com/) — GET 200，尚未浏览器实测。
- [Volatile Nexus：玻璃环与方块](https://dasprinzip.com/tinker/day42/) — GET 200，尚未浏览器实测。
- [ABYSSAL：极端海况模拟](https://token-gremlin.github.io/natural-disasters/) — GET 200，尚未浏览器实测。
- [Garden Anomaly：玻璃气泡花园](https://dasprinzip.com/tinker/day41) — GET 200，尚未浏览器实测。
- [WebGPU Glass：玻璃材质演示](https://webgpu-glass-material.vercel.app/) — GET 200，尚未浏览器实测。
- [Predator Cloak：隐形折射材质](https://predator-material.vercel.app/) — GET 200，尚未浏览器实测。
- [Ramen Dumplings：汤碗物理场景](https://spacemagik.github.io/dumplings/) — GET 200，尚未浏览器实测。
- [The Boiler Room：机械物理空间](https://isaac-mason.github.io/the-boiler-room/) — GET 200，尚未浏览器实测。
- [Lively Crossing：街口微缩场景](https://isaac-mason.github.io/lively-crossing/) — GET 200，尚未浏览器实测。
- [3D Wave Grid：立方体波浪](https://projects.arkon.digital/threejs/wavy-cubes/) — GET 200，尚未浏览器实测。
- [Volumetric Light：体积光空间](https://cullenwebber.github.io/three-volumetric-light/) — GET 200，尚未浏览器实测。
- [Boing-boing Box：弹性盒子](https://dasprinzip.com/tinker/day38/) — GET 200，尚未浏览器实测。
- [WebGPU：页面形变转场](https://page-transitions-with-webgpu-vanilla-js.crnacura.workers.dev/) — GET 200，尚未浏览器实测。
- [Three Particles：粒子文字](https://cullenwebber.github.io/three-particles/) — GET 200，尚未浏览器实测。
- [CMS Cube Gallery：立方体图集](https://gsap-cubic-scrollable-image-gallery.webflow.io/) — GET 200，尚未浏览器实测。
- [Gravity Trail：重力图片轨迹](https://madewithgsap.com/codrops) — GET 200，尚未浏览器实测。
- [Palantir：球面轨迹透镜](https://palantir-seven.vercel.app/) — GET 200，尚未浏览器实测。
- [iMoss：数字苔藓球](https://imoss.bio/) — GET 200，尚未浏览器实测。
- [Video Wall：三维视频墙](https://threejs-video-wall.vercel.app/) — GET 200，尚未浏览器实测。
- [False Earth：程序化地球](https://false-earth.mingjyunhung.com/) — GET 200，尚未浏览器实测。
- [Ink Whale：线描鲸鱼](https://the-ink-whale.vercel.app/) — GET 200，尚未浏览器实测。
- [Astro Barba：连续页面转场](https://page-transitions-astro-barba-gsap.crnacura.workers.dev/) — GET 200，尚未浏览器实测。
- [Music Player：立体播放列表](https://gobzzzmusicplayer2024.vercel.app/) — GET 200，尚未浏览器实测。
- [Async Transitions：异步页面转场](https://async-page-transitions.crnacura.workers.dev/) — GET 200，尚未浏览器实测。
- [Shoe Finder：球鞋浏览界面](https://shoe-finder-wine.vercel.app/) — GET 200，尚未浏览器实测。
- [Portal：滚动空间穿越](https://r3f-lusion-portal.vercel.app/) — GET 200，尚未浏览器实测。
- [Glass Attraction：玻璃球聚合](https://r3f-rapier-ball-of-glass.vercel.app/) — GET 200，尚未浏览器实测。

## 未收录候选与原因

- [Smash Your Pumpkin](https://lucaargentieri.github.io/smash-your-pumpkin/)：游戏为主，与本轮UI优先方向较弱。
- [Haunted Pumpkin](https://halloween-2026-iota.vercel.app/)：游戏为主，与本轮UI优先方向较弱。
- [Random-eyes · a digital eye configurator](https://random-eyes.vercel.app/)：浏览器截图只显示HUD与黑色主体，未证实眼球成功渲染。
- [Ocean — WebGPU](https://ocean-noniv.vercel.app/)：真实GET返回429 Vercel Security Checkpoint。
- [Interlude · Astro starter for page transitions](https://interlude.crnacura.workers.dev/)：转场合集索引，不作为具体效果重复计数。
- [Tidewater](https://dgreenheck.github.io/tidewater/)：游戏为主，初始化提示着色器需要较长时间。
- [Experiment 001](https://experiment-001.madebyhex.workers.dev/)：摄像头人脸效果需要权限，本轮不收录。
- [Dreamfold — bend a real city over your head](https://cityfold.vercel.app/)：首次需要用户提供Cesium API key。
- [Three.js Experience](https://codrops-demo-for-threejs-conference-ten.vercel.app/)：游戏为主，与本轮UI优先方向较弱。
- [Skate Dog](https://skate-dog.vercel.app/)：游戏为主，与本轮UI优先方向较弱。
- [SNOWFLOW](https://snowflow-lilac.vercel.app/)：严格依赖WebGPU的滑雪游戏，兼容性未验证。
- [Threejs-Punk Drive | Cyberpunk driving game in WebGPU & Three.js by Anderson Mancini and Sunag](https://threejspunk.vercel.app/)：驾驶游戏，不以UI效果为主。
- [Easy Bugs](https://bandinopla.github.io/threejs-easybugs/)：引擎式小实验，与本轮审美与UI需求较弱。
- [John & Particia's Comfort Space](https://john-and-patricias-comfort-site-about-attachment-styles.com/)：关系主题沉浸空间，与本轮方向较弱。
- [HTML in Canvas Demo](https://html-in-canvas.vercel.app/)：实验性HTML-in-Canvas的索引入口，非单一效果。
- [x-challenge-geo](https://x-challenge-geo.vercel.app/)：内容不足以确认高质量具体效果。
- [crashcat - javascript 3d rigid body physics](https://crashcat.dev/)：物理引擎首页，避免文档型入口。

## 其他拒绝/限制记录

- Codrops Hub和Development/HoverGrid在curl得到200但标题是“Just a moment… | Codrops”，没有把挑战页当作有效演示；主代理另做浏览器核验。
- CodePen临时live preview候选跳到编辑/升级入口，未收录。
- 资源版权归各作者；这里只保存索引、原创简述和官方缩略图URL。
