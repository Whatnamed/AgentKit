# AgentKit

跨项目、跨 Agent 使用的个人方法与能力资源库。可长期维护 Agent Skills、ChatGPT 私人 Plugins 的源文件、`AGENTS.md` 模板、工作流、参考案例与必要的辅助工具。

**当前阶段：** 设计方法来源研究已进入两个 Skill **原型试做**。这些目录尚未安装为私人 Plugin，也没有完成独立的多模型效果评估。产品设计与 UI/UX 是第一批主题，不限定仓库未来只能存设计内容。

## 第一批试做

- [product-ia-interaction](skills/product-ia-interaction/SKILL.md)：根据已确认产品目标建立或修正页面职责、关键任务路径、上下文与交互状态。
- [visual-system-extract](skills/visual-system-extract/SKILL.md)：从可追溯源码/设计规范提取设计系统快照，包括组件、Typography、Tokens、Source Map 和真实性边界。
- [Smoke cases](tests/design-skills-smoke-cases.md)：实际使用前的对照测试题、预期行为与人工评分标准；**目前只是测试设计，并非测试 PASS**。

两个目录各自包含可选的 `references/` 与 `assets/`，可独立复制、试用。仅当任务需要时才展开详细参考；不要把研究草案当正式规则。剩余五个候选 Skill 尚未制作，职责见 [v0 架构提案](research/design-skills-architecture-proposal-v0-2026-10-13.md)。

## 目录约定

- `agents/`：可复用的 Agent 指令模板（不是本仓库的 `AGENTS.md`）。
- `skills/`：试做及审定后的标准 Agent Skills。
- `plugins/`：Plugin 分发/打包材料，尽量引用同一份 Skill 源码。
- `templates/`：可复用产物模板。
- `references/`：经筛选、脱敏的案例和设计参考。
- `research/`：待审定研究、候选方法、证据与方案。
- `scripts/`、`tests/`：必要的辅助脚本和 Skill 评估。
- `private/`：本机原始对话、附件与未脱敏资料，**永远不上传仓库**。

目录按实际需要逐渐建立，不预建空壳。

## 资料与隐私

本仓库目前是 **Public**。原始 ChatGPT 导出、完整聊天、截图附件、身份/账号信息、密钥、本机私有文件路径，均不进入 Git。仅在明确筛选、脱敏和确认可公开后，才将可复用内容放入 `research/` 或 `references/`。

研究结论必须区分用户已确认决策、助手建议、执行报告、源码可验证事实和待验证推断。候选规范不得提前宣称已经跨项目验收。
