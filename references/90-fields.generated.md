# 生成字段表（勿手改）

来源：`schema/production.schema.json` v3
单文本项上限：**7000** 字符

## 镜级事实（写一次，可从上镜继承）

| 字段 | 中文 | 建议上限 |
|---|---|---|
| `orientation` | 人物朝向 | 90 |
| `ground` | 地面与道具状态 | 90 |
| `axis` | 轴线与机位关系 | 120 |
| `framing` | 景别与焦段 | 80 |
| `movement` | 运镜 | 80 |
| `dof` | 景深 | 70 |

## 武戏连续性契约（只有跨镜必须校验的事实）

| 字段 | 中文 | 建议上限 |
|---|---|---|
| `axis` | 轴线保持 | 80 |
| `distance` | 起止间距（米） | 40 |
| `contact` | 接触点 | 60 |
| `damage` | 伤害与损耗 | 60 |
| `tail` | 尾帧状态 | 60 |

## 文戏连续性契约

| 字段 | 中文 | 建议上限 |
|---|---|---|
| `axis` | 轴线保持 | 80 |
| `eyeline` | 视线关系 | 60 |
| `distance` | 人物间距 | 40 |
| `state_change` | 状态变化 | 80 |

## 写作方法（不进 schema、不进校验、不进编译）

- 武戏五拍：approach → commit → contact → recovery → reset
- 武戏七层：force_source · trajectory · contact · resistance · impact_hold · transfer · recoil
- 文戏五拍：open → press → turn → land → after
- 详见：references/40-action-choreography.md、references/31-performance-handoff.md
