# AgentKit Product & UX — Plugin package source

本目录保存 **portable plugin.json** 与打包说明；Plugin ZIP 由仓库根目录下的单一 Skills 源码生成，不在此目录重复维护 `SKILL.md`。没有 MCP/外部账号依赖。

包含：
- `product-discovery`：功能想法 → 用户任务、核心对象、范围与真实限制。
- `product-ia-interaction`：已知产品能力 → 详细 IA、逐页布局和微观交互、状态合同。
- `product-ux-review`：检查产品细节遗漏、不合理决策和完整操作路径，并适时停止。

可单独启动其中一项，不强制每次从头开始。用户要求“从产品想法完整做到可开发 UI 规格”时，先补产品定义，再按页面深度展开，不要止于站点地图或静态 Demo。

**打包**：在仓库根目录执行 `python scripts/build-plugins.py product-ux`，生成 `dist/plugins/agentkit-product-ux.zip`。ZIP 内有根 `plugin.json` 和 `skills/<name>/SKILL.md` 及全部引用资源；可按宿主支持方式导入 ChatGPT/Codex 的 Plugins。

这是插件源码/可构建分发包，不代表已在用户账号里安装或发布。分发可用性由宿主平台和当前权限决定。
