# AgentKit Visual System — Plugin package source

使用四个独立 Skills 完成新产品的视觉设计与继承。Plugin 只是组装与分发，不重复维护 Skill 正文，也不包含字体和私人原始截图。

- `visual-system-extract`：从现有项目提取完整、版本化视觉参考系统（Typography、空间节奏、组件 API/状态、Source Map、证据）。
- `visual-system-create`：根据**已确定的产品布局**从零建立视觉方向和设计系统，支持多轮探索、选择、局部调整与定稿。
- `visual-system-adopt`：把指定源系统的视觉语言完整映射到新产品 IA，包括字体、间距/行高/信息密度、区域层级、状态等，**不复制源产品业务导航**。
- `visual-qa`：基于真实渲染和规范找差异、最小修复和收口。

**打包**：在仓库根目录执行 `python scripts/build-plugins.py visual-system`，得到 `dist/plugins/agentkit-visual-system.zip`；由宿主支持的 ZIP 导入流程安装。不是已发布的账号 Plugin。

`personal-ui-delivery` 故意独立作为可复制 Skill，负责后续 Coding Agent 的实现与文档同步，不因安装视觉 Plugin 就自动获得。
