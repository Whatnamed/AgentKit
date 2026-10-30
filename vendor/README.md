# 第三方 Skills 原文快照（不是 AgentKit 自创技能）

本目录固定保存下面三个上游仓库的 Skill 原文件，不修改正文、名称或前置描述；LICENSE 均随快照保留。固定源码版本用于避免上游更新悄悄改变行为。这里只镜像 **Skills 和许可**，没有把整个上游项目的 Hook/本地运行时代码复制进 AgentKit。若想使用原版 Hook，请从对应项目官方发布渠道安装并按宿主许可审查。

| 快照 | 上游 | commit | 原文 Skill | 用途 |
| --- | --- | --- | --- | --- |
| Stop That Shit | https://github.com/lennney/stop-that-shit | `17ffc9f5108381916f4f9b019d61b759626c4a71` | `skills/stop-that-shit` + `skills/stss` | 任务边界/无用防御；附带一般写作防御性措辞 |
| Anti-Defensive Writing | https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill | `82d31402caa0db1790026824399044538483171b` | 中英两个版本 | **专用于学术论文写作**，不是通用任务管理技能 |
| Ponytail | https://github.com/DietrichGebert/ponytail | `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` | 6 个原始 Skills | 日常编码简洁、复用、Review/Audit、成本分析；尽量使用上游 Plugin 安装以获得宿主集成 |

说明：
- ChatGPT 若使用从这些文件组装的**纯 Skills Plugin**，不会具备上游原项目的本地 Guard/Hook 强制拦截，不能声称拦截了本地操作。
- 原始第三方 Skill 没有被 AgentKit 编辑。适用条件、优先级、冲突处理、ChatGPT 项目指令等由 AgentKit 外层文档描述。
- Ponytail 与 STS 对编码有重合：一般不要两套全局 always-on 同时启用。Ponytail 适合编码时选择实现方式，STS 更重任务边界、重复流程、未经授权的防御。按任务决定哪个为主。
- 学术原版的说服性修辞不能覆盖真实性：研究结果、局限和引用事实必须完整、准确，不能为了突出优势省略影响结论的反证。
- 本目录为**冻结快照**，不是上游自动更新机制；后续若更新，重新核对 commit、原文变更、许可，并明确记录版本。不要把文件内容悄悄编辑成 AgentKit 自己的 Skill。
