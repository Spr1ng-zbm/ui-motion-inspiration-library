# 第七轮 UI 与动效候选研究

日期：2026-11-03。仅来源研究，无浏览器实测通过结论。

新增 35 条，其中 15 条移动端具体录像，其余为独立互动/电商/空间作品与数据可视化界面。全部与生成时 candidate*.json + library.json 按 canonical_url 去重；移动录像另核对 preview_url，避免同一片段换页重复。

## 研究方法与质量边界

- 移动片段由 60fps 发布，逐一读取作品正文与首个 video/source；本轮检查的 24 个对应 MP4 的 HEAD 均返回 200、video/mp4，剔除生成前已进入主库的 9 条。没有下载或播放录像。60fps 是记录者，不能把其描述当作 App 厂商承诺；待实际观察后仍可能需要纠正描述。
- FWA 官方公开项目数据提供具体作品直链；核对原站标题、正文或明确的脚本入口。一般宣传页 Alethia 暂排除，Brunello Cucinelli 返回拒绝访问，未凑数添加。
- 数据方向选作品本体：天气与电力地图、电影关系交互、菜单档案、文字地图和音乐时间线；没有收通用图表库、教程或目录。
- Electricity Maps 命令行 GET 403，公开页面读取工具能看到地图/侧栏与碳强度图例；仍未确认地图主体可运行，单独标明。Gucci 活动入口只有脚本壳，当前体验可用性待核查。
- Dialed 使用首页实际链接 `/color`，不把七种游戏目录作为条目。其余场景切换/图表能力只按官方作品说明概括，未冒充观察结果。

## 分类

- App 微交互：15
- 游戏与交互体验：5
- 品牌与产品界面：3
- 数据可视化：8
- 画廊与导航：3
- 作品集与展示：1

## 条目与待核查动作

### 1. Runmo：心电波形与发光游标

[作品入口](https://60fps.design/shots/runmo-lab-pulse-heart-ecg-interaction) · [来源](https://60fps.design/shots/runmo-lab-pulse-heart-ecg-interaction)

深色生物指标网格上，心电曲线与发光游标循环运动，周围指标保持布局。

待核查：实际播放并拖动进度；观察波形绘制、游标脉冲及仪表信息层级。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/6a9e9ba32f578a19ae2569ae/main.mp4)：HEAD 200，video/mp4，未播放。

### 2. Runmo：跑步里程环形旋钮

[作品入口](https://60fps.design/shots/runmo-drag-to-adjust-distance-wheel-interaction) · [来源](https://60fps.design/shots/runmo-drag-to-adjust-distance-wheel-interaction)

里程设置用环形刻度拖动更新数值，确认后结合目标进度弧显示状态。

待核查：实际播放并拖动进度；观看拖动和确认两个阶段，检查数值与进度弧的联动。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/6a9e9bb52f578a19ae256a7a/main.mp4)：HEAD 200，video/mp4，未播放。

### 3. CRED：票券打印与重排

[作品入口](https://60fps.design/shots/cred-printing-tickets-shuffle-interaction) · [来源](https://60fps.design/shots/cred-printing-tickets-shuffle-interaction)

票券从打印状态出现，错落排列成卡片组，同时显示倒计时和确认反馈。

待核查：实际播放并拖动进度；确认打印、卡片重排及倒计时入场；不把页面描述替代具体观察。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/6ac725a341d1f14ce09740f1/main.mp4)：HEAD 200，video/mp4，未播放。

### 4. Revolut：虚拟卡光泽扫过

[作品入口](https://60fps.design/shots/revolut-single-use-pulse-card-sweep-morph-animation) · [来源](https://60fps.design/shots/revolut-single-use-pulse-card-sweep-morph-animation)

一次性虚拟卡片段通过深色光晕和金属反光扫过卡面，再回到白色界面。

待核查：实际播放并拖动进度；观察光晕、反光与恢复静止状态的完整周期。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/6a9e9ba2aa4fda34666693d5/main.mp4)：HEAD 200，video/mp4，未播放。

