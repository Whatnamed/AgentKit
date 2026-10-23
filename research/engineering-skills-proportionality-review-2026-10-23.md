# 工程 Skills 复核：最小有效审查、Bug 诊断、长任务与过度工程化

> 2026-10-23。针对个人在 ChatGPT 做设计决策、本地 Agent 做实现的工作方式。本文件是来源分析和取舍记录，**不自动向全部项目下发新指令**；正式可执行内容位于各 Skill。

## 本次决定

- **不制作 `decision-to-execution`**：它实际上重复了现有“讨论/规格定稿→独立执行文档（复杂任务）或短 Prompt→本地 Agent”过程。除非日后发现交接反复遗漏某类信息，否则只保留现有项目规范及按需模板，不新设硬门槛。
- **不制作 `context-continuity`**：仓库内 canonical 项目文档负责长期事实，网页 Handoff 负责窗口衔接；目前另加一层“记忆文档/Skill”容易重复、漂移。
- **已制作 `spec-and-diff-review` 与 `repro-first-debug`**：仅在真正审查或难问题诊断时调用，不作为每次小修复必须执行的关卡。
- **`knowledge-capture` 暂缓**：如果以后确实经常重复踩同类坑，可以借鉴 Every 的“已验证且未来会重新发现才写下来”；不规定每次任务结束强制 Retro 或新增文件。
- **Agent 跨宿主同步工具**后续单独考虑，不混入本轮 Skills。

## A. Karpathy 相关规则的真实身份与适用性

