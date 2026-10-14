# 视觉继承：避免只复制皮肤的检查参考

**先有目标产品 IA。** 这个文件是设计角色迁移的检查项，不是让所有产品继承同一个宏观页面形态。

## 源与目标逐层映射

| 层 | 源系统需要调查的细节 | 目标必须确定 |
| --- | --- | --- |
| 设计意图 | 气质、密度、内容优先于 chrome 还是展示优先 | 是否适配目标用户任务，有意例外 |
| 字体 | face/文件、真实字重、Unicode/script fallback、mono、数字 | 与目标宿主兼容的资源、行高/基线、长中英混排 |
| 文字层级 | Page/Section/Item/Metadata、字阶、字距、字重、caption | 每个目标区域应用哪个 role，别机械加副标题 |
| 空间节奏 | Page padding、Section gap、Group gap、list row、control gap、title/caption | 目标页面真实信息密度、滚动/折叠、组合关系 |
| Surface | canvas/sidebar/workspace/raised/inset、border、shadow、inspector | 持续区域/临时弹层的不同表面层次 |
| 颜色状态 | semantic、hover、selected、focus、disabled、loading | 能区分来源状态与选择状态，Dark 自洽 |
| 控件 | Button/Input/Select/Table/Row/Badge/Dialog/Popover 等全部适用变体 | 目标行为不失真，键盘焦点与点击区域合理 |
| 图标、动效 | 线性风格/光学中心/stroke/速度/easing | 按目标含义选图标，不用动效遮盖状态错误 |
| 宿主与适配 | 字体安装、DPI、视窗宽度、浏览器/WPF/Tauri 差异 | 真实多视窗/主题/数据状态观察 |

## 密度的可观察判断

- Page 到 Section 的呼吸感是否和源系统等价？只给主区多留白，辅区维持密度有无破坏节奏？
- 标题、操作工具栏、内容列表是否属于同一个视觉组？区分区间靠边框还是靠空间，位置有没有理由？
- 一个列表项里标题/参数/元信息的比例与相互距离是否相符？是否把全部元素都加大了间距？
- Inspector/side pane 在默认态、选中态、错误态是否拥有独立 Surface？语义 Badge 与选中高亮是否冲突？
- 改一套字体后按钮高、行高、图标光学对齐是否真的仍一致？
- Light/Dark 是否只是翻转颜色，还是保有同样的层级和焦点强度？

## 借鉴记录的真实性

- 只有在源系统有相应组件或模式时才可标 `inherit`。
- 源系统没有目标领域组件时标 `new` 并沿已有 Token 构建，不假装已有同名组件。
- “不能照搬”应解释是业务 IA、交互职责、主题差异、平台或证据不足的哪一种。
- 源 UI 已验收但目标未运行时，最多说明“目标映射计划已确认”，不能说“视觉迁移 PASS”。
