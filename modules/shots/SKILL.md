---
name: acheng-shots
description: 根据叙事功能设计分镜、摄影、剪辑与4–15秒生成切片。
metadata:
  version: "3.2.0"
---

# acheng-shots

局部返修先把人物可见范围、空间隔离、道具归属和事件完成状态写成具体初态与尾态。每次观看对象或空间视角切换登记独立 Shot，再装入 Clip；画外角色不登记可见起始坐标。动作窗口必须容纳对白后的接触、释放和离场，不用模板表演说明代替具体对象。

新旧源稿的对白镜头由编译器根据每句台词的说话者与整数帧窗插入说话者脸肩近景、转轮反打和长句末尾的听者反应视角；旁白不触发人物近景。手工确定景别/关注对象/剪辑理由的镜头可选用 `storyboard_policy.version=1`，细则见[对白摄影与剪辑](../../references/decisions/shots.md#对白摄影与剪辑)。编译插入不改变源稿 Shot/Segment、对白或时间轴。

确定可见事件、视轴、运镜或参考图用途时，按[局部决策指南](../../references/decisions/shots.md)对应节执行；先排除不适用选项再查库，不强制每镜双候选辩论。

读[114 绑定合同](../../references/114-reference-binding-delivery-v4.3.6.md)。在 reference_requirements 写本镜确需的对象/素材版本/用途，与 assets 复核，不能把整个资产库都上传。首帧、尾帧、中间关键帧和构图图分开；未来状态不能提前继承。标签由 model 分配，shots 不写第二套绑定真值。

本文件是acheng-director随包专业子入口，按路径加载；主导演负责真值、版本、对象创建和最终合并。它不自动启动代理或调用模型。

先读[本分支核心合同](../../references/20-storyboard-compiler.md)与[专门规则](../../references/21-genre-camera-capacity.md)；同时遵守[模块回包合同](../../references/91-module-orchestration.md)。只读取本任务依赖，保留上游来源与冻结项。

先读确认剧本、场景地图、资产版本和必须可见事件。选择受限/全知视点、景别与路径；为每次切镜说明新增信息。绑定真实Previs家族并展开运动，静态构图不强行运动。按事件安全边界装箱，超窗或短尾不可行时返回边界问题。

返回既有shots的visual/camera/时序/角色位置及segments的镜头覆盖。不得改台词与胜负；由主导演建新对象骨架。和表演动作模块核对可见性。

字段写入白名单取[模块登记](../../data/module-registry.json)。回包包含request_id/input_revision/module/status/attempt/patch/evidence/unresolved；最多初次加一次有证据的修正。只改允许路径，不能把其他模块的建议直接写成已确认事实。
