---
name: acheng-performance-action
description: 文戏表演因果、武戏/打戏攻防编排、动作受力因果，以及从上游表演交接到镜头的适配。用户要求设计或修复攻防、格挡、闪避、缠绕、挣脱、受击反制时使用。
metadata:
  version: "3.2.0"
---

# acheng-performance-action

在 Infinite Canvas 制作稿中，`performance`、`acting_design` 及其子字段内供人阅读的描述、动作线索和排除项一律使用简体中文；只保留结构键、稳定 ID、数值和合同要求的枚举值。不要因字段名或示例使用英文而输出英文表演正文。H3 的英文译文由正式编译后的翻译流程生成，不要求源稿维护英文副本。

情绪尚未外化、动作因果缺失或对白与动作抢节拍时，按[局部决策指南](../../references/decisions/performance.md)对应节执行，先筛可见部位和身体条件，再选适用配方。

本文件是acheng-director随包专业子入口，按路径加载；主导演负责真值、版本、对象创建和最终合并。它不自动启动代理或调用模型。

写入前先读取本文件和 `data/module-registry.json` 中 performance 登记的全部 `reads`；该登记是依赖清单，不以父入口提到“performance 模块”代替实际加载。动作任务至少核对[表演适配](../../references/30-performance-adapter.md)、[本分支核心合同](../../references/31-performance-handoff.md)、[灵动表演合同](../../references/32-liveliness-performance-framework.md)、[专门规则](../../references/40-action-choreography.md)与[模块回包合同](../../references/91-module-orchestration.md)，并按当前命中的局部决策指南执行。只读取本任务依赖，保留上游来源与冻结项。

武打/攻防写入前检查：每个动作 Shot 都有结构化 `combat`，含七层受力、`chain` 攻应果续和 `timing` 的五阶段、`direction_facts`、`speed_profile`；`phases` 使用本镜局部整数帧并闭合到 Shot 时长。`characters` 只列画内角色并标明位置、朝向、视线、持械手和武器方向。若镜头是明确落空，写最近距离、制动支点、惯性结果和尾态，不虚构接触。H3 的 `visual` 要落实同一攻防事实，不能用自由文本替代这些结构化字段。

有锁定expression_handoff时消费来源、十二项表演信息与排除项；镜头只接收可见的相位。无交接时依据已确认剧本设计，不声称外部专家已处理。动作采用攻应果续与适用的受力链，保留受击和尾态。

内心信息需要由演员承载时，只写剧本已支持且镜头可见的眼神、呼吸、姿态或动作变化；超自然感知中的抽象对象由视效规则转成画面征象，不用演员反应替代征象，也不为解释内在状态擅加动作。

返回符合白名单的 `patch`、依据明确的 `evidence` 和未决项 `unresolved`；涉及表演/动作时写入 `performance`/`combat` 及可追溯来源。需要灵动、夸张或动作化表演时，额外返回 `acting_design` 和可供模型编译的运动逻辑。没有锁定 `expression_handoff` 时不得捏造来源 beat ID；依据已确认剧本设计可见动作，并将缺失来源事实列入 `unresolved`。expression_handoff由主导演接收和锁定，本模块不修改它。不修改镜头景别、故事结果或伤势事实。不可见或超容量的节拍明确返回主导演，不静默删去。

字段写入白名单取[模块登记](../../data/module-registry.json)。回包包含request_id/input_revision/module/status/attempt/patch/evidence/unresolved；最多初次加一次有证据的修正。只改允许路径，不能把其他模块的建议直接写成已确认事实。
