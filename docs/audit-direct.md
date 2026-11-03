# Direct demo 实证核查

2026-11-03，IAB 实测54条：53 pass，1 blocked。

逐项加载、观察主体并操作核心交互。pass为功能/视觉核查通过；选品建议独立标识。blocked不是全网坏链。未依赖HTTP200或旧截图判定。

## 1. [https://dmtrbrl.github.io/discography/](https://dmtrbrl.github.io/discography/)

- 结论：pass
- 操作：点击 Next album；比较切换前后截图与专辑标题
- 观察：唱片封面和3D盒体完整显示；由 Yeah Yeah Yeahs / Its Blitz 切换到 IAMX / The Alternative，中央封面与左右排列同步变化。
- 限制：未测试全部专辑或音频。

## 2. [https://gelatin.games/ultrawater](https://gelatin.games/ultrawater)

- 结论：pass
- 操作：等待WebGPU场景加载，使用camera选择器 Lagoon→Underwater
- 观察：海面波纹、岸边焦散与透明水体正常渲染；选择后切到水下视角，可见鱼群、海底与水面折射。
- 限制：初次导航超时后主体正常；未运行性能benchmark。

## 3. [https://ocarina.thibaut-lefrancois.com/](https://ocarina.thibaut-lefrancois.com/)

- 结论：pass
- 操作：二次加载后点击Press Start，按空格/上箭头，并打开Songs面板
- 观察：二次访问成功进入复古像素风木屋和三维陶笛；按键后音符控件高亮，飞行精灵位置改变；Songs打开完整曲目/五线谱面板。
- 限制：首次加载曾卡58%，二次访问恢复。未审听音色或完成整首曲目。

## 4. [https://www.kubai.design/pro-threads/](https://www.kubai.design/pro-threads/)

- 结论：pass
- 操作：将 Text 输入由 PRO 改为 UI，比较两张截图
- 观察：光丝字形从PRO实时变成UI，形状与布局对应输入变化；材质与调参面板完整可见。
- 限制：核验文字生成交互；本轮未确认持续自动流动，不应以此宣称连续动态已测。
- 描述修正：可输入文字生成细密光丝字形，并调整调色板、形状与光照；适合标题与品牌视觉参考。

## 5. [https://instanced-mesh-showcase.vercel.app/](https://instanced-mesh-showcase.vercel.app/)

- 结论：pass
- 操作：等待着色器编译后点击并短按画布
- 观察：飞船穿过大量小行星，前后截图陨石位置变化；短按后可见爆破碎片，Destroyed由1增长至5。
- 限制：WebGPU场景在本环境可运行；没有测试其它renderer或百万实例档。

## 6. [https://phileeppov.com/glass](https://phileeppov.com/glass)

- 结论：pass
- 操作：将Studio预设切换Night
- 观察：玻璃笑脸图标主体完整；预设切换后背景变黑、标志反白，彩色折射纹与材质参数对应变化。
- 限制：未上传私人图片、未使用麦克风。

## 7. [https://dmtrbrl.github.io/leafthrough/](https://dmtrbrl.github.io/leafthrough/)

- 结论：pass
- 操作：点击Next pages，观察翻页中和完成后的截图
- 观察：封面先弯曲翻起，随后完整展开为第2–3页；页码和图文内容同步变化。
- 限制：已验证首个翻页，不代表全部12页与框架变体。

## 8. [https://mrdoob.github.io/slop-newyork/](https://mrdoob.github.io/slop-newyork/)

- 结论：pass
- 操作：等待城市生成后点击Night 23:00
- 观察：纽约街道、出租车、雷达与导航HUD正常显示；日间城市切换夜景，路灯窗光及地面反射相应变化。
- 限制：场景较重，夜景首次切换时HUD显示13FPS；未测全部交通模式。

## 9. [https://greggman.github.io/cyber-web-city/](https://greggman.github.io/cyber-web-city/)

- 结论：pass
- 操作：等待城市与着色器生成，按页面提示C切换相机
- 观察：霓虹楼群、雪粒与飞行汽车实际渲染；C键后由外部追踪视角转入驾驶舱，构图和HUD提示更新。
- 限制：未测试全部主题或手动驾驶。

