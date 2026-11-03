# React Bits：减少动画偏好对 13 项预览的影响

核实时间：2026-11-03。此文件来自官方公开源码、线上公开 registry 和媒体响应的只读研究；未使用浏览器，没有把源码逻辑或 HTTP 成功当作本轮画面核验通过。

**Aurora 的静止渐变、指针无反应，以及 Shiny Text 默认只见灰字，都能由官方源码中的无障碍降级解释，不能据此认定网站损坏。** 但不是所有 13 项都会完全静止：Balatro 仍以较慢速度运行，多个组件仍允许手动交互。

## 证据版本

官方仓库固定提交：[4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4](https://github.com/DavidHDev/react-bits/tree/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4)。通过 GitHub tree API 发现真实路径后读取组件与 Demo 源码，不猜演示路由。

还读取了线上 `reactbits.dev/r/<组件>-JS-CSS.json`：13 个 registry 中的 JSX 与该提交对应 JSX 去除首尾空白后逐字相同。因此这里不是仅依赖陈旧仓库代码。此比对证明线上分发源码一致，不声称反向证明所有已部署 JavaScript chunk 的版本。

## 逐项影响

| 组件 | 系统偏好为 reduce 时的明确逻辑 | 核查时应怎样解释 | 官方源码与线上分发 |
|---|---|---|---|
| Aurora | 时间步进乘零；指针参与条件要求不处于 reduce；跳过入场。 | 静止彩色图案且指针无反应属于预期降级。不能声称已验证原始动态极光。 | [读取与渲染分支](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Aurora/Aurora.jsx#L292-L373) · [线上 registry](https://reactbits.dev/r/Aurora-JS-CSS.json) |
| Split Text | 直接设置 ready、调用完成回调并返回，不进入文字拆分动画。 | “Animation Finished” 立即出现只能证明降级完成回调，不能证明逐字入场已播放。 | [提前返回](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/TextAnimations/SplitText/SplitText.jsx#L113-L123) · [线上 registry](https://reactbits.dev/r/SplitText-JS-CSS.json) |
| Blur Text | 外层 MotionConfig 采用 user 策略。 | Motion 官方说明该策略禁用位移/布局运动，其他如透明度仍可能变化；不能把整个组件笼统称为完全静止。 | [配置](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/TextAnimations/BlurText/BlurText.jsx#L372-L394) · [线上 registry](https://reactbits.dev/r/BlurText-JS-CSS.json) · [Motion 语义](https://motion.dev/docs/react-motion-config#reducedmotion) |
| Shiny Text | 默认循环、进入视口触发及 hover 触发要求不处于 reduce；无活动光带时渲染纯色渐变。 | 默认灰字符合降级。页面已有 Follow Pointer 手动模式，该分支没有 reduce 条件，可单独尝试验证手动扫光，不能冒充默认自动循环。 | [纯色渲染](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/TextAnimations/ShinyText/ShinyText.jsx#L156-L177) · [手动与自动分支](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/TextAnimations/ShinyText/ShinyText.jsx#L211-L312) · [线上 registry](https://reactbits.dev/r/ShinyText-JS-CSS.json) |
| Scroll Float | GSAP 滚动时间线仅在 no-preference 媒体查询内创建。 | 在 reduce 下滚动只看到正常文字而没有拉伸/浮起，不应判为故障。 | [媒体查询](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/TextAnimations/ScrollFloat/ScrollFloat.jsx#L131-L151) · [线上 registry](https://reactbits.dev/r/ScrollFloat-JS-CSS.json) |
| Circular Gallery | 自动滚动和波动被关闭；滚动与展开的跟随系数直接取 1；入场直接完成。 | 仍可手动换图/滚动，但会立即响应，不能用缺乏惯性判坏。 | [波动禁用](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Components/CircularGallery/CircularGallery.jsx#L547) · [自动与跟随](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Components/CircularGallery/CircularGallery.jsx#L692-L711) · [线上 registry](https://reactbits.dev/r/CircularGallery-JS-CSS.json) |
| Stack | 使用 useReducedMotion；甩出时立即改变卡片顺序；拖拽倾斜取消；部分过渡简化为短淡变。 | 手动换卡仍可检验，但飞出轨迹和倾斜不会照常出现。 | [简化过渡](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Components/Stack/Stack.jsx#L166-L169) · [立即换序](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Components/Stack/Stack.jsx#L234-L244) · [倾斜分支](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Components/Stack/Stack.jsx#L310-L321) · [线上 registry](https://reactbits.dev/r/Stack-JS-CSS.json) |
| Infinite Menu | 自动轮播条件要求不处于 reduce；入场很快完成，传入着色器的 spin 值为零。手动拖拽状态仍参与帧更新。 | 应测试手动球面导航，不能把无自动转动视为全部失效。 | [手动与自动](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L578-L621) · [spin 分支](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Components/InfiniteMenu/InfiniteMenu.jsx#L663) · [线上 registry](https://reactbits.dev/r/InfiniteMenu-JS-CSS.json) |
| Threads | 自动时间推进停止；指针、分开线条的位置插值仍更新。 | 不能以时间不流动判坏；应实际移动指针查看对应手动反馈。 | [帧更新和指针](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Threads/Threads.jsx#L428-L474) · [线上 registry](https://reactbits.dev/r/Threads-JS-CSS.json) |
| Iridescence | 自动相位停止；指针搅动和点击旋涡被禁用；鼠标位置、光泽/存在感相关值仍可跟随。 | 不能声称全部鼠标反馈关闭；也不能期待点击生成旋涡。 | [帧更新](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Iridescence/Iridescence.jsx#L393-L415) · [指针与点击限制](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Iridescence/Iridescence.jsx#L431-L459) · [线上 registry](https://reactbits.dev/r/Iridescence-JS-CSS.json) |
| Ballpit | 关闭入场、漂移游走和点击 burst；抓取释放的速度传递代码仍存在，没有被 reduce 分支跳过。 | 仍应检验球体的直接操作；不能因无自动漂移把整个物理球池判静态。 | [漂移归零](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Ballpit/Ballpit.jsx#L734) · [抓取释放与 burst](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Ballpit/Ballpit.jsx#L1091-L1114) · [线上 registry](https://reactbits.dev/r/Ballpit-JS-CSS.json) |
| Orb | 时间、旋转、正常 hover 区域与点击 pulse 被抑制；入场直接完成。 | 静止球体属于降级。Force Hover State 是具体状态预览，不等于系统偏好覆盖。 | [帧分支](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Orb/Orb.jsx#L404-L442) · [点击分支](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Orb/Orb.jsx#L480) · [线上 registry](https://reactbits.dev/r/Orb-JS-CSS.json) |
| Balatro | 自动流动/旋转速度变为 20%，指针搅动强度变为 40%，点击旋涡禁用。 | **不是完全静态**；仍应观察慢速运动，不能把无运动全归因于 reduce。 | [速度与搅动比例](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Balatro/Balatro.jsx#L405-L440) · [点击分支](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/content/Backgrounds/Balatro/Balatro.jsx#L560) · [线上 registry](https://reactbits.dev/r/Balatro-JS-CSS.json) |

## 页面上有没有“忽略减少动画”开关

读取了上述 13 个 `src/demo/...Demo.jsx`，没有发现向组件传入的系统偏好覆盖开关。多数目标组件在内部直接读取媒体查询，其公开参数也没有此覆盖选项。Pause、Mouse Interaction、Intro 等控件不能被当成忽略 reduce 的开关。

Shiny Text 有一个有用且不同的现成手动模式：[Demo 中的 Follow Pointer 控件](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/demo/TextAnimations/ShinyTextDemo.jsx#L243-L259)。源码的跟随指针分支没有 reduce 守卫，因此可通过原页面控件尝试它；仍必须以实际画面确认，不以源码推断替代操作。

没有找到可以据实宣称“绕开该媒体偏好”的独立预览路由。没有修改系统、浏览器媒体设置、网站运行代码，也没有尝试猜测路由。

## 官方现成演示录像：13 项都有

官方 [Information.js 的 videoUrl 元数据](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js) 明确给出这些素材路径；[ComponentList 的媒体代码](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/components/common/ComponentList.jsx#L705-L746) 为同名 WebM 和 MP4 提供 source。这些链接来自官方源码，不是猜测。

下列 13 个 MP4 均已只读 HEAD 确认返回 HTTP 200、Content-Type video/mp4。**尚未实际播放；不能写成“录像已通过”。** 可让主代理在浏览器直接打开并播放。如果最终以录像替代受限现场预览，条目应标为视频，并保留原组件页作为来源/实现入口，不能把录像标为可交互演示。

| 效果 | 官方录像 | 元数据行 |
|---|---|---|
| Aurora | [MP4](https://reactbits.dev/assets/video/aurora.mp4) | [1796](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L1796) |
| Split Text | [MP4](https://reactbits.dev/assets/video/splittext.mp4) | [763](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L763) |
| Blur Text | [MP4](https://reactbits.dev/assets/video/blurtext.mp4) | [538](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L538) |
| Shiny Text | [MP4](https://reactbits.dev/assets/video/shinytext.mp4) | [748](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L748) |
| Scroll Float | [MP4](https://reactbits.dev/assets/video/scrollfloat.mp4) | [703](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L703) |
| Circular Gallery | [MP4](https://reactbits.dev/assets/video/circulargallery.mp4) | [1182](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L1182) |
| Stack | [MP4](https://reactbits.dev/assets/video/stack.mp4) | [1663](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L1663) |
| Infinite Menu | [MP4](https://reactbits.dev/assets/video/infinitemenu.mp4) | [1384](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L1384) |
| Threads | [MP4](https://reactbits.dev/assets/video/threads.mp4) | [2542](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L2542) |
| Iridescence | [MP4](https://reactbits.dev/assets/video/iridescence.mp4) | [2232](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L2232) |
| Ballpit | [MP4](https://reactbits.dev/assets/video/ballpit.mp4) | [1826](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L1826) |
| Orb | [MP4](https://reactbits.dev/assets/video/orb.mp4) | [2377](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L2377) |
| Balatro | [MP4](https://reactbits.dev/assets/video/balatro.mp4) | [1811](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/constants/Information.js#L1811) |

注意：官网列表内的视频悬停预览本身也会尊重减少动画偏好。[usePreviewMediaAllowed](https://github.com/DavidHDev/react-bits/blob/4dc7b5b7772e1217c8fb8d2a7aa074302180e5b4/src/hooks/usePreviewMediaAllowed.js#L5-L13) 要求精确指针、非减少动画、非受限连接。所以“列表缩略图不播放”同样不能推导出媒体文件坏掉；应直接打开已发现的媒体 URL，用浏览器播放控件核验。

## 推荐给本轮核查的判定方式

- 现场预览只有降级静态状态：写明“静态降级正常，完整动画受测试环境偏好限制”，不要写“网站失效”，也不要写“动效已通过”。
- 尚可手动交互的项目：按表中对应动作实查并收窄通过范围；不自动提升为全部动画通过。
- 官方录像实际播放通过：可保留视频参考，但需准确标注录像与现场演示的差别。
- 若主体空白、GPU 报错或资源失败，仍独立处理，不能把所有问题归给 reduce。尤其 Balatro 在该偏好下仍有慢速自动运动。
