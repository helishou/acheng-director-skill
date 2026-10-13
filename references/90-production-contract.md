# 90｜统一生产数据与 A/B/C 总线

## 版本与基本类型

当前唯一画布生产格式使用 UTF-8 JSON 或 YAML，必须同时声明根 `version: 2`、`prompt_assembly.version: 2` 与 `ledger.contract_version: 2`。Shot 使用整数 `duration_frames`、`timeline_id`、`story_order` 和局部帧，不保存全局 `start_frame/end_frame`。角色、场景、道具引用走 `subject_registry`、`subject_usages`；关键帧走 `shots[].keyframes`；对白通过 `utterances` 与 `utterance_refs` 绑定；Clip 图片由 Subject/关键帧编译派生，归档声音由 `audio_bindings` 显式绑定。旧格式、未知标记、全局帧 Shot 与 `segments[].references` 均不再解析或回写，需由当前 Acheng Director 显式升级。秒数可用整数、十进制或有理数字符串，所有时间运算由 Fraction 完成；帧号为整数，不接受 bool、NaN 或重复 JSON/YAML key。区间左闭右开。路径相对 production 文件目录，不相对当前 shell 工作目录。

必需字段：version、prompt_assembly、ledger、project_id、fps_num/fps_den、production_total_duration、generation_clip_limit、scene_registry、character_registry、subject_registry、shots、utterances、segments。可选 brief、story、asset_cards、unresolved_threads、dispatch_log 保存叙事和溯源，不能替代必需字段。`audio_bindings` 每项保存 label、来源音频节点、storageKey、SHA-256、角色和局部 Shot 范围；不复用旧 `Segment.references`。

新合同分别见[11叙事](11-story-architecture.md)、[31表演](31-performance-handoff.md)、[32灵动表演](32-liveliness-performance-framework.md)、[46条件特效](46-effect-families.md)、[61资产依赖](61-asset-dependency-production.md)、[91专业模块](91-module-orchestration.md)。旧A/B/C支路契约继续解释已有资产来源与窄操作，七模块登记负责新的阶段分工；两者不重复赋予同一字段多个最终写入者。

## 场景与角色登记

scene_registry 每项至少 id/name，生产使用时同时写 space、entrances、exits、landmarks、key_light、version。character_registry 每项 id/name/height_m/identity；height_m 是设计值或测量值须在旁注区分，百米以上自动触发尺度审查。角色 ID 和场景 ID 互不复用；道具 ownership 只指向登记对象。

## Shot：Subject Prompt Assembly v2

| 字段 | 合同 |
|---|---|
| id / scene_id | 稳定且已登记的身份 |
| duration_frames / timeline_id / story_order | 正整数 Shot 时长及所属时间线顺序；绝对窗口由编译器派生 |
| visual | 英文可见画面、当前场所、身份和动作初态 |
| features | core_emotion/combat/supernatural_vfx/colossal 四个显式布尔值；不能通过关 flag 躲审查 |
| subject_usages | Subject ID、可见/画外音/状态上下文、显式图片绑定、局部用途与状态条件 |
| camera | previs_id 三位字符串，description、movement、path、target、adaptation、sensor_basis、lens_mm、shutter_angle |
| performance | 旧完整五轨或strategy:selective轨道；也可用source_beat_id/source_anchor/events消费完整表演交接；需要灵动/夸张/动作化表演时增加acting_design与段级motion_profile；详见31/32 |
| combat | 战斗时七层 force_source/trajectory/contact/resistance/impact_hold/transfer/recoil，加 chain.attack/response/result/continuation |
| vfx | energy_fluid使用主干/三通道/四相位；其他family使用origin/scope/process/end_state/lighting/continuity/events |
| scale_proofs | 巨构时至少两类证据，每项 type/detail/frame_location/depth_relation |
| keyframes / utterance_refs | 关键帧局部锚点及对白原文片段的局部帧窗口 |
| audio | foley 数组、low_frequency_hz；有低频写 source/classification，无则 no_low_frequency_reason |
| outcome_events | 本镜造成的账本事件 ID，未变化为空数组 |
| state_in/state_out | 对应初始／事件重放的完整状态快照 |

