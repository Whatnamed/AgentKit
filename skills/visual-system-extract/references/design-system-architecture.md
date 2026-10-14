# 设计系统提取时的架构与文件组织

只有在要求**建立整套可交付设计系统**、迁移至另一技术平台或审查源资料“是否完整”时才加载。

## 先区分四类不同的设计信息

| 类别 | 主要问题 | 常见交付物 |
| --- | --- | --- |
| Design intent / Principles | 为什么要有这样的视觉角色、密度与主次？ | 设计目标、Do/Don't、少量代表页面 |
| Foundations / Tokens | 哪些规律跨组件一致、值和角色怎样命名？ | Typography、Color、Space、Shape、Surface、Motion、Theme、资产与版权 |
| Components & patterns | 单个控件有哪些状态，多个控件怎样完成任务？ | Anatomy、Variants、状态、键盘、响应式、组合模式/页面结构 |
| Source/quality handoff | 设计与真实实现谁是权威，版本与证据在哪里？ | Source Map、组件路径、设计文件、平台差异、验收/缺口 |

具体项目不必拥有大团队级 Storybook/Figma Tokens 工程，但**需要的具体细节不能只留一句“遵循设计系统”**。

## Token 层次不要一刀切

- primitive 记录原始尺度或调色板；
- semantic 记录用途/语义（text-primary、surface-raised、space-section 等），跨 Light/Dark/平台转换；
- component-only 记录某个可复用组件确有专属需求时的例外，不是强制为所有控件分别建立 Token 层。

类似色值也不一定有相同意义。主题映射必须区分文字、背景、状态、焦点、图表等，不仅换色相。
遵循项目现有 Token 真正的命名/引用约定；如无现成规范，选择小而有意义的层次而不是到处撒散乱常量。

## 从参考图提取不等于拿到源码

- 图片可观察层次、相对间距与视觉意图，但**不能**证明字体文件、精确行高、DOM、真实 hover 或实际主题。
- 设计文件可以提供参数与组件变体，却不一定反映运行中的宿主差异。
- 源码可证明配置与实现，不能保证所有字体实际加载、主题与数据状态都好。
- 真实运行可证实某个采样环境与状态的效果，但源代码、许可证和其他平台的情况仍须独立核实。

## 基本产物与版本化

最低应让另一 Agent 回答：它该依据什么版本/文件？按哪些设计目标决定新组件？如何使用各视觉角色？某个真实业务页不存在源组件时如何扩展？哪些领域 UI 绝不能照搬？设计变化应同步到哪里？

可把必要的参考拆成 `DESIGN-SYSTEM.md` / `tokens` / `components` / `patterns` / `SOURCE-MAP.md` 或使用目标仓库已有结构。Morpho 设计系统导出的 JSX、types、逐组件 Prompt 是**一种优秀范例而非唯一文件组织标准**；原独立设计项目还可能有当前导出未含的运行 UI Kit/规范卡片。

参考：[Morpho Design System](https://github.com/Whatnamed/Morpho/tree/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system)、[DTCG](https://github.com/design-tokens/community-group)、[GOV.UK Design System](https://design-system.service.gov.uk/patterns/)、[Anthropic Knowledge Work — Design System](https://github.com/anthropics/knowledge-work-plugins/blob/main/design/skills/design-system/SKILL.md)。
