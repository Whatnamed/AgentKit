# Product UX 复审的独立视角

这里只是让复审能发现真正缺口，不是每次都打满的评分表。需要审查完整新产品时从这些角度有选择地走一遍：

- **任务适合性**：从用户为何来、到达成功所需步骤、完成后的确认与继续；是否被页面组织拖累？“存在这个功能”不代表可用。
- **信息架构**：内容在哪里归属；名称是否符合心智模型；一级导航、侧栏、详情是否以任务区分；搜索与浏览能否找到对象。
- **交互与状态**：触发、反馈、可撤销性、故障恢复、Loading/Empty/Error/Partial/Unknown；相关操作有没有不同的焦点和状态。
- **内容设计**：标题、标签、帮助文本、错误信息、用户真正需要知道的来源/限制；是否有为了填满界面而新增的无价值描述。
- **场景覆盖**：首次、日常、异常、数据多寡、不同角色与权限、不同输入设备/窗口、国际化与阅读障碍等**仅适用场景**。
- **实用性和商业规则**：是否能完成真实系统允许的动作；代价、风险和权限是否准确；业务真相不能被视觉 demo 粉饰。
- **交付一致性**：源规格、页面详设、当前运行代码相互矛盾吗？目标设计改动是否被记录，而不是让开发者猜？

用事实给出影响 → 证据 → 可执行的具体变更。少量高价值建议比几十项泛泛“注意事项”更好。

参考：[NN/g — 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)、[gstack Plan Design Review](https://github.com/garrytan/gstack/blob/main/plan-design-review/SKILL.md)、[GOV.UK User Tasks Patterns](https://design-system.service.gov.uk/patterns/)。不要将它们的组织体系无条件复制成我们的固定流程。
