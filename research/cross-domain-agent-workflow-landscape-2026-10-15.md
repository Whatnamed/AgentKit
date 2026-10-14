# 个人 Agent 工作流：知名开发者 Skills / Frameworks 广度研究（第一轮）

> 日期：2026-10-15 · **研究与架构候选，不是 AgentKit 新的正式工作流或已安装 Skills**。范围从 Product/UI 扩展到工程开发、架构、调试、审查、持久化上下文和多 Agent 协作。只从公开源仓库、明确的使用实践推导方法，避免把作者宣传数字当独立质量证明。

## 1. 为什么研究这些，而不直接装完整框架

目标是建立一套**用户自己的跨项目方法**：网页 ChatGPT 讨论需求、产品/UX、视觉、架构和复审；本地 Codex/Agy/OMP 等 Coding Agent 在项目仓库中实现与验证；GitHub 保持源码和关键项目证据可追踪。只在确实需要时调用额外 Skill。

约束来自已形成的协作习惯：
- 小问题简单 Prompt 即可；大任务用项目内独立执行文档 + 极简启动 Prompt，避免凭“流程规范”自动生成冗长 Plan。
- 已确定产品/UX/关键架构才交给实现 Agent；工程实现细节可以合理自主，不反复询问。
- 日常主工作树+任务分支，只有并行/需隔离/保留现场时才开 worktree；并行比较须明确独立基线和提交归属。
- 先看**实际 Git diff / 测试和运行证据**，再 accepted、合并、清理；不捏造通过、不做无意义 audit→fix→audit。
- 每类文档有单一职责：AGENTS 是稳定规则，产品/UX/设计系统是目标，STATUS/Devlog 是现状，Prompt/Plan 是单次执行，网页 Handoff 不是仓库永久进度。
- 可能需要无人值守，不确定且不可逆的事项应保留为 blocker，允许安全独立部分继续；不要无限等用户确认。

**原则：流程深度取决于不确定性、风险和可验证性，不主要取决于代码行数。** 这不是所有框架的共同规定，而是对本用户更合适的综合建议。

## 2. 主要来源：原始项目与固定快照

