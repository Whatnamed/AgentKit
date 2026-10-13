# 产品 IA 的证据与状态检查（按需参考）

仅在涉及多源规格冲突、事实性状态、跨页转换或异常时读取；不把此文件当作每次必填问卷。

## 证据分层

| 类别 | 典型证据 | 用法 |
| --- | --- | --- |
| 用户确认的目标 | 当前决定、明确否定/替换的旧决定 | 作为目标产品行为；记下日期和适用范围 |
| Canonical 产品/UX 规格 | 有权威关系和版本的项目文档 | 用来判断目标页面与行为；留意“尚未实现” |
| 当前真实实现 | 对应提交、运行中 UI、API/数据模型 | 用来判断现在能否实现、目前有哪些偏差 |
| 源视觉参考 | 可追踪的样式、组件、截图/设计系统 | 用来参考外观，不应决定业务对象或页面 IA |
| Agent 建议或执行日志 | 草案、测试报告、临时方案 | 先核实再晋升；不是用户已确认 |

不要机械排序“文档永远高于代码”或反过来。**目标权威**与**当前实现事实**必须分别写清楚，发现冲突后指出处理方式。

## 状态矩阵最小字段

对每条关键流程检查：

- **事实来源**：状态由谁产生、是否实时、有无证据等级或权限限制？
- **状态含义**：Empty 是真的没有，还是尚未查询/不可用？Unknown 与 Error 是什么？正在运行是否能被系统核实？
- **用户动作**：此状态允许做什么、不能做什么、下一步在哪里？
- **上下文持续性**：过滤条件、时间窗、选中项、侧栏展开、正在编辑内容在跳转/刷新/恢复后怎样变化？
- **危险与不可逆**：删除、覆盖、清理、提交是否有清楚范围和确认？如何回退？
- **可访问与窄屏**：键盘焦点/可辨识选中/长名称/缩放导致操作被挡住时怎么处理？

## 已核查的来源案例（不要移植业务规则）

- [ProxyLens — UI Product & Interaction Framework v1](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/PROXYLENS_UI_PRODUCT_INTERACTION_FRAMEWORK_v1.md)：以调查路径组织页面、上下文与 Inspector；文件声明不是视觉规范。
- [ProxyLens — UI Semantic Presentation](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/ui-semantic-presentation-v1.md)：区分真实数值、估算、监测缺口和 Unknown 的不同成因。
- [AgentBench — IA v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/information-architecture.md)：测试执行页与题库目录虽共享视觉语言，但分别采用原位展开与 List–Detail；当时属于目标 IA，非已验收运行 UI。
- [AgentBench — UX v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/ux-spec.md)：当前组身份、切组与 Chevron 展开是不同操作。

这些来源只证明对应项目在指定版本的决策，不会自动变成其他项目的统一页面模板。
