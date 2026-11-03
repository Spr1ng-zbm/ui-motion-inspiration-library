# 视频素材检索与核验说明

检索日期：2026-11-02（Asia/Taipei）。本批共 53 条，B 站 20 条，YouTube 33 条。所有条目都有具体视频 URL；没有使用搜索结果页充数。

## 核验范围

- B 站 20 条：使用官方公开 view API 取回标题、作者、时长和封面，全部返回 code=0。metadata_url 字段可复查。
- YouTube 20 条：搜索工具返回原平台题名、作者或简介；已尝试逐条打开，部分只有页面标题，其余受到抓取限流。未观看视频，未把页面有响应视为播放成功。
- YouTube 13 条：来源为下列已读取第三方收藏索引，原视频访问多受限。verification 标为“第三方索引”，不冒充独立核验通过。
- 本机直连 YouTube oEmbed 全部遭 SSL EOF；对应 metadata_check 保存错误，不能据此判断视频删除。
- B 站封面来自官方 API；13 张 YouTube 封面地址直接来自已读取索引，尚未独立检验加载。其他封面留空。

## 重要来源

- [Swipefile：Motion, intros & product launches](https://swipefile.design/board/motion-intros-product-launches/)：用于发现具体软件产品发布片。仅录入与 UI 或创作工具直接有关的部分，不录入无关硬件广告。
- [JIEJOE 蜘蛛眼教程源码](https://github.com/JIEJOE-WEB-Tutorial/005-spidereye)：核对鼠标跟随案例与视频。
- [JIEJOE 横向滚动教程源码](https://github.com/JIEJOE-WEB-Tutorial/007-03-horizontal-scrolling-scrolltrigger)：核对横向滚动与视频。
- [JIEJOE CPDD](https://github.com/JIEJOE-Visual/cpdd)、[MAA](https://github.com/JIEJOE-Visual/MAA)：核对整站作品与视频。

## 收录方式

中文名称有时按效果重新命名，官方标题另存 official_title。description 为建议参考的方向，基于题名/简介或明确索引，不能当作本次实看评测。所有链接去重。部分教程包含培训、付费源码或产品营销；已在具体简介中注明明显限制。

## 逐条证据

- [拿了个国际小奖，我的个人网站演示](https://www.bilibili.com/video/BV1hYceeGEuq/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1hYceeGEuq/)
- [呼叫 matter！我的交互网站急需 2D 物理引擎](https://www.bilibili.com/video/BV1tAzVYdEoM/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1tAzVYdEoM/)
- [网站离高级，还差一个跳转动画？](https://www.bilibili.com/video/BV1Nk4y1Q7pk/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1Nk4y1Q7pk/)
- [开源网页游戏：当贪吃蛇遇上爆炸](https://www.bilibili.com/video/BV1gqZ4Y1ETA/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1gqZ4Y1ETA/)
- [像这样的超奈斯网站，该去哪里找？](https://www.bilibili.com/video/BV1Bu4y1A7ME) — 官方元数据；[证据](https://www.bilibili.com/video/BV1Bu4y1A7ME)
- [蜘蛛眼旋转：鼠标跟随互动](https://www.bilibili.com/video/BV1Mc411k7hv) — 官方元数据；[证据](https://www.bilibili.com/video/BV1Mc411k7hv)
- [页面横向滑动效果：ScrollTrigger 版](https://www.bilibili.com/video/BV1L83WzgEoJ) — 官方元数据；[证据](https://www.bilibili.com/video/BV1L83WzgEoJ)
- [神兽管理局：中国神话交互网页](https://www.bilibili.com/video/BV1Ka4y1o7aS) — 官方元数据；[证据](https://www.bilibili.com/video/BV1Ka4y1o7aS)
- [CPDD：搞怪个人介绍网页演示](https://www.bilibili.com/video/BV1Ne41177jP) — 官方元数据；[证据](https://www.bilibili.com/video/BV1Ne41177jP)
- [UI 动效作品集：消消美食街](https://www.bilibili.com/video/BV1zSfPYwEev/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1zSfPYwEev/)
- [2026 届游戏 UI 动效作品集](https://www.bilibili.com/video/BV1JybpzXESe/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1JybpzXESe/)
- [UI 动效：项目作品与 3D/2D 交互合集](https://www.bilibili.com/video/BV1vHUaBMEyr/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1vHUaBMEyr/)
- [丝滑的 XD 交互动效](https://www.bilibili.com/video/BV1T341127Pz/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1T341127Pz/)
- [Framer Site：丝滑的交互动效](https://www.bilibili.com/video/BV1nG4y1s77B/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1nG4y1s77B/)
- [Rive 动画中文课程：从 0 到精通](https://www.bilibili.com/video/BV1a7krB3EXe/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1a7krB3EXe/)
- [UI 动效设计案例实战教程合集](https://www.bilibili.com/video/BV1vA411N7jy/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1vA411N7jy/)
- [UI/UX 交互动效：设计师必备的动效设计](https://www.bilibili.com/video/BV1gg411X77A) — 官方元数据；[证据](https://www.bilibili.com/video/BV1gg411X77A)
- [Creating Elaborate Website Animation Sequences — GSAP 3](https://www.youtube.com/watch?v=T0_Y4oCjLxw) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=T0_Y4oCjLxw)
- [Master Creative Frontend in 2 Hours with React, Three.js & GSAP](https://www.youtube.com/watch?v=DEeaT6FxEws) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=DEeaT6FxEws)
- [GSAP Keeps Outdoing Itself With These Landing Page Animations](https://www.youtube.com/watch?v=olj1WWJEfA0) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=olj1WWJEfA0)
- [Next.js 自定义页面转场（Codegrid）](https://www.youtube.com/watch?v=3wtTG-8crF0) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=3wtTG-8crF0)
- [Landing Page Reveal Animation? One GSAP Timeline Did All of This](https://www.youtube.com/watch?v=z_0H7wLyX3A) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=z_0H7wLyX3A)
- [This Animated Landing Page Reveal Has Better Timing Than I Do](https://www.youtube.com/watch?v=PmlXAhlv9Vk) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=PmlXAhlv9Vk)
- [3D Image Slider Tunnel — Infinite Scroll](https://www.youtube.com/watch?v=XWZII4fiQ08) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=XWZII4fiQ08)
- [波浪式滚动画廊（Codegrid）](https://www.youtube.com/watch?v=ckX1c75CoFc) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=ckX1c75CoFc)
- [This GSAP Text Animation Shouldn't Be This Satisfying](https://www.youtube.com/watch?v=jRRSWhQEz5w) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=jRRSWhQEz5w)
- [Next.js + GSAP — Block Reveal Text Animation](https://www.youtube.com/watch?v=0H9aKFkBcS4) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=0H9aKFkBcS4)
- [Figma Tutorial & Liquid Swipe After Effects Animation](https://www.youtube.com/watch?v=3lE5ish-e44) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=3lE5ish-e44)
- [Build and Deploy an Awwwards Winning Website](https://www.youtube.com/watch?v=zA9r5zTllx4) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=zA9r5zTllx4)
- [Creative Frontend Course — Master GSAP, Three.js & React](https://www.youtube.com/watch?v=ATdaYQw0ptk) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=ATdaYQw0ptk)
- [Create an Infinite Horizontal Scroll Animation](https://www.youtube.com/watch?v=iLmBy-HKIAw) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=iLmBy-HKIAw)
- [Rive Tutorial for Beginners — Interactive Animation in 25 Minutes](https://www.youtube.com/watch?v=N3zGbAwL10U) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=N3zGbAwL10U)
- [Rive 官方：交互菜单 Quick Start（2026 更新）](https://www.youtube.com/watch?v=u2kThOXc3Ek) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=u2kThOXc3Ek)
- [Button Micro-Interaction Using Smart Animate in Figma](https://www.youtube.com/watch?v=nYFIOWcAe-Q) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=nYFIOWcAe-Q)
- [Cuberto Showreel 2024](https://www.youtube.com/watch?v=bK8eUJ65LyY) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=bK8eUJ65LyY)
- [Material Design Motion](https://www.youtube.com/watch?v=cQzien5H2Do) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=cQzien5H2Do)
- [Google I/O 2014 — Material Design: Motion](https://www.youtube.com/watch?v=FBD0VlcVS1E) — 原平台搜索元数据；[证据](https://www.youtube.com/watch?v=FBD0VlcVS1E)
- [Meet Notion Calendar](https://www.youtube.com/watch?v=C4Q2ezioTUM) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Introducing canvas — Slack](https://www.youtube.com/watch?v=wJ80ip-buXc) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Introducing Linear Agent](https://www.youtube.com/watch?v=mRql2VJ99gM) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Announcing Linear Reviews](https://www.youtube.com/watch?v=4r8YmQ6lfLo) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Raycast Focus: Enter Flow State](https://www.youtube.com/watch?v=ykaj0pS4A1A) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Introducing Pitch 2.0](https://www.youtube.com/watch?v=tqfeE5G36tM) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Unveiling the Next Generation of OneDrive](https://www.youtube.com/watch?v=DzXBdc8Dfmg) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Material Design](https://www.youtube.com/watch?v=Q8TXgCzxEnw) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Introducing Spline](https://www.youtube.com/watch?v=sIfP9h-H23s) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Webflow — A New Era of No-Code](https://www.youtube.com/watch?v=eEW2gr7K7kc) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Introducing Windows 11](https://www.youtube.com/watch?v=Uh9643c2P6k) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [Presenting: Figma Slides](https://www.youtube.com/watch?v=p-B--SGq_ZQ) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [The New Microsoft Icons: Diverse and Connected](https://www.youtube.com/watch?v=wYmTkgqbrDM) — 第三方索引；[证据](https://swipefile.design/board/motion-intros-product-launches/)
- [APP 展示视频与动效练习：健康检测概念](https://www.bilibili.com/video/BV1Q54y1q7oi/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1Q54y1q7oi/)
- [二次元、国风、科技风的游戏 UI 动效设计](https://www.bilibili.com/video/BV16o4y1S7Rg/) — 官方元数据；[证据](https://www.bilibili.com/video/BV16o4y1S7Rg/)
- [星际公民：飞船内部 FUI 与 HUD 界面](https://www.bilibili.com/video/BV1op4y1w7U5/) — 官方元数据；[证据](https://www.bilibili.com/video/BV1op4y1w7U5/)