| 项目/作者 | 固定仓库快照 | 亲自核对到的代表做法 | 哪些值得借鉴 | 不直接照搬 |
| --- | --- | --- | --- | --- |
| **Matt Pocock — Skills for Real Engineers** | [mattpocock/skills@49dd158](https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336) | [ask-matt](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/ask-matt/SKILL.md) 的动态流程路由；[grill-with-docs](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/grill-with-docs/SKILL.md) 引导澄清并记录术语/ADR；[to-spec](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-spec/SKILL.md) 汇总已讨论决定，不再重复问；[to-tickets](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md) 做可验证纵切与阻塞边；[code-review](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/code-review/SKILL.md) 分规范/目标两轴；[retro](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/retro/SKILL.md) 改善环境而非无端加规则 | 单一领域词汇、极少量难逆 ADR、长任务可独立完成的纵切任务、双轴 diff 审查、只提升确有反复价值的环境规则 | 全部任务强制“grill→spec→tickets→review”、每个小修复都建 Issue/TDD、每项决策都等用户确认。仓库现行文件使用 **GLOSSARY.md**，旧教程的 CONTEXT.md 叫法可能已过时 |
| **Kieran Klaassen/Trevin Chow — Every Compound Engineering** | [EveryInc/compound-engineering-plugin@7a68002](https://github.com/EveryInc/compound-engineering-plugin/tree/7a68002fc24139fe4876c759c9e5a3ebff976ad4) | brainstorm→plan→work→simplify→review→compound 的闭环；[ce-compound](https://github.com/EveryInc/compound-engineering-plugin/blob/7a68002fc24139fe4876c759c9e5a3ebff976ad4/skills/ce-compound/SKILL.md) 仅在结论“已经真实解决、代码中不易重新发现、未来有复发风险”时保存；review 可按风险选择审查深度 | 高价值经验才入库；领域规则不重复；任务完成后的轻量提炼；独立审查的权限边界 | 默认完整六步、所有任务多模型审查、无谓 solutions 文档与持续回顾 |
| **Jesse Vincent — Superpowers** | [obra/superpowers@bb92a77](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3) | 从需求澄清→设计确认→Implementation Plan→子 Agent 执行→测试/复审；强调验收与可独立完成的任务 | 复杂项目需要清晰目标、实现计划、反馈回路；编码者不擅自改未定产品决策 | 对小任务自动启动长访谈、强制全过程 TDD 或子 Agent 链；与既有网页规划岗位重复 |
| **Garry Tan — gstack** | [garrytan/gstack@15ebd85](https://github.com/garrytan/gstack/tree/15ebd85cdde6c9a1b2fb707e8573aec18e8f7438) | 产品价值审查、工程设计审查、视觉设计审查、真实浏览器 QA、代码审查与 ship 拆角色 | “计划中应描述用户真实看到/做什么”；工程、产品、体验复审各自有不同问题；需要证据的真实页面 QA | 宣传性的产出倍数、每次打分/全部角色全开、强制大型 QA 与自动发行、把私人项目当创业组织 |
| **Peter Steinberger — agent-scripts** | [steipete/agent-scripts@bf4d15a](https://github.com/steipete/agent-scripts/tree/bf4d15ab265aa6a4d844701f377ee7b1a6d68ca7) | 一个 canonical Skill/AGENTS 源仓库；映射到 Codex/Claude；短 Skill 描述用于路由；脚本与 hooks 只处理确定性的重复动作 | **和 AgentKit 最直接适配**：一份源码，平台入口/分发适配，AGENTS 稳定规则，Skill 本体短而明确，复杂步骤按需参考 | 其 macOS Bash/symlink 位置与个人项目细节；在 Windows 需独立验证安装与入口语义，不能照搬脚本 |
| **Fission-AI — OpenSpec** | [OpenSpec@9111a76](https://github.com/Fission-AI/OpenSpec/tree/9111a7654d7800391459431fff4eaf66e33a3d2e) | proposal / specs / design / tasks / apply / archive；特别强调已存在代码的变更、按场景的需求描述与变化归档 | “本轮变更合同”与“长期产品规格”分离；可选的新增/修改/删除行为记录、版本一致性 | 所有项目强制新增 openspec 目录/统一归档和安装 CLI；AgentKit 已有项目文档职责 |
| **GitHub — Spec Kit** | [spec-kit@51b6d17](https://github.com/github/spec-kit/tree/51b6d170aa7368205bee629d75a7059185272d19) | 独立的 Spec-Driven 开发、Bug fixing、Idea assessment 入口；constitution→specify→plan→tasks→implement→converge 按能力调用 | **问题类型路由**比所有任务走一个大流水线更合适；变更完成应回查最初需求 | 每个任务重复 constitution、规格和多轮 converge，或默认引入完整目录/工具链 |
| **BMad Method** | [BMAD-METHOD@8f0d50e](https://github.com/bmad-code-org/BMAD-METHOD/tree/8f0d50e1817fdd8fcf05a20c524218222d13cd8d) | Product/UX/Architecture/Dev/Test 的角色分工，流程按任务规模可伸缩，支持现存代码和新产品 | 角色与产物责任清楚；不用一个 Agent 同时“擅自做完所有取舍”；关注历史代码库现实 | 大团队敏捷角色/大量重复模板；当前 main 自述 V7 为预览版、V6 为稳定版，不能不固定版本就全盘安装 |
| **open-gsd — GSD Core** | [gsd-core@1b362a1](https://github.com/open-gsd/gsd-core/tree/1b362a1f688ce35d88594b535c50db36536d9e68) | Discuss→Plan→Execute→Verify→Ship，每个复杂任务/阶段可由干净上下文执行，状态与决策文档持续跨会话 | 跨窗口/跨 Agent 的明确交接、阶段性证据和 context freshness；无人值守分段执行 | 每项任务都建 milestone/roadmap、所有计划固定为 200k 上下文，或复制项目不兼容的执行配置；先核实仓库及包来源 |
| **Andrej Karpathy — autoresearch** | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 小范围可修改文件 + 固定运行预算 + 可重复比较指标 + keep/discard 回路，`program.md` 即 agent 长程任务说明 | 仅对**结果可测量、操作有界、重复实验有意义**的任务考虑 unattended 优化；不用每次都唤醒人类 | 这是特定 ML 训练研究，不是通用的软件开发方法，不能把“自主循环”直接套到主产品 UI/架构上 |

以上对项目的描述来自对应仓库 README 与上述代表 Skill；不声称已在用户的 Windows 系统上安装、运行或验证这些外部框架。

## 3. 社区使用反馈：没有唯一最佳整套框架

- [r/ClaudeCode · 按任务大小选工作流](https://www.reddit.com/r/ClaudeCode/comments/1wmax2u/whats_your_actual_claude_code_workflow_by_task/)（2026-09-21）：有人日常坚持 Matt / Superpowers；也有人反馈小功能耗在规划、重复 review 上，倾向“小 bug 直接修、大功能才拆 Spec”，并强调新上下文、有限并行与真实停止标准。
- [r/claudeskills · Matt、Superpowers、OpenSpec 混用](https://www.reddit.com/r/claudeskills/comments/1wwqyom/matt_pocock_superpowers_openspec_do_you_pick_one/)（2026-10-03）：存在“组合抽取模块”和“现代模型上过多流程浪费 token”的争论，不能当成安装越多越好。
- [r/claudeskills · 日常 Skills](https://www.reddit.com/r/claudeskills/comments/1we3ktn/claude_code_power_users_what_custom_skills_are/)（2026-09-12）：有用户只保留极少数高频 Skills，例如代码提交复审与最小 bug 复现；这是个人经验而非普遍统计。

社区意见仅用于识别流程成本与可能的失败模式，不应当作工具有效性的定量证明。

## 4. 面向 AgentKit 的推荐形态（**候选，不是正式实施**）

不建议立刻再建一个“AgentKit Mega Agent”或安装 GSD+BMAD+Matt+Superpowers 的全套集合。已有的 Product/UX、Visual System 和独立 `personal-ui-delivery` 仍保持原职责。

更适合的**跨项目入口 + 少量工程 Skills**：

| 层 | 未来候选 | 实际负责的事 | 借鉴来源 / 与旧能力边界 |
| --- | --- | --- | --- |
| 入口/路由 | `workflow-router`（可为轻量 Skill 或 README/命令） | 判定产品讨论、视觉、实施、故障、复审、交接、经验沉淀该走哪条短路径；用户明确点名 Skill 时不改道 | Matt 的 ask-matt；不复制所有步骤到入口，也不自动强制执行 |
| 讨论→执行桥接 | `decision-to-execution` | 根据**已经确认**的产品/UX/架构决定与实时仓库事实，生成可执行边界、验收和阻塞，简单任务用短 Prompt，复杂任务给独立执行文档+启动 Prompt；不重复访谈用户 | Matt to-spec/to-tickets、OpenSpec、GSD；与 `product-ia-interaction` 的目标规格分工 |
| 工程诊断 | `repro-first-debug` | 对难以复现的 bug/回归先建立最短可失败反馈，再定位根因与有界修复；有简单明确问题时可直接修 | Matt diagnosing-bugs；不对每个 typo 强制建 harness |
| 执行成果复审 | `spec-and-diff-review` | 独立核对**是否实现约定**与**是否符合工程/安全规范**，列出真实证据和阻塞；只改明确授权的内容；无重要问题即可收口 | Matt 双轴、Every 风险分级；与现有 personal-ui-delivery 的执行/局部自检不同 |
| 跨窗口连续性 | `context-continuity`（可能是模板+规则而非 Skill） | 记录窗口进度/下步阻塞，与项目的 canonical 产品/状态文档分开；压缩/切模型/换 Agent 后能恢复上下文，不抄长聊天 | GSD、Matt handoff；已有窗口 Handoff 规范时应复用不再造 |
| 经验沉淀 | `knowledge-capture` | **真实解决且将来可能重犯**的经验才写入现有文档、自动测试或 Skill；已有代码能说明的不新增文档 | Every ce-compound、Matt retro；不是“每次任务结束自动写复盘” |

**可选实验性能力**：独立 Agent/worktree 比较或长期有界批处理，只在真的有清晰比较指标、互不争用数据、能验收与回滚时开展。可以借鉴 GSD 与 autoresearch 的有限上下文/反馈，但不把并行当默认。

## 5. 候选工作流不是必须执行的线性流水线

| 真实工作 | 最小合理路径 |
| --- | --- |
| 解释/小问题/小修复 | 当前 Agent 直接完成 → 必要验证 → 按仓库约定提交/反馈；通常无需额外 Skill |
| 有明确需求的中等功能 | 读取项目真实状态 → 必要时短执行合同 → 本地 Agent 实现 → 核对 diff/用户路径 → 完成 |
| 产品/UX/视觉仍未定 | 网页端使用现有 Product & UX / Visual System 讨论并明确关键决定 → 再交给执行；不让实现 Agent 代替用户选产品形态 |
| 跨模块、高风险、新架构 | 先解决不可逆决定 → 有界 Plan / 关键接口或不变量 → 按依赖拆成可验证执行单元 → 分段实现 → 独立依据规格/证据复审 |
| 复杂回归/长尾故障 | 先构建能捕获**真实症状**的快速反馈/证据 → 定位 → 有界修复 → 回归 → 只沉淀真正会反复遗忘的经验 |
| 长期无人值守/多 Agent | 明确起始基线、权限、可改文件/工作区、任务界线、验证及停止点；不可逆/产品重大取舍标阻塞，其余安全工作继续；真实结果由 Git+记录恢复 |

### 不宜引入的全局惯例

- 在 `AGENTS.md` 放全部进度、所有长期计划或每个 Skill 内容；
- 规定一律先 /grill、/spec、/tickets、/review、/retro，或者任何任务都要多个审查 Agent；
- 无必要的每轮文档膨胀、自动生成 PRD/ADR/GLOSSARY/方案图；领域词汇真的产生歧义时再建 glossary，难以反转的选择才用 ADR；
- 为普通串行任务机械新建 worktree 或让所有任务自动并行；
- 不用当前代码与可重复证据验证就下结论；也不反复找新问题导致永不收口；
- 自动安装一整套第三方框架并把其全局指令覆盖 AgentKit 的已知协作约束。

## 6. 下一步：先定**架构边界**，而不是抢着写 6 个 Skill

建议先用现有 AgentKit 和这些外部资料，确定一份很短的**任务路由 + 文档权威 + 对应执行交接**规则，并对已有三个产品开发仓库的真实协作方式做“路径对照”检查。

首个最有价值的可制作候选是 **`decision-to-execution`**（用户当前最频繁手工打长 Prompt 的环节），其次才是针对复杂问题的 `repro-first-debug` 和跨模型复审的 `spec-and-diff-review`。`workflow-router` 也许一页说明就够，不一定是独立 Plugin。现有 `personal-ui-delivery` 不应重复造一个“UI 交付” Skill。

**当前状态：仅研究完成，尚未授权/创建新的工作流 Skills 或全局 Agent 指令。** 用户可继续提出其他开发者案例，再结合使用频率、维护成本和重合度确定第一批实现。