### 5. Duolingo：能量奖励飞入计数器

[作品入口](https://60fps.design/shots/duolingo-battery-fill-up-interaction) · [来源](https://60fps.design/shots/duolingo-battery-fill-up-interaction)

能量电池奖励先弹出，再缩小沿弧线飞向顶部计数器并触发数字反馈。

待核查：实际播放并拖动进度；确认奖励弹出、飞行路径、计数器回弹与数字变化。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/6a9e9ba2aa4fda34666693d3/main.mp4)：HEAD 200，video/mp4，未播放。

### 6. Trackables：指标卡扩展为详情

[作品入口](https://60fps.design/shots/trackables-card-morph-to-screen-interaction) · [来源](https://60fps.design/shots/trackables-card-morph-to-screen-interaction)

仪表盘指标卡使用共享元素过渡，展开为全屏详情视图。

待核查：实际播放并拖动进度；观察卡片边缘、数字与图表向详情页的衔接，以及返回过程。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/6a6639212a11e67b17323e97/main.mp4)：HEAD 200，video/mp4，未播放。

### 7. X：股票曲线与蜡烛图切换

[作品入口](https://60fps.design/shots/x-stock-graph-interaction) · [来源](https://60fps.design/shots/x-stock-graph-interaction)

股票图表片段包含曲线变化、沿线读取数据与底部面板内的图表类型切换。

待核查：实际播放并拖动进度；观察曲线拖动、数据提示与蜡烛图切换的具体过程。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/69e48b4ed04993c17ee2b5f9/main.mp4)：HEAD 200，video/mp4，未播放。

### 8. Habitastic：打卡标尺时间线

[作品入口](https://60fps.design/shots/habitastic-daily-check-in-timeline-scroll-interaction) · [来源](https://60fps.design/shots/habitastic-daily-check-in-timeline-scroll-interaction)

横向标尺式时间线让用户浏览每日打卡历史，滚动中切换日期状态。

待核查：实际播放并拖动进度；确认时间线吸附、日期变化与对应打卡信息。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/693434657d19d070282a0479/main.mp4)：HEAD 200，video/mp4，未播放。

### 9. Methods：对比柱形图入场

[作品入口](https://60fps.design/shots/methods-compare-bar-animation) · [来源](https://60fps.design/shots/methods-compare-bar-animation)

引导页面用动态增长的对比柱形图表达数值差异。

待核查：实际播放并拖动进度；观察柱体增长、数值标注及最终对比状态。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/694c0d18e086c47a8222cef1/main.mp4)：HEAD 200，video/mp4，未播放。

### 10. Methods：滑杆联动收益柱图

[作品入口](https://60fps.design/shots/methods-payout-slider-interaction) · [来源](https://60fps.design/shots/methods-payout-slider-interaction)

调整收益滑杆时，柱形图尺寸与文字数值同步更新。

待核查：实际播放并拖动进度；确认滑杆输入、图形高度与数值响应的关系。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/694c0d18f1ad267a0647ebec/main.mp4)：HEAD 200，video/mp4，未播放。

### 11. Spotify Wrapped：歌手排名竞速

[作品入口](https://60fps.design/shots/spotify-2025-wrapped-artist-race-animation) · [来源](https://60fps.design/shots/spotify-2025-wrapped-artist-race-animation)

歌手排名以竖向竞速与圆形拖影呈现，最后过渡到总结卡。

待核查：实际播放并拖动进度；播放完整排名变换，确认拖影、排序和最终卡片。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/6934008e7d19d07028262457/main.mp4)：HEAD 200，video/mp4，未播放。

### 12. Harvee：点阵与环图时间范围切换

[作品入口](https://60fps.design/shots/harvee-tab-switch-graph-morph-interaction) · [来源](https://60fps.design/shots/harvee-tab-switch-graph-morph-interaction)

时间范围标签切换时，点阵图案和环形图动态重组为新状态。

待核查：实际播放并拖动进度；观察标签切换前后图表与数值的连续变化。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/69171d15df9720847e0ac8c9/main.mp4)：HEAD 200，video/mp4，未播放。