当前社区广传的 [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) **不是 Andrej Karpathy 本人写的官方 Skill**，是社区开发者根据他的公开 LLM coding 观点汇编的工程行为约束；对应仓库已提供 [`SKILL.md`](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md) 和 `CLAUDE.md`。Codex 移植另见 [richling98/karpathy-codex-skills](https://github.com/richling98/karpathy-codex-skills)。

最值得借鉴的四项：
1. **Think Before Coding**：不默默自选会影响结果的关键假设，但明确小问题无需长访谈。
2. **Simplicity First**：最小解决问题；避免未要求的选项/兼容层/配置/抽象/无实际风险的异常分支。
3. **Surgical Changes**：变动行应能追溯到需求、必需的安全修复或真实测试；不“顺手”大规模清理。
4. **Goal-Driven Execution**：有可观察的完成标准，实施后验证真实结果。

**局限：**该仓库仍倾向“先测试再实施”的举例与“谨慎优于速度”，不能从它得出“禁止测试”的结论。对于已有较成熟工程环境，更适合将其**简单性与变更边界原则**融入特定的审查/调试 Skill，而不是全局叠加一份口号式约束。Karpathy 本人维护的 [autoresearch](https://github.com/karpathy/autoresearch) 是针对特定可测量 ML 实验的有界自动循环，**不是**一套通用软件工程或反防御性编程 Skill。

## B. 社区抱怨确有具体指向，但不是所有测试和备份都有害

已查阅以下一手问题报告和社区经验：

- [openai/codex #39059](https://github.com/openai/codex/issues/39059)（2026-08-17）：报告有限任务被自行添加的哈希、签名、快照、恢复/审批流程等扩大；这些新机制又自带 schema/迁移/持久化/测试/文档，再成为自己存在的“证明”。其关键问题是**缺独立需求与真实消费者**，不是这些机制本身不安全。
- [openai/codex #35593](https://github.com/openai/codex/issues/35593)：报告普通 UI 变更后已经过针对性测试，Agent 仍执行完整耗时 UI 套件。应按受影响路径与发布阶段选择验证强度。
- [openai/codex #44081](https://github.com/openai/codex/issues/44081)：用户报告简单问题触发不相关 Skills，额外消耗时间/上下文；Skill 应以**用户要求的动作**而非关键词自动触发。
- [openai/codex #32406](https://github.com/openai/codex/issues/32406)：报告 GPT-5.6 搭配 Superpowers 时可能反复重做规划，不进入实施；强调外部框架在特定模型/宿主存在兼容风险。
- [r/codex 过度工程化讨论](https://www.reddit.com/r/codex/comments/1wke0yr/gpt_usually_leaves_so_many_useless_overenginered/) 与 [用量消耗讨论](https://www.reddit.com/r/codex/comments/1wld40n/i_spent_last_week_livid_at_how_quickly_i_burnt/)：有用户提出极端“别写测试/校验”，也有用户指出后续必须补高价值场景检查。此为**用户反馈，不是实证证明**。
- [r/codex 过度抽象](https://www.reddit.com/r/codex/comments/1vf5elq/how_do_you_stop_codexclaude_from_overengineering/)：社区报告简单任务被扩大成类型重构、配置、附加状态和模拟测试。

### 对自己更适合的精确定义

**保护机制要有现实依据**。新增防御性分支、持久化、签名、快照、重试、备份、测试、文档、迁移，应至少能回答：
- 谁真正依赖这个结果？哪种**受支持**的输入/故障/信任边界需要它？
- 已有 Git、数据库事务、框架、CI、API 或数据源是否已经解决？
- 若保留它，将产生多少新的状态与维护义务？是否值得？
- 如果删除它，会使真实用户功能、安全/隐私/数据完整性哪部分退化？

### 测试并非越少越好，而是“有效且足够”

| 变更 | 通常可用的最小验证 | 什么情况下扩大 |
| --- | --- | --- |
| 文案/很小的静态 UI | 直接核对可见结果与构建必要项 | 有共享组件影响、正式发布前的专项门禁 |
| 局部逻辑或组件 Bug | 现有定向测试/真实复现场景 + 相关类型检查 | 改动涉及共享状态、回归影响多页 |
| 数据库/迁移/持久化 | 核实数据完整性、兼容/恢复边界，执行项目要求的迁移/事务验证 | 真实数据、安全、跨版本或不可逆风险 |
| 权限/安全/支付/隐私 | 明确边界和重要失败路径的强验证，不能以节省 token 跳过 | 多角色/环境/协议连锁风险 |
| 发布/发行候选 | 仓库既有明确 release check 和真实目标宿主验证 | 按项目发布制度，而非普通开发每轮全跑 |

- 重复运行同一 suite 只在修复失败、环境改变、影响范围扩大、结果不可靠时有意义。
- 依赖安装、备份目录、临时工作树、预检报告和“证明文件”也会形成维护负担；只在用户要求或现实风险/环境约束有据时新增。
- **不能**用“禁止一切验证”误伤真实需要的安全/事务/并发/回滚检查；更不能主动清理用户既有备份或放宽项目禁区。

## C. 长任务：大佬们的方法与本用户的实际取舍

| 来源 | 有价值的技术 | 与现有模式结合 |
| --- | --- | --- |
| [Matt Pocock to-tickets](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md) | `tracer bullet` 垂直切片，每片尽量可独立验证；显式 blocking edge | 在复杂执行文档中列任务依赖及每片可观测产物即可，**不强制建 GitHub Issues** |
| [Matt code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md) | Spec 与 Standards 两轴，不让风格与需求符合性混为一谈 | 新建 `spec-and-diff-review` 精简实现；不强制两个并行审查 Agent |
| [Matt diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md) | 复现症状→缩小→假设→少量 instrumentation→修复→原症状回归 | 新建 `repro-first-debug`，但明显 bug 可直接查改，不必每次造 harness |
| [Every Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | 已验证的改变才沉淀非显而易见的经验 | 需要时写到正确的既有文档；没有经验增量则不写 |
| [GSD Core](https://github.com/open-gsd/gsd-core) / [Superpowers](https://github.com/obra/superpowers) | 分阶段执行、上下文隔离、计划/验证与 Handoff | 大型任务可用独立执行文档、阶段基线和短启动 Prompt；不按框架固定里程碑 |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | 本轮变更合同独立于稳定规格 | 现有 Product/IA/UX 与 STATUS/执行文档职责已足够，不引入新的 `openspec/` 平行权威 |

### 对复杂任务的具体建议

- **清楚的小修复**：直接做，不分任务不建新计划。
- **可在一个会话内完成的功能**：一份短边界与验收说明，当前 Agent 完成、定向检查即可。
- **需多个会话/复杂前后端**：独立执行文档记录当前基线、已定产品/架构决定、模块/接口依赖、可验证的纵向阶段、受影响范围与禁区、必要测试、停止条件；启动 Prompt 只引文档路径。
- **跨 Agent 并行**：仅在改动互不冲突、有清楚工作树/分支与独立验收时使用；否则串行更省沟通和合并风险。
- **横跨全仓库的机械迁移**：不应强行拆成会使中途代码不可构建的垂直功能片，适用 expand–migrate–contract 或受控批次。
- **无人值守**：允许局部自主工程决定，无法自行判断的不可逆产品/安全/架构变更成为受影响范围的 blocker，其余安全工作继续，真实结果可从 Git 与项目文档恢复。

## D. 为什么当前不再新增更多 Skills

本轮新增：
- [spec-and-diff-review](../skills/spec-and-diff-review/SKILL.md)
- [repro-first-debug](../skills/repro-first-debug/SKILL.md)

未创建新 Plugin/总控 Agent；也没有把四条 Karpathy 原则再做第三个“反过度工程化 Skill”，避免 Skill 本身成为被反对的额外负担。它们已经在这两个 Skill 中有具体运用；现有 `personal-ui-delivery` 也已有范围、必要验证和有界文档同步原则。

待未来真实工作暴露新的重复问题时，再考虑是否需要面向全编码任务的精简全局规则或命令；但**不直接覆盖各仓库现有 AGENTS.md**，也不把历史研究草案当成已生效规范。