## 10. [https://r3f-sketch-material.vercel.app/](https://r3f-sketch-material.vercel.app/)

- 结论：pass
- 操作：等待模型加载，点击WASH OUT并观察完成状态
- 观察：汽车、墓碑与THREE JS立体字均以蓝色手绘线条渲染；点击后场景逐步洗去为空白纸面，按钮变为REVEAL。
- 限制：未测试全部画笔/参数组合。

## 11. [https://atelier-north.crnacura.workers.dev/](https://atelier-north.crnacura.workers.dev/)

- 结论：pass
- 操作：点击PROJECTS导航，观察跳转与揭示完成画面
- 观察：奶油底与钴蓝大字首屏完整；导航定位到项目区，标题从重复错位收敛为Selected Works，建筑图像由像素块逐步清晰。
- 限制：虚构工作室界面演示；未测试联系方式。

## 12. [https://amber.isma.uy/](https://amber.isma.uy/)

- 结论：pass
- 操作：待标本加载后点击Show Tyrannosaurus
- 观察：五只恐龙和实验转盘完整呈现；中心三角龙切换为霸王龙，转台排列与Rex.005/Predator档案标题同步更新。
- 限制：未遍历全部档案详情。

## 13. [https://isle-thorne-collective.crnacura.workers.dev/](https://isle-thorne-collective.crnacura.workers.dev/)

- 结论：pass
- 操作：点击Cart(0)打开空购物车
- 观察：家居摄影与克制导航完整呈现；点击后出现空购物车浮层、Visit the shop入口及关闭控制，背景内容尺寸/布局响应。
- 限制：仅演示模板，无下单或真实交易；本次看见的是顶部浮层而非标准侧抽屉。
- 描述修正：虚构家具商店演示：全幅室内摄影、克制导航和产品集合布局，附购物车浮层与内容页面。

## 14. [https://jeantimex.github.io/tokyo/](https://jeantimex.github.io/tokyo/)

- 结论：pass
- 操作：等待城市区块加载后切换写实/抽象模型按钮
- 观察：车站、轨道、建筑与道路密集场景完整可见；点击模式后建筑表面由写实纹理切为浅色抽象块体。
- 限制：初次载入较慢，背景仍可继续加载其余区块；地理数据归属PLATEAU/日本国土地理院/OSM，不宜说全部建筑是随机生成。
- 描述修正：东京城市模型与写实/抽象双模式展示，建筑、铁路和街区构成密集空间层次，适合研究三维地图与材质切换。

## 15. [https://underthesea.wawasensei.dev/](https://underthesea.wawasensei.dev/)

- 结论：pass
- 操作：等待加载完成后点击水面
- 观察：月夜水面、渔夫小舟、成群鱼粒与灯光反射可见；点击水面后渔夫抛竿，HUD进入Casting并出现Lure Cam小窗。
- 限制：初始Gathering the school持续较久后正常加载；未验证最终钓获。
- 描述修正：月夜鱼群与水面反射组成钓鱼场景，点击水面触发抛竿和诱饵镜头，适合研究沉浸式场景与游戏HUD。

## 16. [https://sakura.billpwchan.art/](https://sakura.billpwchan.art/)

- 结论：pass
- 操作：等待入口准备后点击SET SAIL，比较航行两个时间点
- 观察：笔触圆环与樱花入口进入山水河道；小舟前进、水波和灯笼倒影持续变化，标题淡出后主体仍正常。
- 限制：初次入口需较长资源准备；未遍历四季、天气和全部地点。

## 17. [https://smear.niccolofanton.dev/](https://smear.niccolofanton.dev/)

- 结论：pass
- 操作：点击PLAY REEL，观察0.14秒与4.32秒画面
- 观察：WebGPU实时短片由彩色几何物体切换到立体SMEAR排版，播放计时增长，具有可见运动与场景变化。
- 限制：核验短片开头多个状态，未完整观看全部15秒循环。

## 18. [https://aureliengmz.github.io/clearwater/](https://aureliengmz.github.io/clearwater/)

