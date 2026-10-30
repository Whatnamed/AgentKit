# AgentKit

跨项目、跨 Agent 的个人方法、Skill、Plugin 与开发规范库。当前第一批是**完整产品前端设计 → 视觉体系 → 实现交付**的工作方法，不是某一产品的 UI Kit，也不限制将来添加其他领域。

## 从一句话开始

“我有一个新产品想法和大概功能，用 AgentKit Product & UX 把产品定义、信息架构和每页布局、操作细节、异常状态都做完整，先不碰视觉；关键决策由我确认。”

产品部分定好以后：

- **复用视觉**：“用 AgentKit Visual System 从指定旧项目提取视觉语言，再完整适配到新产品的页面，连同字体、空间节奏、行高、表面、组件状态一起做。”
- **新做视觉**：“用 AgentKit Visual System 帮我从零选方向，在真实代表页面上反复调整，再整理成可开发、可维护的设计系统。”
- **进入开发**：“使用 `personal-ui-delivery` 按产品/UX 与视觉规范实现 UI，先核对文档与真实代码，不把未定产品设计交给实现 Agent，修改后维护正确的文档。”

详见 [从想法到完整前端的使用路线](docs/design-workflow.md)。

两个 Plugin 的跨行业方法和公开 Skill 对照已收录于 [2026-10-15 外部复审](research/product-ui-external-practice-review-2026-10-15.md)；只补真正需要的按需知识，不新增强制检查流程。

**跨项目工作流探索**：另见 [个人 Coding Agent 工作流与知名开发者 Skills 比较（2026-10-15）](research/cross-domain-agent-workflow-landscape-2026-10-15.md)，覆盖 Matt Pocock、Every、Superpowers、gstack、OpenSpec、Spec Kit、BMad、GSD 和 Peter Steinberger；此文件是研究提案，不表示已安装或启用新的开发框架。

**工程任务的最新取舍**：参见 [2026-10-23 有界审查、Bug 调试与反过度工程化复核](research/engineering-skills-proportionality-review-2026-10-23.md)。现已新增两个独立工程 Skills；`decision-to-execution` 与 `context-continuity` 因和既有习惯重合暂不创建。

## Skills（10 个，单一源码）

| 分组 | Skill | 做什么 |
| --- | --- | --- |
| Product & UX | [product-discovery](skills/product-discovery/SKILL.md) | 需求与任务补全、对象、范围、可行性 |
| Product & UX | [product-ia-interaction](skills/product-ia-interaction/SKILL.md) | **完整 IA、逐页空间布局、组件/控件和微交互、状态与恢复** |
| Product & UX | [product-ux-review](skills/product-ux-review/SKILL.md) | 审查缺漏和不合理交互，按影响决定是否修复和收口 |
| Visual System | [visual-system-extract](skills/visual-system-extract/SKILL.md) | 从真实来源提取完整设计系统、组件与证据 |
| Visual System | [visual-system-create](skills/visual-system-create/SKILL.md) | 从零创建视觉语言，支持持续比较和调整 |
| Visual System | [visual-system-adopt](skills/visual-system-adopt/SKILL.md) | 将指定视觉体系按**角色和细节**迁移到新的产品 IA |
| Visual System | [visual-qa](skills/visual-qa/SKILL.md) | 真实页面视觉对照、根因、最小修复与停点 |
| Standalone | [personal-ui-delivery](skills/personal-ui-delivery/SKILL.md) | Coding Agent 按产品/设计文档实现、核对与同步 |
| Engineering | [spec-and-diff-review](skills/spec-and-diff-review/SKILL.md) | 根据需求与 Git diff 做双轴审查，控制范围与多余验证 |
| Engineering | [repro-first-debug](skills/repro-first-debug/SKILL.md) | 针对真实 Bug 建立有效证据、调查根因并有界修复 |

Skills 可以单独触发，不必每个新问题重复走全流程。完整新产品可以分阶段按用户实际反馈推进，但不以只完成高层框架或 UI Demo 为终点。

## 两个可构建 Plugin

- [Product & UX Plugin](plugins/product-ux/README.md) — 3 个 Skills。
- [Visual System Plugin](plugins/visual-system/README.md) — 4 个 Skills。
- 独立 `personal-ui-delivery` 是通用 Agent Skill，不捆绑到两个插件。

插件使用 [portable Agent Plugins](https://developers.openai.com/plugins/build/plugins) 的根 `plugin.json`；单一源码在 `skills/`，不手工复制第二份。需要 ZIP 时运行（Python 3.10+，无额外依赖）：

```powershell
python .\scripts\build-plugins.py
```

产物：`dist/plugins/agentkit-product-ux.zip`、`dist/plugins/agentkit-visual-system.zip`。导入安装要在支持的平台操作，**本仓库代码存在不意味着账号中已安装 Plugin**。具体见 [打包说明](plugins/README.md)。

**ChatGPT Project 完整项目指令**：见 [《开发项目协作规则》完整整合版](docs/chatgpt-project-instructions.md)，已按既有八章节将反无效防御、适度验证及写作要求融入正文，可整份复制到 ChatGPT Project 设置。仓库根目录 [AGENTS.md](AGENTS.md) 是本仓库完整、独立的协作规则，不等于本机用户全局 AGENTS.md；后者的最新私有原文没有存放于此公开仓库。

## 源码与长期结构

- `AGENTS.md`：仅维护本仓库的稳定协作规则。
- `skills/`：Agent Skills 的唯一可编辑源；每项自带按需阅读的 `references/` 与 `assets/`。
- `plugins/`：插件清单与分组；`scripts/`：轻量打包工具。
- `docs/`：实际使用路线；`research/`：历史草案与来源核验；`references/`：脱敏案例和来源索引。
- `tests/`：先前拟定的可选 smoke 场景，个人使用**不以跑大量测试为前置**。
- `private/`：本地原始对话、ZIP、图片和私有笔记，Git 忽略；绝不上传公共仓库。

## 证据与隐私

本仓库是 **Public**。原始 ChatGPT 聊天、未脱敏截图、账号信息、凭据、无法授权的第三方素材和字体文件不进入 Git。项目源码证据应有可核实的版本/路径；用户确认、Agent 建议、设计标准、真实实现和运行验收不是同一种证据。

这套 Skills 旨在**减少重复解释与重复踩坑**。格式及路径已可静态检查，但尚不宣称跨所有模型或不同新项目均经过独立实测；后续只针对实际使用发现的问题进行必要修正，不设无限优化计划。
