# 候选选品质量与重复审查

日期：2026-11-03。范围：第一轮79条 + 第二轮41条，共120条候选。逐条读取名称、URL、描述、类型与访问说明，并复查已有原站 HTML/媒体证据；没有修改任何候选数据或主库。

本子线程重新调用 `cua.getState()` 后仍返回 `browsers: []`，未接管其他线程标签。因此本报告是选品与证据审查，**不是画面验收**。不能据此将任何候选改为通过，也不能把仅有 HTML 的网站断言为“没有好 UI”。

## 结论

120条中没有发现明显混入的教程课程或纯 README；需要处理的主要是“主页入口代替具体作品”、同类演示过密，以及商业网站的产品截图/交互证据不足。建议先排除 Rauno 首页这个导航入口，优先核验其12个独立原型。

| 审查建议 | 数量 |
|---|---:|
| 优先浏览器核验 | 97 |
| 建议不单独纳入 | 1 |
| 需补强视觉证据 | 11 |
| 同类择优 | 10 |
| 需查可见缺陷 | 1 |

“需补强视觉证据”不等于站点差。如果打开后是有充分产品 UI 的优秀营销网页，可以保留；如果主体只是口号、客户标志、下载/销售按钮，或必须登录才看得到任何实际界面，就应剔除或寻找具体公开作品页。

## URL 与主题重复

