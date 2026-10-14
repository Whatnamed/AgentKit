# 从源系统复用视觉：完整度与目标可实施规范

仅在“完整视觉迁移、担心细节漏失、源系统与目标技术栈有差异”时使用。此处强调 **Design language parity（视觉角色的等效）**，不是 Pixel identity（像素逐点相同）。

## 四层迁移

1. **原始基础**：颜色/字体/字阶/行高、间距尺、形状、表面、图标、动效、主题、资产与版权。从源系统的指定版本取真实值，不能凭截图发明精确 Token。
2. **语义角色**：Page/Section/Group/Item/Metadata、主次动作、Canvas/Sidebar/Workspace/Overlay、Navigation/Inspector 等，在目标产品对应什么**用户职责**。没有对应角色时不强行映射。
3. **组件与状态**：容器内部 padding、标题/标签/图标之间距离、控件大小、row 高、各种状态、键盘焦点、loading/error/disabled、长内容，源组件未覆盖时按源原则扩展目标组件。
4. **模式与页面节奏**：源系统中“不同级别关系如何通过距离、背景、边界表达”的可移植做法；结合目标 IA 确定筛选条、列表、侧栏、详情、表单、数据视图的密度。若源产品没有该页面类型，不能凭风格名假装它已定义过。

对每个重要目标页面记录：源版本和来源组件 → 对应语义角色 → 继承/调整/新增/不继承 → 目标规范（类型+状态+关键尺寸/间距关系）→ 例外理由 → 验证等级。

## 怎么识别“只是皮肤像了”还是“真的继承完整了”

- **只继承品牌色/字体名称**：不能称完整迁移。
- **组件看似一致但组距/行距/面板层级不同**：仍缺 Visual rhythm 与 Surface parity，优先校准这些系统关系。
- **静态图好看但真实字体/长文本/深色/焦点错位**：缺运行验证，不能称“目标系统已验收”。
- **所有原页面被照搬导致目标任务很别扭**：产品 IA 错配，不能为了视觉保真牺牲使用。
- **目标需要新领域组件或新平台**：不可能逐组件 1:1 复用，保留设计语言并生成目标自己的组件规则与例外。
- **源系统与目标系统有矛盾**：记录权衡（用户任务、平台差异、无障碍、品牌例外），不能把差异偷偷抹掉或无限调参。

## 有缺口怎么办

可见的源码与截图不足以证明所有 Token、字重、控件状态存在。目标文档应把证据分成：

- `source-documented`：源规范如此定义；
- `source-runtime`：在指定源宿主和状态中确实观察到；
- `target-specified`：目标已决定要这样用；
- `target-implemented`：目标代码已实现；
- `target-validated`：目标真实应用中的代表性体验已验证。

每层互相不能代替。缺任何一层只需记明什么还无法判断，**不是要求无休止地跑大型视觉测试**。

## 可借鉴的专业系统

- [Microsoft VS Code Design Philosophy](https://github.com/microsoft/vscode/blob/main/.github/skills/design-philosophy/SKILL.md)：同一个风格应以共享目标、原则和视觉规则维护，而不是凭像素猜。
- [IBM Carbon Spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview)：空间 Token 在组件内、组件间承担不同层次的职责。
- [Anthropic Knowledge Work Plugin — Design System](https://github.com/anthropics/knowledge-work-plugins/blob/main/design/skills/design-system/SKILL.md)：Token、组件变体、状态、可访问性与来源检查，而不只是色表。
