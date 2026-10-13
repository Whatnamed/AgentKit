# AgentKit

跨项目、跨 Agent 使用的个人方法与能力资源库。可长期维护 Agent Skills、ChatGPT 私人 Plugins 的源文件、`AGENTS.md` 模板、工作流、参考案例与必要的辅助工具。

**当前阶段：** 先做资料核验、设计方法提炼和 Skill 方案审定；尚未制作或发布正式 Skills / Plugins。产品设计与 UI/UX 是第一批主题，不限定仓库未来只能存设计内容。

## 目录约定

- `agents/`：可复用的 Agent 指令模板（不是本仓库的 `AGENTS.md`）。
- `skills/`：审定后制作的标准 Agent Skills。
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