- 结论：pass
- 操作：比较不同时刻画面并点击水面
- 观察：透明水面与海底石块完整，前后截图焦散纹理、波峰及阳光反射显著变化。
- 限制：水面持续动画已确认；本次未单独量化点击涟漪与自然波动的区别。

## 19. [https://aquarium.wawasensei.dev/](https://aquarium.wawasensei.dev/)

- 结论：pass
- 操作：等待玻璃鱼缸场景出现后按Space触发Shatter
- 观察：水族箱、水下地形、灯光与焦散完整可见；Space后前玻璃碎裂飞散、水流向外倾泻，HUD变为Shattered · spilling。
- 限制：未遍历Lab或全部调参。
- 描述修正：带水体焦散和玻璃材质的微缩水族箱，可触发破裂与漏水动画，适合研究材质、物理反馈和场景控件。

## 20. [https://sand.scottsun.io/](https://sand.scottsun.io/)

- 结论：pass
- 操作：等待沙盘渲染，拖动手指从左上至右下
- 观察：细沙、树影与光点正常呈现；拖动后生成明确的凹槽和边缘堆沙阴影，与未绘制画面可直接比较。
- 限制：已核查核心绘制交互，未遍历笔触尺寸。

## 21. [https://nestorrig.github.io/Fluid-Pixel-Cursor-Effect/](https://nestorrig.github.io/Fluid-Pixel-Cursor-Effect/)

- 结论：pass
- 操作：拖动指针经过中央画布
- 观察：黑色点阵背景和像素标题正常；拖动后出现蓝紫像素拖尾，随后衰减。
- 限制：未遍历效果参数。

## 22. [https://saurow-reel.vercel.app/](https://saurow-reel.vercel.app/)

- 结论：pass
- 操作：等待照片加载后滚轮滚动
- 观察：完整照片带出现；滚轮后蛇/蒲公英画面移为蒲公英/天鹅，卡片边缘呈弯曲透视。
- 限制：只核查一段卷轴，未遍历20张。

## 23. [https://emotion-iphone-duo.vercel.app/](https://emotion-iphone-duo.vercel.app/)

- 结论：pass
- 操作：观察闭合状态，操作播放暂停控件
- 观察：手机从单块正面变为铰链展开的双屏，进度从0变为0.531，屏幕内容随透视展开。
- 限制：未上传个人图片，未验证所有预设。

## 24. [https://angelolibero.github.io/liquid-lens/](https://angelolibero.github.io/liquid-lens/)

- 结论：pass
- 操作：观察液态图像轮廓并点击画布
- 观察：熔岩图片在不规则融合轮廓中呈现，前后画面轮廓及图像扭曲明显变化。
- 限制：已确认持续形变；未单独分离点击涟漪与自动运动。

## 25. [https://footballs.nestorrig.com/](https://footballs.nestorrig.com/)

- 结论：pass
- 操作：主页查看球体，进入Demo1 Attractor并拖动指针
- 观察：首页PBR足球主体正常；Demo1载入足球群，移动后聚合球群散开、位置和尺度显著变化。
- 限制：核查主页和Demo1，未逐一检查其余三个Demo。

## 26. [https://dasprinzip.com/tinker/day42/](https://dasprinzip.com/tinker/day42/)

- 结论：pass
- 操作：拖动玻璃环场景
- 观察：透明虹彩圆环、金色立方粒子及地板倒影正常出现，拖动后视角旋转且粒子位置改变。
- 限制：未验证声音，也未逐一分离悬停摇晃效果。

## 27. [https://token-gremlin.github.io/natural-disasters/](https://token-gremlin.github.io/natural-disasters/)

- 结论：pass
- 操作：等候云体编译后观看海浪，按N进入下一幕
- 观察：海面、天空与电影HUD完整；海浪纹理持续变化，按N从Dead Calm进入Sunrise，场景光照与镜头改变。
- 限制：未遍历全部灾害。初始有较长GPU准备时间。

## 28. [https://dasprinzip.com/tinker/day41](https://dasprinzip.com/tinker/day41)

- 结论：pass
- 操作：等待玻璃球载入并拖动旋转
- 观察：梦幻花园背景与蓝色透明球正常出现；拖动后球体经纬线、折射纹理、轮廓朝向改变。
- 限制：未验证声音与所有悬停细节。