表演、声音、VFX、关键帧与连续性事件时间都使用 Shot 局部帧。相机路径与人物位置是计划目标，不声称来自源片精确测量。提示词 visual 和 cues 用英语，台词保留用户原文；内部中文分析不得混入最终 H3 正文。

## Segment

Segment 的 `shot_ids` 按源稿顺序连续覆盖，`mode`、`mode_lock`、`mode_selection_reason`、`styleTemplateId`、`style`、`motion_profile`、`overall_soundscape`、`non_diegetic_music` 和 `summary` 保存执行配置与描述。时长与 Shot 窗口派生；禁止在源稿写入 references、subjects、Prompt 或绝对帧。`audio_bindings` 是唯一外部音频输入字段，图像输入使用 `pictureBindings` 与 Shot keyframes。Ref2VA 正文由当前 Subject Prompt 编译器生成；编译产物的 Picture/Audio 清单是派生回执，不是第二生产真值。

实际关键帧应在 `shots[].keyframes` 写主体、锚点与局部帧；工具负责语法和结构检查，人负责看图核对角色与路径。

## 账本事件

账本使用 `facts`、`timelines`、`initial`、`events`、`requirements` 与 `coverage`。事实通过 object_kind/object_id 关联已登记 Subject；事件通过 fact_id、shot_id 与 `local_frame` 锚定，保持 before/after/reason；要求和覆盖保留稳定 ID 与来源锚点。检查重放只写入报告，不回填到源稿；无法映射局部 Shot 的事件拒绝迁移。

## A/B/C 标准消息外壳

所有支路请求都用以下字段：contract、version、request_id、caller、target、input_revision、scope、allowed_write_paths、payload。回包用同 request_id、input_revision、status、patch、evidence、unresolved。总导演拒绝版本不符、作用域之外字段、未知 shot_id 或无法复核的“已验证”。每个请求最多一次生成及一次有明确失败原因的修正；还有冲突时交回主导演，不让两个支路互相调用形成循环。

契约 A target=cinematic-vfx-prompt-engine，只返回 vfx 表现槽。OPTIMIZE 冻结 origin、collision_type、collision 和 phases，防止在槽内偷改接触结果或时间。

契约 B target=h3-prompt-writing，只返回 selected_mode、alignment_line、ordered_sections、reference_map、execution_gate；不改剧情和总时长。当前脚本是该已读指南的确定性文本编译实现，不是远程 Skill RPC。

契约 C target=im2-clean-image，仓库别名 im2-image-skills。返回 image_transaction、seven_steps、recipe、structure_lock、prompt、avoid、actual_generation_settings、acceptance。未生成时 actual_generation_settings 为计划或 null，acceptance.visual=unverified。

可运行资产卡使用`asset_cards`数组：id、target_skill、source_repository、recipe、mode、transaction、seven_steps、prompt、reference_policy、references、generation_status、actual_settings；重场景另有structure_lock。reference_policy为none/required，references每项为image/file/role/subject/preserve/exclude。`prompt`是完整可提交正文，不能省略；可选prompt_bindings只用于导出前显式展开。compile_assets与post_hooks共用相同规则。早期资产模板是[asset-stage.json](../templates/asset-stage.json)，含完整实例。

## 确定性钩子与失效传播

script 后运行 `post_hooks.py script` 检查 scene_id 与正文表头；assets 后运行 `post_hooks.py assets` 检查七步、事务、参考和结构锁。这两个钩子不要求虚构下游镜头。其他模块在完整工作生产包上运行 audit：storyboard 对应G1/G2；performance 对应G4；action 对应G5；vfx 对应G6与冻结差异；compiler 对应G8/G9；continuity 对应G10。尚未产出的下游字段会报告未就绪，不能称整个包通过。最终统一跑十项。场景地图改动使该场相机、资产和关键帧失效；台词改变只使相关表演、声音和编译失效；vfx材质改变不触发剧本重写。

核验报告应区分描述存在与生成画面实测。禁止把上游文件里“通过”字符串当验收证据。机器分数必须来自当前 production 内容 SHA，与实际交付版本一致。
