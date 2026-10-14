# UI 视觉词汇、专业设计维度与“看着不对”的诊断

`visual-system-create` 在**选择方向、从零建系统、用户用日常语言反馈问题**时按需读取；`visual-system-adopt` 应有自己对应的适配检查。词汇帮助 Agent 主动分析，不要求用户使用术语，也不暗示某种固定美学风格一定正确。

## 先说感觉与功能，再找设计原则与变量

参考 VS Code 公开设计方法“Values → Principles → Moves”：先辨识页面想表达何种气质、当前感受被什么破坏；再判断信息层级、空间关系、视觉对比的原则；最后才选择字体角色、间距 Token、表面层级和组件参数。这个方法比让用户报“加 2px”更适合定位系统性问题。

| 用户可能会说 | 设计术语 / 关注点 | 先看什么，再决定改哪里 |
| --- | --- | --- |
| “乱、没重点、像把控件堆一起” | Visual hierarchy、emphasis、information density、scannability | 主任务是否突出，Page/Section/Item 的文字与空间层级，数据密度 vs 辅助 chrome；先判断是否产品结构问题 |
| “挤、闷、没呼吸感” | Negative space / whitespace、spatial rhythm、proximity | 组内 vs 组间距离，容器 padding、行高、模块边界；不直接全局放大所有 gap |
| “太空、松散、不像工具” | Density、vertical rhythm、content grouping | 实际内容量、列表行高、分区与控件距离，是否被空卡片/副标题撑高 |
| “文字飘、垂直不齐” | Baseline、font metrics、line box、optical alignment | 真实字体/fallback、字重、line-height、图标 viewBox、flex alignment；几何中心与视觉中心不同 |
| “字体不协调” | Typeface roles、type scale、font weights、measure、CJK fallback | 中文/英文/Mono 各角色，字符覆盖、字重映射、字宽、数字对齐、段落长度；不是只换 font-family |
| “列表之间没有归属感” | Proximity、grouping、separator、hierarchy | Item 内/Item 间/Section 间相对差异，列表分隔线、状态与标题权重 |
| “好像没层次，全是同一种面板” | Surface hierarchy、elevation、inset/raised、layering | Canvas/Workspace/Sidebar/Panel/Overlay 层级、边框与阴影的语义，不靠给每个模块加卡片 |
| “高亮太吵，重点不明显” | Salience、contrast、accent budgeting、visual affordance | 主操作、选中态、hover、focus、业务状态是否争抢颜色或权重 |
| “两个页面看起来不像一个产品” | Visual consistency、semantic tokens、components/patterns | 相同角色是否使用相同字号、边界、色义、控件规格；差异有无明确产品原因 |
| “换成别的尺寸/深色就坏了” | Adaptive layout、responsive typography、theme semantic parity | 内容溢出、换行、最小宽度、浮层定位、Light/Dark 语义 Token 与对比度 |
| “动效怪、操作反馈不明确” | Motion hierarchy、interaction feedback、reduced motion | 动效是否表达状态/空间变化、是否打断任务、焦点与结果是否确切 |

这些是**诊断入口**，不是唯一原因或自动修复处方。尤其产品 IA 与视觉表现互相影响时，先说明根因归属，再改设计。

## 设计系统成品应包含哪些“层”，而非只有主题色

### 1. Foundations / 原则
- 设计目标、品牌气质、使用环境与信息密度策略；哪些东西应突出、哪些应安静。
- 主题与模式：Light/Dark、高对比/低动效（如目标平台适用）；不同语言与窗口尺寸。

### 2. Tokens / 视觉变量
- 原始量尺（primitives）与含义明确的语义变量（semantic）；按复杂度可增加组件级 token（component）。
- 颜色不只是品牌色：文字/背景/Surface/边框/交互状态/焦点/错误警告/图表。
- Typography：font families/source/license、CJK/Latin/Mono fallback、字阶、字重、行高、字距、可读宽度。
- Spatial system：栅格、页面边距、Section/Group/Item/控件内外距离、密度与尺寸、组件最小/最大宽度。
- shape/radius/border/elevation/shadow、iconography、motion/duration/easing；按任务支持的资产和图像规则。

### 3. Components / 模式
- 每种真正需要的控件记录用途、解剖（anatomy）、parts/slots、变体/尺寸、所有相关状态、键盘与焦点、内容多寡、主题、组合、使用/禁用场景。
- 组件是 Button/Input/Row 等可复用件；**Pattern** 是用户任务方案（筛选、检索、提交、验证错误、完整编辑流程等），由一个或多个组件组成。页面 **Template** 是某种功能页面的结构样板，不等于所有产品套同一布局。

### 4. Handoff / 维护
- 定义代表页面与关键状态如何应用规则；组件到代码/设计文件 Source Map、可用资产及许可、已验证和未验证范围、变更及例外的唯一权威。
- 规格、可运行组件和验收之间能互相定位，才能减少后续 Agent 凭感觉调整。

## 参考资料与适用边界

- [Microsoft VS Code — Design Philosophy Skill](https://github.com/microsoft/vscode/blob/main/.github/skills/design-philosophy/SKILL.md)：设计反馈从目标、原则到具体做法的推理路径。其 Calm/Focused 等价值与 Token 数值属于 VS Code，不要求所有项目照搬。
- [IBM Carbon — Spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview)：空间不仅是 margin/gap 数值，还承担关系、层级和密度的表达。
- [Atlassian — Spacing](https://atlassian.design/foundations/spacing)：小/中/大空间用途与命名尺度的示例，不应强制别的产品使用 8px Base。
- [Impeccable](https://github.com/pbakaus/impeccable)：细分 Typography/Color/Spacing/Layout/Interaction、按任务读取参考和设计反模式；风格建议不可当成无条件美学规则。
- [W3C Design Tokens Community Group](https://github.com/design-tokens/community-group)：视觉变量互操作的标准化方向；没有要求所有个人项目采用同一规模或每个层级必做。
- [WAI APG](https://www.w3.org/WAI/ARIA/apg/patterns/)：组件行为和可访问性模式，具体平台仍需适配。