## 29. [https://webgpu-glass-material.vercel.app/](https://webgpu-glass-material.vercel.app/)

- 结论：pass
- 操作：等候Shader Ball编译完成后切换Gelatinous Cube
- 观察：默认透明玻璃测试球正常显示折射与色散；切换后出现绿色透明凝胶立方体，内部骨架折射可见。
- 限制：源码按钮目前标注coming soon；不可描述为已有开源源码。未检查Aquarium。

## 30. [https://predator-material.vercel.app/](https://predator-material.vercel.app/)

- 结论：pass
- 操作：查看完整人物材质后点击Pin Cloak
- 观察：森林中的Predator角色完整加载；点击后按钮变Cloak Pinned，后续截图角色从金属实体变为透光折射轮廓。
- 限制：未验证音效。

## 31. [https://spacemagik.github.io/dumplings/](https://spacemagik.github.io/dumplings/)

- 结论：pass
- 操作：等待场景加载，启用Use Chopsticks并拖动画布
- 观察：雨夜暖光餐桌、汤碗、蒸汽和行走的拟人饺子完整；拖动可旋转场景，前后饺子位置和蒸汽明显变化。
- 限制：按钮能切换为Put Down Chopsticks，但未确认成功夹取动作；核心场景运动通过。

## 32. [https://isaac-mason.github.io/the-boiler-room/](https://isaac-mason.github.io/the-boiler-room/)

- 结论：pass
- 操作：等待锅炉房加载并拖动旋转观察
- 观察：暖色手绘锅炉房与黑色煤块小生物完整；拖动后视角从正面变为俯视，生物分布与尘粒变化。
- 限制：实际突出手绘场景与搬煤小生物，并非机械装置的物理运动展示。
- 描述修正：暖色手绘风锅炉房，搬煤的小生物在场景中活动，可拖动查看空间，适合童话插画、场景氛围与群体角色动画参考。

## 33. [https://isaac-mason.github.io/lively-crossing/](https://isaac-mason.github.io/lively-crossing/)

- 结论：pass
- 操作：观察行人并拖动街口视角
- 观察：手绘风城市街口与数十名行人正常加载；后续画面行人持续前进，拖动后镜头转向街树和侧面道路。
- 限制：未验证其他交互；更偏手绘风步行街景，非传统俯视微缩沙盘。
- 描述修正：手绘风城市街口中的群体行走动画，可旋转观察树荫、建筑和行人，适合城市氛围与角色群体运动参考。

## 34. [https://projects.arkon.digital/threejs/wavy-cubes/](https://projects.arkon.digital/threejs/wavy-cubes/)

- 结论：pass
- 操作：比较网格展开前后并拖过画布
- 观察：Franky.dev单页与白色立方网格完整；后续网格方块高度和紫色光影位置改变，指针经过后起伏继续变化。
- 限制：这是作品集式文字页面上的低对比网格动效，非独立全屏彩色几何场景。

## 35. [https://cullenwebber.github.io/three-volumetric-light/](https://cullenwebber.github.io/three-volumetric-light/)

- 结论：pass
- 操作：等待画面加载，观察两帧并拖动画布
- 观察：真实手部模型托起发光点阵，斜向体积光与空气粒子正常；后续画面点阵轮廓、手指姿态及颗粒位置变化。
- 限制：已确认动态画面，拖动是否独立改变镜头未确定。
- 描述修正：手部模型托起发光点阵，结合体积光、浮尘与柔和散射，适合研究产品舞台感和光影氛围。

## 36. [https://dasprinzip.com/tinker/day38/](https://dasprinzip.com/tinker/day38/)

- 结论：pass
- 操作：点击并拖动透明箱体
- 观察：透明立方体内蓝黄软球完整可见；操作后箱体旋转，内部球体重新分布并改变形状，地面反射同步变化。
- 限制：未验证声音；核心软体与箱体运动通过。

## 37. [https://page-transitions-with-webgpu-vanilla-js.crnacura.workers.dev/](https://page-transitions-with-webgpu-vanilla-js.crnacura.workers.dev/)

