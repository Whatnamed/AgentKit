# 设计系统提取检查与证据等级（按需读取）

这不是必须逐项全部产出的 checklist。仅依任务、源码规模与使用目的展开，避免系统化文档比实际产品还大。

## 交付覆盖维度

| 维度 | 重要检查 | 只有概念图时如何处理 |
| --- | --- | --- |
| 身份与目标 | 产品气质、视觉原则、密度与层次选择理由 | 描述“方向”，不声称已落地 |
| 主题/颜色 | 语义 Token、Light/Dark、文字和状态、焦点 | 截图取样仅为近似，不写精确实现值 |
| 字体 | 来源文件、字形覆盖、真实权重、fallback、行高、Mono/叙事角色 | 标记字体识别和实际渲染均待查 |
| 布局/空间 | Page/Section/Item/Metadata 角色、间距层级、边栏/Inspector、溢出 | 不把单张图的尺寸当响应式合同 |
| 组件 | 结构、可变属性、状态、交互、组合、长内容 | 推断需标注为设计假设 |
| 资产/图标 | 包装路径、授权、命名、图标风格与尺寸 | 若无法取得授权资产，只提供概念说明 |
| 动效/可访问性 | focus、hover、selected、disabled、busy、reduced motion | 静态参考无法证明行为 |
| 运行与 QA | 目标宿主、视窗/DPI、主题/语言、异常与截图证据 | 记为未验证，不标 PASS |
| Source Map | 每项设计声明到代码、文档、实际验证证据 | 没有源码写“无源码可核验” |

## 证据等级

- `documented`：设计文档有声明，但不代表代码或真实运行支持。
- `source-confirmed`：目标提交的实际源码/资源包含相应配置或实现；仍不能证明视觉呈现正确。
- `runtime-observed`：明确环境中看到或测到相应效果；记录环境、日期、状态与截图/测试结果。
- `human-accepted`：有明确验收人、标准、范围及证据。其他项目的验收不能直接迁移。
- `unverified` / `not-modelled`：无法核实，或源系统尚未覆盖。

证据可以并列记录；不要因为看到 CSS 字体名就断言浏览器实际加载，亦不要把“生成过预览图”当真实组件验收。

## 值得检索的公开案例

- [Morpho design-system README](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/README.md)：设计系统资料如何从独立项目导出到仓库；组件含 JSX、类型和逐组件 Prompt，Token 分层，并有已知未纳入 UI Kit/规范卡片的说明。
- [Morpho design system](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/docs/DESIGN-SYSTEM.md) 与 [SOURCE-MAP](https://github.com/Whatnamed/Morpho/blob/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system/docs/SOURCE-MAP.md)：记录旧版已实现的工作台及源码映射，但不能证明 2026-10 运行时完全一致。
- [ProxyLens Frozen v1 design system](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/design/PROXYLENS_UI_DESIGN_SYSTEM_v1.md) 与 [implementation/QA](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/design/PROXYLENS_UI_IMPLEMENTATION_AND_QA_v1.md)：另一种密度、表面和视觉角色的设计系统；冻结标准与实际验收证据仍需分开记录。
- [AgentBench visual foundations](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/design/visual-foundations.md)：有条件继承 ProxyLens 的视觉基础，却不继承其网络审计业务布局；当前仍属目标视觉标准。

Morpho 的 Claude Design 系统在 ProxyLens 项目中主要提供**设计系统组织、完整性与交付方法**层面的参考。这不等于这几个产品本身是相同的视觉样式。
