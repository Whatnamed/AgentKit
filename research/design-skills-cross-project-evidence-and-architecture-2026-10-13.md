# 设计 Skills 第二轮跨项目来源核验与结构草案

> 2026-10-13 · 状态：**研究草案 / 部分来源已核对 / 尚非正式 Skill 规范**  
> 本文件只包含可公开的概括和可访问的项目文件链接。三份历史聊天的原文、附件以及详细逐轮定位仍保留在本地私有目录，不进入公开仓库。

## 1. 本轮已核实的来源

| 项目 | 固定来源 | 有效证据 | 本轮限制 |
| --- | --- | --- | --- |
| [ProxyLens](https://github.com/Whatnamed/ProxyLens/tree/f7ef34698533f741905bac0a1d554175eab8c0b4) | `f7ef34698533f741905bac0a1d554175eab8c0b4` | 产品交互框架、语义呈现、冻结设计系统、实现与 QA 文档，以及 `ui/src/styles/fonts.css`、`tokens.css` | 文件存在和声明已核对；没有重跑 Tauri 的多状态视觉验收 |
| [AgentBench](https://github.com/Whatnamed/AgentBench/tree/51fa2cb950e85dacbf5ff2ded70624d2c787969d) | `51fa2cb950e85dacbf5ff2ded70624d2c787969d` | `docs/product/product-spec.md`、`information-architecture.md`、`ux-spec.md`；`docs/design/README.md`、`visual-foundations.md`、`visual-qa.md` | **已确认目标 IA v2 / UX v2 和视觉方向，不代表 Windows UI 已实现或验收** |
| [Morpho](https://github.com/Whatnamed/Morpho/tree/8e10903a8ac1450849535514ade9e76229733938) | `8e10903a8ac1450849535514ade9e76229733938` | `docs/design/design-system/docs/DESIGN-SYSTEM.md`、`SOURCE-MAP.md`、`AGENT-BRIEF.md` | 这套文件声明基于已实现的旧版 Morpho 工作台；`SOURCE-MAP.md` 最后同步日期是 2026-07-26，原应用 commit 未记录，**不能证明与 2026-10 main 完全等效** |
| 三段历史聊天 | 第一轮私有整理档案 | 98 轮用户输入、97 轮助手输出；有脱敏候选规则与私有逐轮证据 | 38 张图片尚未完成逐张视觉核对；未经跨项目实证的规则仍是候选 |

**特别注意：Morpho 可能存在不同代际/版本的设计系统。** 用户另提到早期独立的 `Morpho Design System.zip`。本轮环境没有取得该 ZIP 的实际文件字节，所以**未进行 ZIP 与仓库版本的逐文件差异检查**。不得认为两套相同，也不得认为仓库版本覆盖 ZIP。取得文件后应分别建快照索引，按文件树、组件、Tokens、字体、页面布局、设计意图和源码映射比较，再决定哪些属于可复用设计系统交付样板。

## 2. 核验后更清楚的可复用原则

### 2.1 产品职责不等于视觉角色

- [ProxyLens 产品框架](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/PROXYLENS_UI_PRODUCT_INTERACTION_FRAMEWORK_v1.md) 明确声明它不是视觉规范；以 Scan / Review / Investigate / Explain / Verify 推导调查过程。
- [AgentBench IA v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/information-architecture.md) 与 [UX v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/ux-spec.md) 把「测试」设计为组内单题原位工作区，把「题库」设计为目录 + 可收起详情。外观可共用，认知任务不同，不可为代码复用强制统一交互。
- [AgentBench Design README](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/design/README.md) 明确冻结视觉参考来自 ProxyLens 的固定提交，**不继承其业务导航和 Inspector 语义**。

**可复用方法**：先指定每份权威文档的职责及冲突优先级，再决定可共享的视觉层；视觉迁移不是页面克隆。**非普适结论**：上述应用的具体导航名、栏目数、侧栏角色和布局尺寸。

### 2.2 信息状态要根据来源事实建模

- [ProxyLens 语义呈现](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/ui-semantic-presentation-v1.md) 区分 exact / estimated、不同 Unknown 成因、数据 Freshness、监控范围与观测缺口；无监控历史不等于 0% 覆盖。
- [AgentBench 产品规格](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/product-spec.md) 区分公开测试结果、探索性 AI 评审、客观判定和未知用量；不同 Task 版本的成绩不能盲目比较。

**可复用方法**：产出一份“领域事实 → 可展示状态 → 用户行动 → 异常/未知 → 核验依据”的对应表，设计前检查状态空间；不可直接复用别的产品的具体状态枚举。

### 2.3 字体/视觉迁移须查实际资源与真实渲染

- [ProxyLens fonts.css](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/ui/src/styles/fonts.css) 在该固定提交声明 Manrope、Sarasa Gothic UI SC 与 JetBrains Mono 的本地 WOFF2 face；[tokens.css](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/ui/src/styles/tokens.css) 明确字体的 narrative / mono 角色、权重及行高。
- 仅靠 CSS 声明仍不能判断实际 rendered font。字体资源是否存在、权重映射是否正确、中文 fallback 与运行环境的 DPI / WebView / 浏览器表现，都需要运行时检查。
- [AgentBench visual-qa](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/design/visual-qa.md) 明确不能将目标视觉标准、构建通过、浏览器预览或 WPF/Tauri 的真实验收混为一谈；对 Light/Dark、多窗口大小、长中英混排和多个业务状态分别测试。

**可复用方法**：提取视觉系统至少覆盖 Token 语义、文字角色、控件几何、Surface、图标、交互状态、页面密度与真实渲染证据。把平台差异列为例外条件，而不是强制复制像素数字。

### 2.4 不同设计系统案例必须保留各自代际

- [Morpho Design System](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/docs/DESIGN-SYSTEM.md) 将自己定位为映射旧版已实现的单画布工作台，强调画布对象、浮动控制簇与 AI 面板。
- [Morpho SOURCE-MAP](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/docs/SOURCE-MAP.md) 有源文件映射，但来源同步日期与应用版本需单独追踪。
- ProxyLens 是克制、精确、证据导向的桌面工作台。两者设计语汇和产品任务不同，不应合并成“个人统一审美”或强迫所有项目统一风格。

**待处理**：早期 Morpho ZIP 与仓库设计系统的关系应形成 `earlier-package` / `repo-snapshot` 两条来源记录，并在确证后标注 `same lineage` / `forked` / `independent` / `unknown`，禁止提前去重。

## 3. Skill 架构：先保留候选边界，不急于制作空壳

| 候选 Skill | 入口问题 | 独立产物 | 边界 |
| --- | --- | --- | --- |
| `product-discovery` | 产品目标和任务尚不清楚 | 目标、用户任务、对象、场景、边界、待确认假设 | 不预设 IA 或视觉 |
| `product-ia-interaction` | 产品范围已有，但页面/流程未定 | 页面职责、流程、跨页状态、异常、逐页行为合同 | 不直接替用户选视觉风格 |
| `product-ux-review` | 有方案需要反例/取舍/补漏 | 按用户影响分级的审查意见、采纳/拒绝/待评 | 不自动追加无意义功能或无限 polish |
| `visual-system-extract` | 有已验收视觉源需要提取 | 版本化视觉参考包、Tokens、组件、源码映射与证据 | 不声称未验收视觉已冻结 |
| `visual-system-adopt` | 产品 IA 已有，需要继承视觉 | 视觉角色映射、领域差异、实现边界、设计例外 | 不复制别家导航/业务组件 |
| `visual-qa` | 需要检查真实实现的视觉质量 | 场景矩阵、截图/渲染证据、差异与停点 | 不以纯静态检查代替实机验收 |
| `personal-ui-delivery` | Coding Agent 要实现已定设计 | 分阶段实现与回归要求、不可擅改事项、验收记录 | 不替代产品方案讨论、也不把项目日志写进 AGENTS |

这些只是**能力切分提案**，不是 7 个必须同时安装或强制串行调用的 Skill。已确认先按 Product & UX / Visual System 两个可打包组合与一个可独立维护的交付 Skill 讨论，后续可依据 Eval 合并重叠部分。

## 4. 下一步优先序与停止条件

1. **补齐 Morpho 早期 ZIP**：保留原包与仓库系统两个版本；只做来源核查、差异表和历史语义，不把任何历史设计宣称为现行 Morpho 产品方向。未取得 ZIP 前本项为 `blocked_input`。
2. **对最易误判的历史视觉反馈作证据复核**：字体 fallback、局部边界对齐、Surface、selected/hover/legend、Light/Dark；历史图片和运行时证据分开记录。
3. **建立少量可用模板**：产品任务与对象卡、IA/状态合同、视觉提取索引、视觉迁移差异与 QA 清单。模板必须可选，不让所有 Skill 都自动生成长篇文档。
4. **定义小规模对比 Eval**：同一 Prompt 分别用无 Skill 与候选 Skill 运行，检测遗漏、过度设计、错误继承、无根据 PASS、审查无限延长；有证据才能决定拆并。
5. 只有完成上述核对、确认触发边界和最少量的质量标准后，才晋升第一批正式 `SKILL.md` 或私人 Plugin。

**本阶段允许停止在“研究草案 + 可追溯来源 + 明确的欠缺证据”**，不以完成七份 Skill 文件的数量作为验收。