- 结论：pass
- 操作：首页点击The North Face项目
- 观察：山岳照片卡片完整显示；点击后路由变/3，周边卡片淡出，所选照片留在中央并进入左侧文字详情布局，捕获中间与完成画面。
- 限制：页面有Tutorial外链但主体为可交互演示，未进入教程；本次未遍历所有图片。

## 38. [https://3d-carousel.thibaut-lefrancois.com/](https://3d-carousel.thibaut-lefrancois.com/)

- 结论：pass
- 操作：滚动弯曲照片卡片
- 观察：初始雾中人物卡片显示悬停色散；滚动后切为湖畔房屋和人物卡片，透视弯曲轮廓随位置变化。
- 限制：未逐一遍历图片。

## 39. [https://cullenwebber.github.io/three-particles/](https://cullenwebber.github.io/three-particles/)

- 结论：pass
- 操作：观察两帧并拖动粒子区域
- 观察：彩色粒子团与中央标题正常；后续粒子从紧密团块扩散为多臂结构，球体位置和拖影持续变化。
- 限制：已确认动态粒子；未单独确定拖动与自动动画的贡献。

## 40. [https://gsap-cubic-scrollable-image-gallery.webflow.io/](https://gsap-cubic-scrollable-image-gallery.webflow.io/)

- 结论：pass
- 操作：滚动一次切换图库
- 观察：Reina Takagi背景、立方小图和姓名切为Ayaka Mizuno，立方体移动至上方且图片换面。
- 限制：虽含教程链接，主体为完整视觉演示；未进入教程。

## 41. [https://madewithgsap.com/codrops](https://madewithgsap.com/codrops)

- 结论：pass
- 操作：横向移动指针后观察两帧
- 观察：移动后出现多张图片的指针拖尾，图片下落移出画面，主体文字及Demo控件正常。
- 限制：含站内推广弹窗与教程返回链接，但核心图片重力效果可直接使用。

## 42. [https://palantir-seven.vercel.app/](https://palantir-seven.vercel.app/)

- 结论：pass
- 操作：等待环境贴图后拖动球体区域
- 观察：夕阳荒草地、透明球和环境反射完整；拖动后视角改变，球旁出现橙色发光尾迹及地面照明。
- 限制：未遍历调参；场景较暗但主体可辨。

## 43. [https://imoss.bio/](https://imoss.bio/)

- 结论：pass
- 操作：拖动苔藓球并观察前后帧
- 观察：高密度绿色纤维球完整渲染；拖动后球体位移、旋转和轮廓压缩改变。
- 限制：未遍历纤维数量、长度和颜色参数。

## 44. [https://threejs-video-wall.vercel.app/](https://threejs-video-wall.vercel.app/)

- 结论：pass
- 操作：点击Start，观察启动和连续播放画面
- 观察：Start后出现环状发光方块，随后镜头进入三维矩阵视频墙；两帧视频内容、墙块位置和光照明显改变。
- 限制：需要先点Start，启动空黑不是坏链；未验证音频。

## 45. [https://false-earth.mingjyunhung.com/](https://false-earth.mingjyunhung.com/)

- 结论：pass
- 操作：二次加载完成后Start，按W移动并按C切换镜头
- 观察：宇航员置身银色草海与星空，草叶起伏；按W后角色移动，按C从第三人称切为第一人称，HUD同步改变。
- 限制：首次卡28%，二次完成校准后恢复。不是地球球体或地图展示。
- 描述修正：星空下的银色草海与宇航员探索体验，支持行走和第一/第三人称切换，适合研究动态植被、沉浸场景和镜头设计。

## 46. [https://the-ink-whale.vercel.app/](https://the-ink-whale.vercel.app/)

- 结论：pass
- 操作：等鲸鱼载入后拖动模型
- 观察：白底灰色鲸鱼轮廓正常；拖动后姿态从横向侧面变为竖向俯视，鳍尾位置与描边变化。
- 限制：未确认明显彩色指针墨迹；核心非写实鲸鱼与旋转可用。

## 47. [https://page-transitions-astro-barba-gsap.crnacura.workers.dev/](https://page-transitions-astro-barba-gsap.crnacura.workers.dev/)

