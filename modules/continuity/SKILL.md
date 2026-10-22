---
name: acheng-continuity
description: 跨镜跨集事实重放、冷档恢复与分层交付验收。
metadata:
  version: "3.2.0"
---

# acheng-continuity

无限画布运行包提供 ledger contract v2 时，视频制作必须读取并遵守 `getProductionContract(runtimeId, "set_director_production").continuityLedger` 及本运行包的 `scripts/continuity_v2.py`。先按已登记的角色、场景、资产、剧本块和 Shot 构造 timeline、facts、initial、events、requirements 与逐块 coverage。timelineId/storyOrder 显式声明叙事次序；倒叙使用新 timeline 和明确初态，不沿用播放顺序推断。knowledge/relationship 仍引用 story owner 字段；资产版本引用 assets owner 字段。

coverage 是人工专业复核证据，不是机器语义发现：每个剧本 block 都有源摘要和 evidence_kind；变化必须链接事实、requirement、event 与来源；保持须链接对应事实的已知初态；not_applicable 仅使用合同允许的窄规则并附理由与复核引用；未知标 unresolved_review。不能为通过批量填写“不变”或伪造事件。普通编辑可以保存 blocked/partial，不能将它标记为完整。

当场景地图、Blocking 或相邻 Shot 显示人物跨镜改变相对位置/姿态，且会影响下一镜的左右关系、遮挡、视线、攻击路径、接触或剪辑匹配时，必须按[连续性决策 K6](../../references/decisions/continuity.md#k6跨镜位置姿态与场景锚点)判断是否登记空间状态 fact、初态、转场 event 与逐镜 hold/change requirement。单镜构图仍写入 Shot visual/camera；`subject_usages` 只说明可见性。没有证据时不得把场景侧向简化成全段不变位置，也不得猜转场帧。

程序派生的 Shot 起止状态、outcome events 与报告严禁写入 ledger/source。覆盖回执、技能读取、程序重放和媒体观察分别报告；机器结构通过不声称自然语言已完整识别，也不声称实际画面通过。

跨镜状态、参考版本或恢复游标有冲突时，按[局部决策指南](../../references/decisions/continuity.md)对应节定位来源；只返回具体缺口，不新增事件来强行对齐。

读[114 绑定合同](../../references/114-reference-binding-delivery.md)。相邻复核 model 的稳定对象身份、素材状态版本、Shot/帧窗和尾态；发现错误退给字段 owner，不自行改 H3 或素材。联合回执必须与当前 revision 一致，机器 PASS 不等于语义识图、平台上传或实际成片验收。

本文件是acheng-director随包专业子入口，按路径加载；主导演负责真值、版本、对象创建和最终合并。它不自动启动代理或调用模型。

先读[本分支核心合同](../../references/80-continuity-ledger.md)与[专门规则](../../references/95-quality-gates.md)；同时遵守[模块回包合同](../../references/91-module-orchestration.md)。只读取本任务依赖，保留上游来源与冻结项。

从真实初态重放伤势、弹药、道具与场景变化；并保存叙事知识、伏笔、表演来源和资产版本。索引指向完整原文，不能删除原文仅留摘要。归档和恢复核验哈希与素材，失败保持原件。

返回账本差量、未决项目与分层报告。结构通过、提示词就绪、实际影像通过分别记录；不得把未生成片段写为视觉通过。

字段写入白名单取[模块登记](../../data/module-registry.json)。回包包含request_id/input_revision/module/status/attempt/patch/evidence/unresolved；最多初次加一次有证据的修正。只改允许路径，不能把其他模块的建议直接写成已确认事实。
