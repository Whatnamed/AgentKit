# 设计 Skills 的项目来源索引（脱敏简版）

> 这些项目的源码、设计规范和历史讨论是方法学习材料，不会自动成为新项目必须继承的设计决策。

## Morpho — 设计系统完整性和交付方法

- 来源：[Morpho design-system README](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/README.md)、[Design System](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/docs/DESIGN-SYSTEM.md)、[Source Map](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/docs/SOURCE-MAP.md)。
- 起因：在 Morpho 开发后，用户通过 Claude Design 制作完整设计系统，后续 ProxyLens 开发时借鉴它**资料内容、组织结构、详细度和交付方式**，不意味着复制 Morpho 品牌、字体、画布或业务布局。
- 可学：分层 Token → 组件源码/类型 → 逐组件 Prompt → Source Map → 版本/依赖/导出说明。仓库版导出不包含原独立设计系统项目的全部 `guidelines/` 和 `ui_kits/`，不能假称原源完整。
- 适合：`visual-system-extract`、`visual-system-create` 的“做得完整且可交付”的样板。

## ProxyLens — 产品、视觉和迭代决策的实践

- 来源：[产品交互框架](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/PROXYLENS_UI_PRODUCT_INTERACTION_FRAMEWORK_v1.md)、[语义显示](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/ui-semantic-presentation-v1.md)、[视觉规范](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/design/PROXYLENS_UI_DESIGN_SYSTEM_v1.md)、[实施与 QA](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/design/PROXYLENS_UI_IMPLEMENTATION_AND_QA_v1.md)。
- 三段历史 UI 讨论：明确曾从产品职责和真实后端事实出发建立 IA；随后多轮比较、收敛配色、字体和中英混排，出现过 **CSS 字体声明与实际字体不一致**、选中与语义标签状态撞色、局部修改引起行高和对齐漂移等问题。
- 可学：用户目标→产品 IA→视觉方向→设计系统→实际实现→有停点的复审；先判断是设计标准错还是执行偏离，再最小修改。保留真实状态，不用假“无数据”遮掩未知。
- 不应外推：网络审计对象、路由语义、固定 Inspector、最终字体组合、具体色值与宽度不是通用模板。

## AgentBench — 产品 IA 未成熟时迁移视觉的反例

- 来源：[产品规格](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/product-spec.md)、[IA v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/information-architecture.md)、[UX v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/ux-spec.md)、[视觉入口](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/design/README.md)。
- 当时有早期 UI 实验，把 ProxyLens 视觉语言迁移得部分近似，但产品页面职责不足，结果偏 Demo：无意义副标题、列表堆叠、题库被错误套成测试工作台布局等。
- 可学：一个产品的视觉系统不能代替另一个产品的页面行为；题库可用 List–Detail，测试执行可原位展开，同款颜色和控件不意味着同一 IA。没有真实目标宿主验收时，设计系统仍是“目标规范”。
- 不应外推：AgentBench 的八题、提交轮次、评分来源等仍属于其领域事实。

**来源状态**：三份 ProxyLens 历史聊天完整原文和图片存储于本地私有档案；本索引只放可公开的方法概括和固定仓库链接，不包含原文摘录和私人位置。
