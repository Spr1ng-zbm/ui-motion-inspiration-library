# 现库实际体验核验

2026-11-03 使用后台 IAB 打开页面并检查真实截图。仅记录已实际观察到的内容；不将 HTTP 200 或 DOM 文案当作效果可用证据。

|原条目|决定|观察结果|建议主链接|
|---|---|---|---|
|[Motion App Store](https://motion.dev/examples/react-app-store)|保留，替换主链接|初始四卡网格可见；点击旅行卡标题后成功展开中央详情卡，图片、详情及背景遮罩均可见。预览免费，源码收费。|[直接演示](https://examples.motion.dev/react/app-store)|
|[Motion Coverflow](https://motion.dev/examples/react-gallery-coverflow)|保留，替换主链接|文档内iframe最初为暗色占位，独立预览正常显示12张彩色冰棒图片及透视排列。未测试拖拽/轮播。预览免费，源码收费。|[直接演示](https://examples.motion.dev/react/gallery-coverflow)|

浏览器交接后暂停实际浏览核验。其余静态检查另存，不能混同实际效果验证。

## 静态补查（不属于实际效果通过）

`experience_static_gate.json` 记录29个原链接的静态HTML事实，17个60fps详情包含公开的 `<video><source>` 及视频封面。17个主要MP4源的HEAD请求均返回200与 `video/mp4`，体积约152KB–3.2MB。页面正文未发现观看解锁提示；出现的 `unlock` / `sign in` 属于相关案例标题。仍须实际浏览器验证播放，不因HTTP200判定体验通过。

- [Aceternity Container Scroll](https://ui.aceternity.com/components/container-scroll-animation) 的官方链接公开了[独立预览](https://ui.aceternity.com/live-preview/container-scroll-animation-demo)，待实际核验后可替换主链接。
- [MagicUI Animated Beam](https://magicui.design/docs/components/animated-beam) 的HTML公开了[官方效果视频](https://cdn.magicui.design/animated-beam.mp4)，尚未观看。
- [Kokonut Slide to Confirm](https://kokonutui.com/docs/buttons/slide-to-confirm)、[Detent Dial](https://kokonutui.com/docs/inputs/detent-dial)、[Liquid Gauge](https://kokonutui.com/docs/cards/liquid-gauge) 都是内联组件文档，未发现公开独立iframe/预览链接，不应捏造路径。
- [React Bits Aurora](https://reactbits.dev/backgrounds/aurora) 的静态文本要求JavaScript开启后展示预览，不能通过静态内容证明效果正常。
- [Globe.GL](https://globe.gl/) 首屏主体为库说明及演示索引，建议移除首页条目，改选官方已链接的具体示例，例如[世界人口](https://vasturiano.github.io/globe.gl/example/world-population/)、[海底光缆](https://vasturiano.github.io/globe.gl/example/submarine-cables/)或[昼夜循环](https://vasturiano.github.io/globe.gl/example/day-night-cycle/)，尚未实际验证这些示例。


## 浏览器恢复后的补查

- [https://sonner.emilkowal.ski/](https://sonner.emilkowal.ski/)：点击 Render a toast 后，右下角实际出现Sonner通知卡片；首屏堆叠卡片可见。
- [https://vaul.emilkowal.ski/](https://vaul.emilkowal.ski/)：点击 Open Drawer 后白色底部抽屉展开，顶部灰色背景板缩进及圆角可见。
- [https://kokonutui.com/docs/buttons/slide-to-confirm](https://kokonutui.com/docs/buttons/slide-to-confirm)：真实组件可见；对演示按钮按Enter后滑块到右侧并出现Paying状态，随后复位。未测试鼠标拖拽。
- [https://kokonutui.com/docs/inputs/detent-dial](https://kokonutui.com/docs/inputs/detent-dial)：真实圆形温度旋钮可见，按ArrowRight后21.0°变为21.5°，刻度位置反馈可见。
- [https://kokonutui.com/docs/cards/liquid-gauge](https://kokonutui.com/docs/cards/liquid-gauge)：真实黑白液体储存卡可见；按ArrowUp后72%变为73%、92.2变93.4GB。未测试鼠标波纹。
- [https://reactbits.dev/backgrounds/aurora](https://reactbits.dev/backgrounds/aurora)：首次截图短暂空白，加载后截图实际看到紫蓝绿极光预览及完整控制界面。未测试每种参数。
- [https://magicui.design/docs/components/animated-beam](https://magicui.design/docs/components/animated-beam)：实际看到中心OpenAI图标与周围应用图标连线的预览。截图未捕捉到彩色光束运动，故仅确认预览组件已渲染，未确认动态完整表现。
- [https://ui.aceternity.com/components/container-scroll-animation](https://ui.aceternity.com/components/container-scroll-animation)：独立预览实际看到倾斜3D界面板，PageDown后板面转为正面。无需登录或付费。

17个60fps原链接均已实际打开：截图可见具体App画面，主video均readyState=4、paused=false、currentTime>0，无观看付费遮罩。Airbnb New Intro首次读取为readyState=0，复核后正常。所有条目仅核验可播放及画面，未逐条完整观看。具体时长、画面描述及公开源见JSON。

## 最后三项实测

- [https://www.vantajs.com/](https://www.vantajs.com/)：初始实际看到满屏粉色三角鸟群；第二张截图鸟群已聚成另一形态，说明动态在运行，右侧自定义参数面板也可见。
- [https://atroposjs.com/](https://atroposjs.com/)：实际看到完整紫色森林山峰分层首屏卡片；指针点击装饰logo后卡片框及图层构图发生变化。未测试全部showcase卡片。
- [https://earth.nullschool.net/](https://earth.nullschool.net/)：实际看到亚洲与太平洋区域3D地球，连续两张截图从短粒子形成更长风场流线及气旋，确认动态渲染。

合计30条已有链接完成实际浏览器画面核验。未观察到必须登录或付费才能预览的条目；这不代表源码免费。最推荐的链接清理是将Motion两条及Aceternity一条的主链接替换为已实测独立预览。Globe.GL聚合首页的移除建议来自静态内容审查，未混入30条实际核验记录。
