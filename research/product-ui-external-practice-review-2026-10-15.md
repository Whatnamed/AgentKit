# Product & UX / Visual System：外部 Skills 与行业方法复审

> 研究时间：2026-10-15 · 性质：**精选公开源码与官方设计资料的比较 / 采用记录**，不是“所有知名 Skills”的排名或完整清单。只更新两个 Plugin 所依赖的技能正文与按需参考；没有创建更多必经流程、打分框架或额外安装依赖。

## 1. 评估标准

AgentKit 的任务是帮助个人从大概功能想法推进到**完整可开发的产品前端规格**，再把视觉方向深化成**细致且可以实现/迁移的设计系统**。

要同时满足：可用于不同类别产品；Agent 应主动查漏，但不能编造领域事实；最终要具体到页面与控件、视觉角色与空间节奏；过程不强迫用户提交长 PRD、跑完整发现流程、一次问十几个问题或反复评分。比较“哪些方法真正改善这个目标”，不比较 Skill 数量和 GitHub Star 排名。

## 2. 与代表性公开 Skills、工作流的比较

| 来源 | 核对到的特点 | 对 AgentKit 的决定 |
| --- | --- | --- |
| [Dean Peters — Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills)（[Workflow Catalog](https://github.com/deanpeters/Product-Manager-Skills/blob/main/catalog/commands.md)、[JTBD](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/jobs-to-be-done/SKILL.md)） | 问题发现、JTBD、排序、PRD、Story Mapping 和用户故事被做成独立方法/组合命令；产物与阶段清晰 | **借鉴**按问题选择方法、将客户任务与功能区分；**不借鉴**几十个独立 Skill 或强制经历整个 PM 生命周期 |
| [Microsoft 365 Agents Toolkit — PRD + Scenario Design](https://github.com/OfficeDev/microsoft-365-agents-toolkit/blob/dev/.github/skills/prd-ux-design/SKILL.md) | 高层 PRD 与描述用户步骤、状态、例外和界面的 Scenario 合同分开；当前业务设计与运行事实分开 | **借鉴**“Product intent ≠ detailed user-facing behavior”及场景粒度；**不借鉴**企业 owner、Proposal/HTML 生成与繁复审批门槛 |
| [Garry Tan — gstack](https://github.com/garrytan/gstack)（[Plan Design Review](https://github.com/garrytan/gstack/blob/main/plan-design-review/SKILL.md)） | 设计审核关注 IA、状态、用户路径、响应式、设计系统一致性；在写代码前发现用户实际会看到什么 | **借鉴**有 UI 范围才做设计审查、明确关键缺口与未定决策；**不借鉴**强制每题交互审批、大量评分/长篇审查步骤 |
| [Jesse Vincent — Superpowers](https://github.com/obra/superpowers)（[Brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)） | 构想、设计确认、写开发计划和代码验证分工明确，任务规模会改变产物深度 | **借鉴**短问题可直接回答、重大设计留下可开发依据；**不借鉴**其针对工程开发的强制 TDD/子 Agent 流水线 |
| [Anthropic — Frontend Design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 强调产品独立的视觉方向，而非套统一模板 | **借鉴**视觉方向要与具体产品身份相符；**不借鉴**任何特定大胆风格作为默认要求 |
| [Paul Bakaus — Impeccable](https://github.com/pbakaus/impeccable)（[主 Skill](https://github.com/pbakaus/impeccable/blob/main/plugin/skills/impeccable/SKILL.md)） | 拆出 Typography、Spacing、Layout、Color 等专业参考与反模式，按任务选择具体动作；主张有界视觉修正 | **借鉴**专业设计词汇与视觉“看起来不对”的诊断维度，限制无止境 polish；**不复制**其长命令清单或审美指令 |
| [NextLevelBuilder — UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)（[Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md)） | 以可检索的风格、色彩、字体、图表、UX 规则与技术栈资料为支持 | **借鉴**按任务加载专业参考，而不是将所有设计知识塞入一份 Prompt；**不引入**大规模风格数据库、自动猜配色的依赖 |
| [Microsoft VS Code — Design Philosophy](https://github.com/microsoft/vscode/blob/main/.github/skills/design-philosophy/SKILL.md) | Values → Principles → Moves：把“感觉不对”转换为可讨论的视觉原则，再确定 Token/组件改法 | **重点采用**设计反馈由用户观感到专业诊断的方式，避免用户亲自猜行高/间距；其专属设计价值、字阶与 spacing ramp 不能当跨项目默认 |
| [Anthropic Knowledge Work — Design System](https://github.com/anthropics/knowledge-work-plugins/blob/main/design/skills/design-system/SKILL.md) | Token、组件 Anatomy/variants/states/keyboard、审查/文档/扩展分开 | **借鉴**设计系统作为可交付、可维护的完整层级，不只有颜色和圆角 |
| [Microsoft VS Code UX CSS/Layout](https://github.com/microsoft/vscode/blob/main/.github/skills/ux-css-layout/SKILL.md)、[Sentry Design System](https://github.com/getsentry/sentry/blob/master/.agents/skills/design-system/SKILL.md) | 真正产品仓库的本地规范以已存在的 Token、组件 primitive 和平台源码为准 | **借鉴**尊重具体项目的 Source of Truth，跨项目 Skill 不写死控件尺寸与 CSS 值 |

上述项目各有平台、代码与工具依赖，不能假设它们对 AgentKit 目标任务同样有效；借鉴的是清晰可复用的方法，而不是完整复制开源 Skill 原文。不同生态安装与路由方式仍由宿主决定。

## 3. 官方行业参考的补充

| 参考 | 方法要点 | 对我们填补的空缺 |
| --- | --- | --- |
| [NN/g — Task Analysis](https://www.nngroup.com/articles/task-analysis/)、[UX Deliverables](https://www.nngroup.com/articles/common-ux-deliverables/) | 先理解用户实际要达成的任务；交付物应适合沟通目的，非必需全套文书 | Discovery 不停留于功能列表，同时不把个人项目变成企业文档工程 |
| [GOV.UK Design System — Patterns](https://design-system.service.gov.uk/patterns/) | Styles、Components 之外还有**按用户任务组织的 Patterns**，如校验信息、纠错、确认、完成多步骤任务 | Product UX 除布局/组件外主动识别任务模式；不照搬政府业务页面 |
| [W3C WAI ARIA APG](https://www.w3.org/WAI/ARIA/apg/patterns/) | 特定控件的键盘、焦点、状态、可访问语义 | 产品级“有个弹窗/树列表”必须能进一步定义实际交互，而非笼统可点击 |
| [IBM Carbon — Spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview)、[Atlassian — Spacing](https://atlassian.design/foundations/spacing) | 空间是组织关系、层级、密度的工具，组件内外不同层次，不只是随意加 Gap | 修复用户所说“空/闷/散/不精致”，需要系统地判断 Page/Section/Item 之间的**相对关系** |
| [W3C Design Tokens Community Group](https://github.com/design-tokens/community-group) | Token 的跨工具表示、语义与互操作方向 | 设计系统文档须区分数值、语义角色、组件例外和真实源码，而不规定所有项目用同样复杂度 |

## 4. 本轮在 AgentKit 实际采取的修改

### Product & UX

- [product-discovery](../skills/product-discovery/SKILL.md) 增补 [条件性专业方法](../skills/product-discovery/references/conditional-product-methods.md)：任务分析、JTBD、Story Mapping、角色权限和数据可行性仅在相关时启用。
- [product-ia-interaction](../skills/product-ia-interaction/SKILL.md) 增补 [跨产品类型与任务模式](../skills/product-ia-interaction/references/adaptive-product-patterns.md)：专业桌面工具、内容/知识库、B2B 协作、交易、数据分析、画布/创作、AI Agent、移动设备与高风险公共服务，针对不同任务选择真正有关的 UX 模式。
- [product-ux-review](../skills/product-ux-review/SKILL.md) 增补 [专业复审视角](../skills/product-ux-review/references/professional-review-lenses.md)：内容策略、数据事实、权限/角色、任务适合性与交付一致性。

**不变**：新产品的结束标准是**完整可开发的页面/控件/状态/交互规格**，不是完成很多营销、商业、访谈与 PRD 仪式；用户仍可从几句想法开始。

### Visual System

- [visual-system-create](../skills/visual-system-create/SKILL.md) 增补 [视觉术语与问题诊断](../skills/visual-system-create/references/visual-language-and-diagnosis.md)：Typography、Spacing/Rhythm、Density、Negative Space、Hierarchy、Surface、Alignment 等具体维度和从观感到根因的分析路径；同时说明一套成品设计系统含 Foundations、Tokens、组件/Patterns、Handoff/证据。
- [visual-system-adopt](../skills/visual-system-adopt/SKILL.md) 增补 [完整迁移层级与交接](../skills/visual-system-adopt/references/visual-fidelity-and-handoff.md)：基础值→语义角色→组件状态→整页节奏，源与目标的证据等级分开；不以“皮肤像了”或“只有配色字体”冒充完整迁移。
- [visual-system-extract](../skills/visual-system-extract/SKILL.md) 增补 [设计系统架构与责任](../skills/visual-system-extract/references/design-system-architecture.md)：原则、Tokens、组件/Pattern、Source Map/运行验证，和截图/设计稿/源码/实际呈现的不同证据能力。

**不变**：视觉体系可以先选方向、反复在真实代表页调整，最后产出可交付设计规范；不能为了固定流程一开始就锁定所有数值。视觉不能强行改变已确定的产品任务与页面职责。

## 5. 结论和仍然不保证的事

这轮发现的是**表达与参考知识的广度问题**，不是 AgentKit 的整体框架错误。现有 3 个 Product Skills + 4 个 Visual Skills 可以维持不变；只增加按需参考，避免源 Skill 变成一本没人会完整读的教科书。

新的类型指南是一张“可能值得考虑”的地图，**不是声称任何产品都不会出现未知需求**。新领域有特殊的合规/硬件/业务规则时，必须从该项目真实来源验证。模型执行不理想首先判断它是否加载并读到了相关参考；不因此无限扩写整套规则。

未来 AgentKit 可以单独研究[ gstack ](https://github.com/garrytan/gstack)、[ Superpowers ](https://github.com/obra/superpowers)、[ Product-Manager-Skills ](https://github.com/deanpeters/Product-Manager-Skills)等完整个人工作流体系，评估跨项目的规划、开发、代码审查和文档协作能力。**但这不是当前两个 Plugin 的前置任务**。