- 结论：pass
- 操作：依次点击Works和Team
- 观察：路由及中央标题正确由Index变Works再Team，背景色和页面内容过渡到相应状态。
- 限制：属于极简教学配套转场Demo，每页主要是大标题与credits；视觉成品丰富度低，不应描述成完整作品/团队站。
- 描述修正：极简多页转场试验，以大标题和彩色背景比较页面退出与进入节奏。
- 选品建议（不等于功能失败）：建议从高质量视觉主库移除或降级：主体是教程配套的占位布局，视觉信息量明显低于其他成品。

## 48. [https://gobzzzmusicplayer2024.vercel.app/](https://gobzzzmusicplayer2024.vercel.app/)

- 结论：pass
- 操作：点击下一首歌曲
- 观察：专辑卡片以三维圆环形式显示；点击Next后The Strokes切为Toploader，卡片旋转、标题动画与播放状态同步改变。
- 限制：未审听音频品质，未使用添加自定义歌曲。

## 49. [https://ripple-effect-webgl.vercel.app/](https://ripple-effect-webgl.vercel.app/)

- 结论：blocked
- 操作：分别在中央和左侧花朵图片上拖动指针并检查错误
- 观察：三张花朵图和页面正常，但多次指针移动后的截图未能明确辨认水波折射，不能声称核心特效通过。错误日志为空。
- 限制：当前prefers-reduced-motion=true，是否导致效果弱化未证实；需其他环境复验。

## 50. [https://async-page-transitions.crnacura.workers.dev/](https://async-page-transitions.crnacura.workers.dev/)

- 结论：pass
- 操作：由Home导航至Alternative Page并观察前后状态
- 观察：艺术品数据和超大编号从AH.736变WV.663，进入后标题/信息行完成揭示，路由正确。
- 限制：页面只呈现文字信息与超大编号，本次未见丰富成品界面。
- 选品建议（不等于功能失败）：建议从高质量主库移除或降级：是教程配套的简约转场示例，视觉信息量偏低。

## 51. [https://shoe-finder-wine.vercel.app/](https://shoe-finder-wine.vercel.app/)

- 结论：pass
- 操作：等待球鞋图库载入，点击New Balance品牌筛选
- 观察：球面排列的鞋款缩略图和底部胶囊筛选条完整；点击后Nike图集淡出重排为New Balance图集，捕获过渡与完成状态。
- 限制：商品是带空间布局的图片，不应声称每只鞋均为可旋转三维模型；未发起购买。
- 描述修正：将球鞋图片布置成球面图库，品牌筛选时淡出、重排并替换商品，适合运动电商和探索式商品浏览参考。

## 52. [https://r3f-lusion-portal.vercel.app/](https://r3f-lusion-portal.vercel.app/)

- 结论：pass
- 操作：等空间隧道加载后向下滚动两屏
- 观察：宇航员位于发光网格隧道中央；滚动后紫色灯带转为蓝色，宇航员姿态、喷射光和隧道视角变化。
- 限制：核心滚动驱动场景通过，未验证完整滚动终点。

## 53. [https://r3f-rapier-ball-of-glass.vercel.app/](https://r3f-rapier-ball-of-glass.vercel.app/)

- 结论：pass
- 操作：拖动并点击球体，比较多帧
- 观察：透明多边形拼片组成单个球体；拖动后球体转向且局部拼片轮廓变形，再次观察趋于完整球形。
- 限制：不是多个独立玻璃球的聚合；未使用设备运动权限。
- 描述修正：由透明多边形拼片组成的玻璃球，指针交互带来旋转、扰动和复位，适合折射材质与物理反馈参考。

## 54. [https://pixelimageeffect.pages.dev/](https://pixelimageeffect.pages.dev/)

- 结论：pass
- 操作：从首屏向下滚动一屏并比较揭示前后
- 观察：北方探险编辑式图文首页完整；滚入下一组照片先出现黑白大像素块，随后还原为营地和山谷的清晰图片。
- 限制：教程仅为外链，主体为可直接体验的照片揭示Demo；未遍历全部详情页。
