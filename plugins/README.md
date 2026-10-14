# AgentKit Plugin 组装

当前两个 **skills-only portable Agent Plugin** 源包：
- [Product & UX](product-ux/README.md)
- [Visual System](visual-system/README.md)

上游唯一的 Skill 源码：`/skills/<skill>/SKILL.md`，各自 `references/` 和 `assets/`。本目录仅保存 `plugin.json`、分组说明；不维护第二份 Skill。

在仓库根目录运行：

```powershell
python .\scripts\build-plugins.py
```

输出（已忽略 Git）：

```text
dist/plugins/agentkit-product-ux.zip
dist/plugins/agentkit-visual-system.zip
```

每个 ZIP 为**独立插件根目录**，根下包含 `plugin.json` 与完整 `skills/`；不要在归档外额外包一层文件夹。可以单独构建 `python scripts/build-plugins.py product-ux` 或 `visual-system`。

格式以 [OpenAI Plugin packaging](https://developers.openai.com/plugins/build/plugins) 和 [Agent Skills specification](https://agentskills.io/specification) 为准。这里不配置无必要的 MCP、hooks、凭据或空 app 映射，也不在源码仓库里保存个人账号 Plugin ID。构建得到可导入包 **不等于已安装/发布**；真正使用之前按宿主产品的 Plugins 入口导入或通过 Plugin Creator 创建私人版本。

若只需要本地 Coding Agent，按其真实加载约定使用根 `skills/` 中的独立技能即可；**ChatGPT Plugin 的安装不会自动把技能安装到每个本地 Agent**。

如暂时不想使用本地 Python，也可在 GitHub 仓库 Actions 页手动运行 **Build AgentKit Plugins**，从该次运行的 `agentkit-plugin-bundles` artifact 下载两个已组装的插件 ZIP（外层 artifact 压缩包需要解压后再导入其中的单插件 ZIP）。这只是**按需打包**，不会安装到账号里。
