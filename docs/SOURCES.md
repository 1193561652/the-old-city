# 资料索引

更新日期：2026-09-29

## 已有项目文档

| 资料 | 状态 | 用途 |
| --- | --- | --- |
| `ue5-single-player-roadmap.docx` | 已存在 | 10 周 MVP 路线、里程碑、风险、技术边界和两周行动。 |
| `README.md` | 当前项目 | 项目入口与文档导航。 |
| `PROJECT_OVERVIEW.md` | 当前项目 | 长期愿景和稳定设计原则。 |
| `MVP_SCOPE.md` | 当前项目 | 当前执行范围与验收标准。 |
| `DECISIONS.md` | 当前项目 | 已确认决策、待验证问题和停车场。 |
| `BALANCE_V0_1.md` | 当前项目 | 人口规模、历史依据、数值初值和验证计划。 |
| `../config/balance_v0_1.json` | 当前项目 | 可调整的 v0.1 配置数据。 |
| `balance/projection_v0_1.json` | 当前项目 | 经济与训练推演，不包含战斗验证。 |

## 资料收集分类

### 历史与空间

- 君士坦丁堡陆墙、城区、港口的空间关系。
- 晚期城市衰败、修复与围城时期的物质条件。
- 仅提炼可服务玩法和视觉叙事的内容，不追求一比一复原。

### 城市系统

- 前工业城市的食物、石材、木材、人口、运输和维护。
- 废墟清理、建筑施工、道路与防御工程。

### 战争系统

- Branko Milanovic, [An Estimate of Average Income and Inequality in Byzantium around Year 1000](https://stonecenter.gc.cuny.edu/files/2006/09/milanovic-an-estimate-of-average-income-and-inequality-in-byzantium-around-year-1000-2006.pdf), *Review of Income and Wealth* 52(3), 2006，pp. 449、461、464。研究论文，2026-09-29 查阅。用于军队与总人口量级参考；存在估计分歧，不能直接当作晚期君士坦丁堡或固定粮食供养定额。进入 MVP 数值基线，不作为历史复原宣称。
- John Haldon, [The Organisation and Support of an Expeditionary Force: Manpower and Logistics in the Middle Byzantine Period](https://deremilitari.org/2014/05/the-organisation-and-support-of-an-expeditionary-force-manpower-and-logistics-in-the-middle-byzantine-period/)，De Re Militari 于 2014 年转载的学者研究，2026-09-29 查阅。用于理解地区、家庭、税收和征发共同参与军队供给；据此将人口池表述为城市与供养腹地，未引入粮食运输或完整后勤系统。
- 围城中的城防、补给、士气、指挥和破口争夺。
- RTS 中少量但清楚可读的单位与阵线设计。

### UE5 实现

- [Top Down Template — Epic Games 官方文档](https://dev.epicgames.com/documentation/unreal-engine/top-down-template-in-unreal-engine)：2026-09-29 查阅。原始技术资料；Strategy 变体提供可移动、缩放的俯视相机、单位选择和移动示例及简单界面。已确定作为 MVP 工程起点，需改造交互并自行实现经营、建造与守城规则；实际可用性以选定引擎版本为准。
- RTS 相机与选择。
- 数据驱动建筑系统。
- 建筑预览、碰撞与放置验证。
- 小规模 AI 寻路与性能测试。

### 视觉与声音

- 衰败而仍有人生活的古城，而非纯粹废墟。
- 城墙、港口、宗教建筑与住宅肌理的视觉语言。
- MVP 阶段只保存参考，不投入正式资产生产。

## 收集条目模板

新增资料时记录：

- 标题 / 链接 / 作者或机构
- 资料类型与日期
- 可信度（原始资料、学术研究、通俗整理、艺术参考）
- 可支持的具体设计问题
- 提炼结论
- 是否改变已有决策
- 是否进入 MVP