- 两轮120条按最终 URL 归一化（忽略 www、末尾斜杠）没有内部重复；与核查时的五份来源文件共173条也没有 URL 重合。
- 主题重复比 URL 重复更明显：30条来自60fps，13条在Rauno域名（含首页），5条Globe.GL、5条Three.js、5条shadcn预览。不要把同源数量当质量保证。
- [Rauno 首页](https://rauno.me/)主要承担入口作用，已有具体原型后不建议独立占条目。
- [14islands](https://www.14islands.com/)和[Blobmixer](https://blobmixer.14islands.com/)属于作品集与具体工具，不能机械去重。
- [Figma Slides](https://www.figma.com/slides/)与[Figma Design](https://www.figma.com/design/)是不同产品；[Notion Calendar](https://www.notion.com/product/calendar)与[Notion 首页](https://www.notion.com/)也不是同一页面，但后者必须证明新增价值。
- Things、Opal 等官网与对应60fps具体状态录像可以同时存在，前提是一个展示完整界面、另一个展示明确微交互；不使用相同文案假装两种内容。
- 海浪/水池/流体已有多种候选和旧库条目；建议优先保留有明确可操作反馈的代表，普通海面与材质测试后置。Globe.GL五条也应按数据编码/交互差异挑选，不按每种贴图计数。

## 需特别注意的来源证据

- [Pitch](https://pitch.com/)、[AFFiNE](https://affine.pro/)、[Figma Design](https://www.figma.com/design/)的图片描述可对应编辑器、面板、变量等具体 UI，值得优先浏览器核查。
- [Felt](https://felt.com/)当前图片描述包含水彩场景和业务示意，不能自动解释为可操作 GIS。必须看真实界面或首屏视频。
- [Tana](https://tana.inc/)目前是代理会议平台；首屏若只播放参会者面部视频，不能据此认定 UI 动效突出。旧版笔记产品描述已不适用。
- [Superhuman](https://superhuman.com/)当前是多产品入口，原页虽有使用图片，仍应寻找明显的邮件/文档实际展示，而不是只收品牌入口。
- [shadcn sidebar-03](https://ui.shadcn.com/view/new-york-v4/sidebar-03)是可渲染的目录组件，不是教程文章，但完整内容很弱；[dashboard-01](https://ui.shadcn.com/view/new-york-v4/dashboard-01)更符合完整 UI 需求。
- [House of Corto](https://www.houseofcorto.com/)有 HTML 残留占位句；若实际可见，直接剔除。当前未看到画面，不擅自报视觉失败。

## 全部120条逐项审查

序号中的“一/二”对应候选批次；每条链接是实际候选 URL。以下“优先核验”仅表示研究价值，不表示通过。

| 批次/序号 | 候选与来源 | 建议 | 理由 |
|---|---|---|---|
| 一-1 | [Igloo Inc.：品牌官网](https://igloo.inc) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-2 | [Active Theory：数字体验工作室](https://activetheory.net) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-3 | [monopo London：创意机构界面](https://monopo.london) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-4 | [14islands：产品与品牌作品集](https://www.14islands.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-5 | [Blobmixer：自由塑形的 3D 团块](https://blobmixer.14islands.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-6 | [Makepill：产品机构官网](https://makepill.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-7 | [Immersive Garden：数字体验官网](https://immersive-g.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-8 | [Studio Freight：品牌项目编排](https://studiofreight.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-9 | [Studio Herrström：音乐与文化品牌展示](https://studioherrstrom.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-10 | [Clay：数字产品与品牌案例](https://clay.global) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-11 | [Ramotion：Web 与移动产品展示](https://www.ramotion.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-12 | [Robb Owen：创意开发者作品集](https://robbowen.digital) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-13 | [Seán Halpin：产品设计师作品集](https://www.seanhalpin.xyz) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-14 | [Henry Heffernan：个人作品集](https://henryheffernan.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-15 | [Rauno Freiberg：设计工程作品](https://rauno.me) | 建议不单独纳入 | 首页主要为 Craft、Projects、Field Notes 等入口；本轮已有12个具体微交互，保留作品本身更直接。 |
| 一-16 | [abeto：实时交互作品集](https://abeto.co) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-17 | [Aristide Benoist：动效开发作品集](https://aristidebenoist.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-18 | [Chartogne-Taillet：葡萄园品牌叙事](https://www.chartogne-taillet.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-19 | [Chiara Luzzana：声音设计作品集](https://www.chiaraluzzana.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-20 | [Pitch：演示文稿产品界面展示](https://pitch.com) | 优先浏览器核验 | 页面图片描述明确提及编辑器、样式选项、分析、品牌库与工作区；产品 UI 证据比泛营销入口更强。 |
| 一-21 | [Superhuman：效率工具产品展示](https://superhuman.com) | 需补强视觉证据 | 首页现为 Mail、Docs、Go 等套件入口；已有应用使用图片证据，但应优先选具体 Mail 界面，不能仅凭套件首页名气通过。 |
| 一-22 | [Reflect：笔记产品界面展示](https://reflect.app) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-23 | [CleanShot X：截图工具展示](https://cleanshot.com) | 优先浏览器核验 | 原页有 quickaccess、zoom 等功能录像，比纯口号页更接近用户想要的反馈与工具 UI。 |
| 一-24 | [Craft：文档与任务界面展示](https://www.craft.do) | 需补强视觉证据 | 现有抓取证据主要是产品身份与营销结构；需看到具体文档/任务 UI 后才能保留。 |
| 一-25 | [Things：任务管理界面展示](https://culturedcode.com/things) | 优先浏览器核验 | 原页明确列出 Mac、iPhone、iPad、Apple Watch 界面截图与产品视频。 |
| 一-26 | [Figma Slides：演示编辑器展示](https://www.figma.com/slides) | 优先浏览器核验 | 两个候选分别为 Slides 与 Design；原页有插件选择、投票、设计变量、动效曲线等具体 UI 描述，不能因同域误去重。 |
| 一-27 | [Notion Calendar：日历产品展示](https://notion.com/product/calendar) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-28 | [Spline：3D 设计产品展示](https://www.spline.design) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-29 | [Rive：交互动画产品展示](https://rive.app) | 需补强视觉证据 | 首页是多产品平台与编辑器/CLI/游戏引擎入口；必须确认实际可看的动画或编辑器展示，不能收导航和市场页。 |
| 一-30 | [tldraw：即时白板界面](https://tldraw.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-31 | [Excalidraw：手绘风白板界面](https://excalidraw.com) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-32 | [Song Maker：音乐网格创作界面](https://musiclab.chromeexperiments.com/Song-Maker) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-33 | [Elastic Man：弹性面部形变](https://david.li/elastic-man) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-34 | [Fluid Paint：流体绘画](https://david.li/paint) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-35 | [Ocean Wave Simulation：海浪模拟](https://david.li/waves) | 同类择优 | 与 Three.js 海面和可交互水池同属水面演示；本轮先验更有明确交互的水池，避免水面素材过密。 |
| 一-36 | [Things 3：按钮展开为待办卡片](https://60fps.design/shots/things-3-drag-to-create-to-do-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-37 | [Perplexity：模型选择抽屉形变](https://60fps.design/shots/perplexity-model-selection-sheet-morph-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-38 | [Snapseed：照片散落后归堆](https://60fps.design/shots/snapseed-photos-pop-shuffle-effect) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-39 | [Airbnb：导航标签图标旋转](https://60fps.design/shots/airbnb-tab-icon-animation) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-40 | [Pokémon TCG：撕开卡包揭示卡牌](https://60fps.design/shots/poke-mon-tcg-pocket-swipe-packet-to-reveal-card-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-41 | [Chrome：下拉操作导航](https://60fps.design/shots/google-chrome-pull-down-to-reload-and-new-tab) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-42 | [CRED：账单卡堆展开](https://60fps.design/shots/cred-autopay-bills-stack-animation) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-43 | [Swatch This：相机图标翻为 3D 模型](https://60fps.design/shots/swatch-this-3d-camera-flip-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-44 | [Recollect：卡片、胶囊与网格形变](https://60fps.design/shots/recollect-value-prop-morph-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-45 | [Monogram：语音输入液态模糊反馈](https://60fps.design/shots/monogram-tap-and-hold-mic-liquid-blur-pulse-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-46 | [Currency Converter：手写货币符号筛选](https://60fps.design/shots/currency-simple-converter-draw-symbol-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-47 | [Linear：问题编辑操作弹层](https://60fps.design/shots/linear-issue-actions-popup-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-48 | [Lumy：位置选择抽屉](https://60fps.design/shots/lumy-select-location-sheet-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-49 | [Google：搜索栏扩展为 AI 页面](https://60fps.design/shots/google-ai-mode-search-morph-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-50 | [Find My：搜索物品放大镜动画](https://60fps.design/shots/apple-find-my-searching-items-sheet-animation) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-51 | [Opal：敲开宝石奖励](https://60fps.design/shots/opal-tap-to-reveal-gem-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-52 | [Good Air：天气时间滑杆](https://60fps.design/shots/good-air-time-slider-dynamic-weather-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-53 | [Cosmos：主题切换预览](https://60fps.design/shots/cosmos-theme-switcher-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-54 | [Apple Astronomy：行星壁纸切换](https://60fps.design/shots/apple-astronomy-wallpaper-3d-planets-morph-swipe-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-55 | [Ben Journal：天气背景切换](https://60fps.design/shots/ben-journal-weather-toggle-background-animation) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-56 | [The Outsiders：进度图表配色切换](https://60fps.design/shots/the-outsiders-progress-graph-color-change-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-57 | [Apple：摄影风格横向预览](https://60fps.design/shots/apple-photographic-styles-carousel-swipe-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-58 | [Moods Faster：心情胶囊展开](https://60fps.design/shots/moods-faster-pills-morph-expand-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-59 | [Okuri：拟物日历翻页](https://60fps.design/shots/okuri-page-flip-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-60 | [Apple Wallet：卡片全息光泽](https://60fps.design/shots/apple-wallet-card-gyro-pattern-color-change-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-61 | [Avec：按住说话到文本](https://60fps.design/shots/avec-hold-and-speak-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-62 | [Find My：AirPods 空间搜寻界面](https://60fps.design/shots/apple-find-my-finding-airpods-case-gyroscope) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-63 | [Elevate：答案词语形变反馈](https://60fps.design/shots/elevate-correct-answer-words-morph-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-64 | [Cosmos：内容分组拖拽](https://60fps.design/shots/cosmos-cluster-drag-and-drop-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-65 | [Pinterest：共享抽屉横向切换](https://60fps.design/shots/pinterest-shared-sheet-swipe-interaction) | 优先浏览器核验 | 具体 App 操作录像，题材明确且不是教程；需看播放时间推进及关键状态，不把视频当可交互原 App。 |
| 一-66 | [Globe.GL：全球人口柱状地球](https://vasturiano.github.io/globe.gl/example/world-population) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-67 | [Globe.GL：国际航线弧线](https://vasturiano.github.io/globe.gl/example/airline-routes/us-international-outbound.html) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-68 | [Globe.GL：海底通信电缆](https://vasturiano.github.io/globe.gl/example/submarine-cables) | 同类择优 | 与航线示例同属球面路径表达；只有布局或交互差异足够大时才单独计数。 |
| 一-69 | [Globe.GL：昼夜循环地球](https://vasturiano.github.io/globe.gl/example/day-night-cycle) | 同类择优 | 地球昼夜可作为背景特效，但应与人口/航线界面区分用途；不凭换贴图增加 UI 数量。 |
| 一-70 | [Globe.GL：月球着陆点界面](https://vasturiano.github.io/globe.gl/example/moon-landing-sites) | 同类择优 | 同一地球组件体系的地点标记，暂后于人口和航线示例；视觉检查后再决定独立价值。 |
| 一-71 | [Three.js：周期表空间排列](https://threejs.org/examples/css3d_periodictable.html) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-72 | [Three.js：可扰动水面](https://threejs.org/examples/webgl_gpgpu_water.html) | 同类择优 | 与 David Li 波浪和 Evan Wallace 水池重复覆盖水面主题，先择优一个有清楚交互的代表。 |
| 一-73 | [Three.js：海面与天空](https://threejs.org/examples/webgl_shaders_ocean.html) | 同类择优 | 与其他海浪/水池近似；偏渲染示例，需画面表现明显出色才单独收录。 |
| 一-74 | [Three.js：透射玻璃材质](https://threejs.org/examples/webgl_materials_physical_transmission.html) | 同类择优 | 属于单项材质技术示例，已有库玻璃效果较多；应以视觉效果价值单独验，不当成完整 UI。 |
| 一-75 | [Three.js：发光后处理](https://threejs.org/examples/webgl_postprocessing_unreal_bloom.html) | 同类择优 | 属于发光技术示例，单独画面若不够突出就不扩充；源代码官方不等于选品优秀。 |
| 一-76 | [Evan Wallace：可交互水池](https://madebyevan.com/webgl-water) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-77 | [glfx.js：实时图像滤镜台](https://evanw.github.io/glfx.js/demo) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 一-78 | [deck.gl：纽约出租车轨迹](https://deck.gl/examples/trips-layer) | 优先浏览器核验 | 具体地图数据体验，题材有差异；先确认地图、数据和 WebGL 上下文正常，空地图不能通过。 |
| 一-79 | [deck.gl：六边形空间聚合](https://deck.gl/examples/hexagon-layer) | 优先浏览器核验 | 具体地图数据体验，题材有差异；先确认地图、数据和 WebGL 上下文正常，空地图不能通过。 |
| 二-1 | [Rauno · Exclusion Tabs](https://rauno.me/craft/exclusion-tabs) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-2 | [Rauno · Vanish Input](https://rauno.me/craft/vanish-input) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-3 | [Rauno · Wheel Input](https://rauno.me/craft/wheel-input) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-4 | [Rauno · Vercel Footer](https://rauno.me/craft/vercel-footer) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-5 | [Rauno · Logo Carousel](https://rauno.me/craft/logo-carousel) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-6 | [Rauno · Adaptive Precision](https://rauno.me/craft/adaptive-precision) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-7 | [Rauno · Radial Menu](https://rauno.me/craft/radial-menu) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-8 | [Rauno · Minimap](https://rauno.me/craft/minimap) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-9 | [Rauno · Fractional Slider](https://rauno.me/craft/fractional-slider) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-10 | [Rauno · Precision Slider](https://rauno.me/craft/precision-slider) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-11 | [Rauno · Flashlight Tabs](https://rauno.me/craft/flashlight-tabs) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-12 | [Rauno · Copy & Paste](https://rauno.me/craft/copy-paste) | 优先浏览器核验 | 原作者独立控件，原页有具体操作或原型主体；其中三种滑块需实际比较，保留功能差异而不是按作者批量收录。 |
| 二-13 | [shadcn · Dashboard 01 完整数据界面](https://ui.shadcn.com/view/new-york-v4/dashboard-01) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-14 | [shadcn · 可折叠应用侧栏](https://ui.shadcn.com/view/new-york-v4/sidebar-07) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-15 | [shadcn · 文档目录侧栏](https://ui.shadcn.com/view/new-york-v4/sidebar-03) | 同类择优 | 主体为文档目录与占位内容，虽然不是教程文章，但不够完整；同批 dashboard 和 sidebar-07 优先。 |
| 二-16 | [shadcn · Login 03 认证界面](https://ui.shadcn.com/view/new-york-v4/login-03) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-17 | [shadcn · Login 04 认证界面](https://ui.shadcn.com/view/new-york-v4/login-04) | 同类择优 | 与 login-03 功能近似；先比较真实桌面和移动布局，若差异仅装饰则二选一。 |
| 二-18 | [Warp Terminal](https://www.warp.dev/terminal) | 需补强视觉证据 | 已改为具体 /terminal 页，但本轮无终端实际运行证据；须看清终端 UI，不能把代码/营销文案当精美界面。 |
| 二-19 | [Zed 编辑器](https://zed.dev/) | 需补强视觉证据 | 编辑器产品身份明确，静态 HTML 的非标志图片描述主要是人物和文章；需核实首屏实际编辑器展示是否充分。 |
| 二-20 | [Obsidian 知识工作台](https://obsidian.md/) | 优先浏览器核验 | 原页明确包含 Canvas 嵌入内容；适合验证知识图谱/画布组织，仍不可等同应用已操作。 |
| 二-21 | [AFFiNE 文档与白板](https://affine.pro/) | 优先浏览器核验 | 原页图片描述明确指向文档编辑器、白板、规划数据库；适合优先验证多模式工作台。 |
| 二-22 | [HEY 邮件与日历](https://www.hey.com/) | 优先浏览器核验 | 原页提供产品 overview 图片和视频；优先核对邮件/日历状态。 |
| 二-23 | [Evervault 支付产品界面](https://evervault.com/) | 需补强视觉证据 | 目前已有事实只支持支付产品定位，不能证明具体卡片交互或界面质量；主体若只有产品文案则排除。 |
| 二-24 | [Felt 地图工作台](https://felt.com/) | 需补强视觉证据 | 当前图片描述包含水彩地图场景、插图及业务示意；它们不自动等于实际 GIS UI，需辨别首屏视频和真实界面占比。 |
| 二-25 | [Cal.com 预约日程](https://cal.com/) | 需补强视觉证据 | 排程软件身份明确，但现有描述偏功能营销；必须看到具体预约界面或可交互演示。 |
| 二-26 | [Notion 工作空间](https://www.notion.com/) | 需补强视觉证据 | 首页是多个功能与代理的入口；已有演示媒体地址，但仍须看主体是否有可辨识工作区 UI，优先具体 Calendar 页。 |
| 二-27 | [Figma Design 产品界面](https://www.figma.com/design/) | 优先浏览器核验 | 两个候选分别为 Slides 与 Design；原页有插件选择、投票、设计变量、动效曲线等具体 UI 描述，不能因同域误去重。 |
| 二-28 | [Penpot 设计工作台](https://penpot.app/) | 优先浏览器核验 | 原页包含 App project 与 Web project 的具体设计项目图片描述。 |
| 二-29 | [Tana 会议工作台](https://tana.inc/) | 需补强视觉证据 | 当前是代理会议产品，首屏视频文件对应参会者头像；不能仅凭这些视频认定 UI 动效优秀，也不能标为旧版笔记产品。 |
| 二-30 | [Capacities 知识工作台](https://capacities.io/) | 需补强视觉证据 | 产品身份明确，已有描述尚未指出具体过渡或可操作控件；需完整看产品 UI，不能仅因知识工具名气入库。 |
| 二-31 | [Playdate 产品官网](https://play.date/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-32 | [Daylight DC-1 产品官网](https://daylightcomputer.com/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-33 | [teenage engineering 产品官网](https://teenage.engineering/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-34 | [Opal 专注应用](https://opalapp.com/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-35 | [Atmos Gallery 配色工作台](https://atmos.gallery/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-36 | [Aardvark Book Club](https://www.aardvarkbookclub.com/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-37 | [MoMoney 博物馆官网](https://museumofmoney.com/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-38 | [House of Corto 家具作品](https://www.houseofcorto.com/) | 需查可见缺陷 | HTML 中存在 This is some text inside of a div block 残余占位句；不据此宣称视觉坏掉，但若实际可见就剔除。 |
| 二-39 | [Lando Norris 官方网站](https://landonorris.com/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-40 | [MANA Yerba Maté](https://manayerbamate.com/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |
| 二-41 | [TrueKind 护肤品牌](https://truekindskincare.com/) | 优先浏览器核验 | 具体作品/界面/效果的来源成立；是否好看、是否主体完整、是否能操作仍须看实际画面。 |

## 交给画面核验的统一标准

1. 先看主体是否完整；空白、报错、登录墙或长时间加载不能算作品通过。
2. 静态 UI 参考必须有足够完整、可辨识的真实界面；动态效果必须看到前后状态或视频时间推进。
3. 教程文章、课程售卖、导航索引、模板目录不纳入。单项控件演示可纳入，但不把周围安装文档当作品。
4. 产品营销站只有在本身界面编排出色、或展示足够清楚的实际产品 UI 时保留；不能因品牌知名或 URL200通过。
5. 同类作品比较交互差异和画面完成度。若只是数据/贴图/颜色替换，优先留少量代表。
