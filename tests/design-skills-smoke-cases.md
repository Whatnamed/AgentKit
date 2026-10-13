# 两项设计 Skill 的第一轮 smoke / 对照评估

> 状态：**测试案例已编写，尚未执行独立模型对照或真实视觉验收**。该文件是测试设计，不是已经通过的测试报告。
> 日期：2026-10-13。范围：`product-ia-interaction` 与 `visual-system-extract` 两个原型。

## 使用方式与计分

对每个案例至少运行两组：**相同模型、相同输入/来源**下无 Skill 的 baseline，以及明确启用目标 Skill 的版本。保存模型与环境、日期、输入、读取的来源版本、输出；对照后由人检查。不要用本文件的“预期”代替运行结果。

每一项按 0（失败）/1（部分达到）/2（达到）打分。除了覆盖目标任务，还评估：是否凭空补产品事实、是否照搬源页面、是否堆无意义辅助文案、是否无证据声称已验收、是否把简单任务膨胀成一整套模板。出现严重无证据 PASS 或泄露私有材料应直接判为阻塞。

## A — 不同页面职责（IA，正向）

**用户输入**：已存在 Windows Coding Agent 测评工具，用户可以组织独立测试组，单题执行与提交；另有长期题库可检索、查看不同版本。设计「测试」和「题库」的页面职责、典型流程、侧栏角色与上下文恢复。请说明为何不能强制复用同一页面布局。

**可用依据**：[AgentBench IA v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/information-architecture.md) + [UX v2](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/product/ux-spec.md)。

**预期**：测试是组内原位工作区，题库是目录 + 可收起详情；选中/展开、切组/恢复分离；明确目标规格尚未全部验收。

**警戒失败**：为二者强推同一“列表点开”范式；在页面 IA 未定时强行用外观模板决定结构；捏造当前运行 PASS。

## B — 复杂状态和事实来源（IA，正向）

**用户输入**：设计一个分析面板，数据可能没有被采集、采集已中断、聚合尚未完成，数值可能是实测或估算。给出必要页面语义、状态及用户能够执行的操作，不要只设计一张漂亮图表。

**可用依据**：[ProxyLens 语义呈现](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/ui-semantic-presentation-v1.md)。

**预期**：区分未知、空、观测缺口、陈旧、估算和精确等来自源规范的不同语义；解释哪些属于特定产品事实而不是所有产品通用枚举。

**警戒失败**：把没数据显示为 0%、将 estimated 写成 exact、把所有错误统一成 Empty。

## C — 设计系统提取的完整度（Visual，正向）

**用户输入**：请以指定 Morpho `docs/design/design-system/` 快照建立给另一个设计 Agent 使用的来源索引。不要先生成新界面，说明能提取哪些系统层次、组件契约、缺失哪些真实运行证据。

**可用依据**：[Morpho 设计系统仓库版](https://github.com/Whatnamed/Morpho/tree/8e10903a8ac1450849535514ade9e76229733938/docs/design/design-system)。

**预期**：覆盖设计规范、Tokens、组件族、类型声明、逐组件 Prompt、SOURCE-MAP、资产/字体及导出约束；识别导出包未包含独立设计项目中的 `guidelines/` 与 `ui_kits/`；不把该快照与 2026-10 运行时等同。

**警戒失败**：只摘色值/字体；宣称导出包已包含完整原始 UI Kit；复制源码无授权分析；将未运行的组件判为已验收。

## D — 视觉提取不能替代 IA（Visual，反向）

**用户输入**：我喜欢 ProxyLens 的视觉，但给一个完全不同业务的产品开发界面。先提取可用设计语言，能不能把 ProxyLens 的 Overview/History/Inspector 布局原封不动作为新产品 IA？

**可用依据**：[ProxyLens 设计系统](https://github.com/Whatnamed/ProxyLens/blob/f7ef34698533f741905bac0a1d554175eab8c0b4/docs/design/PROXYLENS_UI_DESIGN_SYSTEM_v1.md) + [AgentBench visual foundations](https://github.com/Whatnamed/AgentBench/blob/51fa2cb950e85dacbf5ff2ded70624d2c787969d/docs/design/visual-foundations.md)。

**预期**：明确可以继承视觉角色，但宏观布局由新产品任务、对象、IA 决定；来源证据不支持的目标业务要求不能假装已定义。

**警戒失败**：只因已有组件或便于复用就搬运 ProxyLens 审计语义和页面结构。

## E — 信息不足与节制（两项都应通过）

**用户输入**：我只有一张界面截图，没有源码、字体文件、组件状态或产品功能列表。请帮我做一套完整、已验收的设计系统，顺便确定页面 IA。

**预期**：保留可观测的视觉方向，标注字体、真实交互与响应式不可证实；没有用户任务/对象不能确认 IA；只产出有依据的部分，指出最关键缺口。

**警戒失败**：从静态截图硬造精确 Token、真实 font-family、功能合同、Light/Dark 验收，或为了“完整”输出冗长空壳模板。

## F — 局部请求不扩大范围（两项都应通过）

**用户输入**：只需要帮我判断这张列表里“选中项”和“展开详情”是否应该是同一个状态。不要重做整个界面。

**预期**：给出适用条件、独立状态及操作反馈；答复简明，没有完整产品定义、全部页面表或视觉系统提取。

**警戒失败**：忽略“只判断局部”并强制生成产品 PRD 或设计系统包。

## 运行记录模板

| 案例 | 模型与环境 | 无 Skill 评分 | Skill 评分 | 变化证据 | 阻塞/延期 |
| --- | --- | ---: | ---: | --- | --- |
| A–F | 未运行 | — | — | — | `not-run` |

**验收决定**：只有积累至少一轮真实对照输出与人工打分，才能决定是否把原型标为 accepted，或合并/拆分 Skill。静态文件可解析 ≠ 实际使用效果良好。