### 13. The Outsiders：睡眠阶段图表横移

[作品入口](https://60fps.design/shots/the-outsiders-sleep-stages-graph-slide-interaction) · [来源](https://60fps.design/shots/the-outsiders-sleep-stages-graph-slide-interaction)

分层睡眠阶段图通过横向拖动与吸附显示对应时间提示。

待核查：实际播放并拖动进度；观察横向拖动、选中位置与提示框内容变化。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/68f080a7befe20b134b9fd4a/main.mp4)：HEAD 200，video/mp4，未播放。

### 14. Lumy：时间滑杆与太阳轨道

[作品入口](https://60fps.design/shots/lumy-time-slider-interaction) · [来源](https://60fps.design/shots/lumy-time-slider-interaction)

时间滑杆驱动天空颜色过渡与太阳图标沿轨道移动。

待核查：实际播放并拖动进度；核对滑杆位置、天空配色及太阳轨道的对应变化。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/68e71806e76d5c62e6f6decf/main.mp4)：HEAD 200，video/mp4，未播放。

### 15. Family：流体价格曲线与标签弹性

[作品入口](https://60fps.design/shots/family-fluid-price-charts-animation) · [来源](https://60fps.design/shots/family-fluid-price-charts-animation)

钱包界面的价格曲线在时间范围切换中流畅变形，配合弹性的标签过渡。

待核查：实际播放并拖动进度；观察时间范围切换、曲线形变和静止状态；不评价投资内容。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。60fps 是录像发布者，不是对应 App 的官方厂商说明；页面标题/动作说明尚需对照真实片段。

[公开录像源](https://video.gumlet.io/66b49d08225b7b88f78b7b44/68689573fc386bd77fdc75f5/main.mp4)：HEAD 200，video/mp4，未播放。

### 16. Gucci：La Famiglia 互动谜案

[作品入口](https://lafamigliamysteryunfolds.gucci.com/) · [来源](https://thefwa.com/cases/gucci-la-famiglia-mystery-unfolds)

Gucci 官方活动把珠宝失踪故事组织成可调查的互动谜案，项目资料说明结合实时对话。

待核查：进入谜案并检查场景、人物与对话入口；若有登录要求，记录具体限制。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。HTML 是脚本入口壳，作品内容证据来自品牌域名与官方 FWA 项目；需确认当前活动主资源与会话可用。

### 17. Indigo：五段珠宝感官故事

[作品入口](https://indigo-laboratory.it/) · [来源](https://thefwa.com/cases/indigo-laboratory)

手工珠宝品牌以五个故事组织不同系列，每个故事配有独立声音与视觉身份。

待核查：切换故事与系列，检查声音、商品图集及转场。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 18. OUTFIT：设计工作室服饰商店

[作品入口](https://outfit.hellohello.is/) · [来源](https://thefwa.com/cases/outfit)

++hellohello 的自有服饰商店，将工作室视觉识别延展到商品列表与详情界面。

待核查：浏览商品并打开详情，核查图像、选项和返回过渡；不提交订单。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 19. RetroCast Now：复古天气播报界面

[作品入口](https://weather.com/retro) · [来源](https://thefwa.com/cases/retrocast-now)

The Weather Channel 将九十年代本地天气播报样式重构为可按地点查看的网页体验。

待核查：选择地点并观看播报循环，检查天气图表、时序与地点切换。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 20. UTB 25 周年：动态历史地图

[作品入口](https://jenamdvacetpet.cz/) · [来源](https://thefwa.com/cases/25-years-of-university-in-zlin)

大学周年微站通过互动三维地图组织历史里程碑与城市发展故事。

待核查：探索地图并打开多个年份/事件，检查视角、信息层和返回。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 21. Dialed Color：颜色记忆滑杆界面

[作品入口](https://dialed.gg/color) · [来源](https://thefwa.com/cases/color-game)

独立颜色记忆游戏先展示目标颜色，再通过滑杆重建颜色并给出差异评分。

待核查：完成一轮颜色重建，核查滑杆、目标/选择对比与计分过渡。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 22. Quintessence：五种视觉世界叙事

[作品入口](https://quintessence.ultranoir.com/) · [来源](https://thefwa.com/cases/quintessence)

ultranoir 的交互故事以五种视觉世界呈现同一叙事，原站推荐在移动设备体验。

待核查：开始体验并切换世界，观察各世界视觉、导航与重新开始状态。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 23. 365days：水墨与金色作品空间

[作品入口](https://kamimae.com/365days/) · [来源](https://thefwa.com/cases/365days-project-in-2024)

作者将一年创作的 366 张纸上水墨与金色画作组织为虚拟画廊。

待核查：浏览空间并展开不同画作，检查图像、编号与视角切换。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 24. XOX：实时井字棋界面

[作品入口](https://xox.makemepulse.com/) · [来源](https://thefwa.com/cases/xox)

makemepulse 将井字棋设计为强调响应速度与视觉反馈的实时对战体验。

待核查：开始匹配或可用练习，核查落子、回合和胜负反馈；无人匹配时明确记录。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 25. iyO：无屏设备三维配置体验

[作品入口](https://www.iyo.ai/) · [来源](https://thefwa.com/cases/iyo-p2)

设备品牌网站以三维模型、声音波形和粒子表现呈现无屏计算设备，项目资料包含配置器。

待核查：检查模型、配置选项与声音视觉章节；不提交购买。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 26. Sutéra：Change Reality 空间界面

[作品入口](https://www.sutera.ch/) · [来源](https://thefwa.com/cases/sutera)

空间界面设计师作品集通过 Change Reality 按钮切换不同呈现世界。

待核查：点击 Change Reality 并检查不同世界的导航和内容可读性。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 27. Ruinart：数字壁画探索

[作品入口](https://fresque.ruinart.com/) · [来源](https://thefwa.com/cases/ruinart-digital-fresco)

品牌与艺术家 Manon Diemer 的实体壁画被转为可自由探索的数字作品。

待核查：移动或缩放壁画，展开细节并查看内容入口。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 28. Utopia Tokyo：面具与未来城市

[作品入口](https://www.utopiatokyo.com/) · [来源](https://thefwa.com/cases/utopia-tokyo)

独立数字体验把日本历史意象、面具与未来城市设定结合成可探索的叙事空间。

待核查：进入场景并执行界面提示操作，核查面具、信息层与返回路径。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。

### 29. Ventusky：天气图层与风场界面

[作品入口](https://www.ventusky.com/) · [来源](https://www.ventusky.com/)

完整天气地图界面提供温度、降水、雷达、风速等图层及风场动画。

待核查：切换图层、地点与时间，检查粒子、图例与地图控制。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。收录理由是可视化/浏览界面，不是将分析结论作为本库事实背书。

### 30. Electricity Maps：用电碳强度地图

[作品入口](https://app.electricitymaps.com/map/fifteen_minutes) · [来源](https://app.electricitymaps.com/map/fifteen_minutes)

电力地图以碳强度图例组织地区电网信息，并提供时间粒度与侧栏入口。

待核查：确认主地图加载，选择区域并查看图表、图例和时间范围；区分免费内容与登录入口。
响应：GET 403。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。收录理由是可视化/浏览界面，不是将分析结论作为本库事实背书。 命令行 GET 被站点防护拦截；公开网页读取工具可读地图页面与碳强度图例，仍需实际浏览器确认。

### 31. The Real Kevin Bacon：电影人物关系

[作品入口](https://pudding.cool/2026/10/kevin-bacon/) · [来源](https://pudding.cool/2026/10/kevin-bacon/)

互动数据作品提供演员搜索、年代滑杆与角色关系比较，围绕电影合作网络展开。

待核查：搜索一名演员，拖动年份并推进比较/模拟阶段，检查图表过渡。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。收录理由是可视化/浏览界面，不是将分析结论作为本库事实背书。

### 32. 5,000 Restaurant Menus：历史菜单浏览器

[作品入口](https://pudding.cool/2026/06/menu-collection/) · [来源](https://pudding.cool/2026/06/menu-collection/)

以纽约公共图书馆历史菜单收藏为对象的独立浏览器，提供年份、展开与下一份菜单操作。

待核查：打开菜单、展开图像、切换下一份，检查数据与图像导航。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。收录理由是可视化/浏览界面，不是将分析结论作为本库事实背书。

### 33. Happy Map：十万个幸福瞬间

[作品入口](https://pudding.cool/2026/02/happy-map/) · [来源](https://pudding.cool/2026/02/happy-map/)

将十万个关于幸福时刻的文字记录组织为地图式浏览作品。

待核查：等待地图完成，尝试选点、移动与文本展开；先确认画面确实超出 Loading。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。收录理由是可视化/浏览界面，不是将分析结论作为本库事实背书。

### 34. Common Threads：音乐主题时间线

[作品入口](https://pudding.cool/2025/12/motifs/) · [来源](https://pudding.cool/2025/12/motifs/)

音乐主题可视化将不同音乐剧中的重复旋律与时间图表相连，提供音频播放和片段切换。

待核查：播放片段并切换 Previous/Next，观察图表高亮和多主题时间线；不摘录歌词。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。收录理由是可视化/浏览界面，不是将分析结论作为本库事实背书。

### 35. NYC Urban Textscape：街头文字搜索

[作品入口](https://pudding.cool/2025/07/street-view/) · [来源](https://pudding.cool/2025/07/street-view/)

围绕纽约街景可见文字构建的交互浏览作品，提供城市文字数据的视觉检索方向。

待核查：确认搜索和街景主体加载，输入普通地标/词语，检查结果与定位反馈。
响应：GET 200。仅完成来源研究，未用浏览器查看主体、执行交互或播放，不计核验通过。收录理由是可视化/浏览界面，不是将分析结论作为本库事实背书。

## 未纳入

- [Apple Health：健康类别花环入场](https://60fps.design/shots/apple-health-longevity-intro-animation)：URL 已存在。
- [Revolut：三维卡片就绪入场](https://60fps.design/shots/revolut-card-ready-animation)：URL 已存在。
- [Circle：头像气泡群动态开场](https://60fps.design/shots/circle-splash-bubbles-pop-interaction)：URL 已存在。
- [Brick：引导标题动词翻转](https://60fps.design/shots/brick-intro-value-prop-text-flip-interaction)：URL 已存在。
- [Plasma：报价卡变为底部面板](https://60fps.design/shots/plasma-duo-style-bottom-sheet-open-interaction)：URL 已存在。
- [Duolingo：石块雕刻角色奖励](https://60fps.design/shots/duolingo-sparkle-sculpt-pop-interaction)：URL 已存在。
- [CRED：票数滑杆与票券粒子](https://60fps.design/shots/cred-ticket-pop-on-slider-interaction)：URL 已存在。
- [Run Receipt：手写签名落在收据上](https://60fps.design/shots/run-receipt-signature-interaction)：URL 已存在。
- [Platen：打字机灯光与主题切换](https://60fps.design/shots/platen-typewriter-intro-how-to-interaction)：URL 已存在。
- [Alethia](https://www.alethia.earth/)：以宣传介绍为主，未确认有独立可操作的数据界面。
- [Brunello Cucinelli - Human-Centred AI E-commerce](https://shop.brunellocucinelli.com/en-gb/ai)：原站 403。

## 完成检查

- 所有 JSON 条目为 candidate / browser_verified=false，媒体 preview_verified=false。
- 未修改主库、UI、构建代码或通过记录。
