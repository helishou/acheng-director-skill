# 62｜STYLE MOTHER 风格锚定合同

## 目的与边界

动画资产可以共享画风，但 `STYLE_MOTHER` 是可选的质量工具，不是制作或编译门槛。用户选择使用时，可先制作受控的 `STYLE_MOTHER` 参考图，再用于角色、场景、道具、特效和关键帧。它是视觉渲染语言的锚，不是故事海报、角色设定图或场景母图。未配置锚点时保留风格诊断并继续编译；只有真实选择为生成输入的参考文件缺失或内容哈希不符时，才阻止对应目标。

STYLE MOTHER 应包含一个不带剧情身份的通用主体（例如无脸中性模型或抽象人体比例体）、简单环境、一个代表性材料／道具和目标媒介。画面要能验收线条边缘、阴影分层、色板逻辑、材质响应、背景抽象、空气透视、轮廓可读性和动画关节可动性；禁止文字、标志、水印、网格、故事专属角色、复杂叙事构图、可识别脸部、品牌和场景地标。它必须有足够的主体、材质和空间层次来代表目标画风，但不能携带会污染后续身份、构图、动作或故事状态的内容。

必要时可追加两个探针，但不能替代母版：

- `STYLE_CHARACTER_PROBE`：通用头部、躯干和手部，验证脸部线条、皮肤／衣料分离与关节可读性；
- `STYLE_ENVIRONMENT_PROBE`：无角色环境与代表性材质，验证透视、景深、主光和背景细节衰减；
- `STYLE_EFFECT_PROBE`：只有视效占主导的项目才增加，验证粒子、辉光、烟尘和遮挡不吞掉动作轮廓。

不要用主角四视图、英雄海报、复杂分镜、情绪板或单张剧情关键帧作为唯一风格参考。它们会把身份、构图、几何或故事光线误传给所有资产。

## 数据合同

项目根可声明：

```json
{
  "style_lock": {
    "anchor_asset_id": "STYLE_MOTHER",
    "anchor_version": "v1",
    "status": "planned",
    "medium": "2d_cel",
    "preserve_scope": ["clean line weight", "flat cel shadow hierarchy", "warm-cool palette separation", "matte material response"],
    "exclude_scope": ["character identity", "face and body proportions", "scene layout", "pose and action", "exact light direction", "text and logo"],
    "apply_to_kinds": ["character", "costume", "injury", "scene", "prop", "vehicle", "keyframe", "effect"],
    "approved_file": null,
    "approved_sha256": null
  }
}
```

## 低污染 STYLE_MOTHER 提示词模板

```text
Create one clean style reference image for an animation production pipeline, not a story image and not a character design sheet. Show one neutral faceless mannequin-like subject with simple joints on a plain unbranded studio ground, plus one small material sample that represents the project's main surface response. Use the target medium: [2D cel / 3D cinematic / stop-motion / ink / other]. Demonstrate [line edge behavior], [shadow hierarchy], [palette roles], [surface response], [background abstraction], [air perspective] and [silhouette readability] with one broad motivated key light and restrained fill. Keep the composition quiet and centered so the rendering language can be judged clearly. No recognizable face, no named character, no costume identity, no story prop, no location landmark, no text, no logo, no watermark, no grid, no panel labels, no dramatic action, no complex narrative lighting, no branded object, no decorative visual noise.
```

需要风格锚点时，把图登记为 `STYLE_MOTHER`。提示词交付可附 `STYLE_MOTHER.image.txt`，由作者选择是否将其作为角色、场景、道具、特效和关键帧的真实输入。使用时明确只继承媒介、线条、阴影、材质响应与色调，排除身份、构图与动作。智能体仅在用户授权媒体生成时调用相应模型。

用户选择 STYLE_MOTHER 时，它登记为 `asset_plan` 中 `kind: style` 的节点，锚点卡使用 `recipe: style`。`planned` 表示提示词已准备；`generated` 表示真实媒体已归档并通过文件/版本/哈希核验；`approved` 只在实际审核后使用。已选择的锚点可作为依赖并用 `role: style` 绑定；角色身份、场景几何和构图参考仍各自保留。未审核但技术有效的图可使用，且保持 `generated` 状态。

## 权威优先级

1. 身份参考决定脸、身体、服装和道具事实；
2. 场景参考决定几何、地标、入口和遮挡；
3. 当前 ShotSpec 决定姿态、动作、机位、状态和精确光向；
4. STYLE MOTHER 只决定媒介、线条、阴影、色板、材质、背景抽象和空气深度。

风格锚定不能覆盖角色身份、场景拓扑、相机布局、动作方向、状态损伤、道具所有权或故事中的精确光位。参考清单必须写明保留与排除范围；缺少批准锚点时只能交风格资产草案和缺图依赖，不能把后续资产标记为 ready。

## 可选视觉检查

需要视觉检查时，可核对文字／标志／水印／网格、线宽、阴影层次、色板、材质、景深、轮廓和构图污染。机器校验字段、版本、文件和哈希；视觉一致性由用户自行查看，默认不写入 approved，也不阻断其他制作。

显式选择 required 策略时，apply_to_kinds 覆盖当前资产类型，style_lock 与锚点的状态、版本、文件路径和 SHA-256 必须一致。实际使用该参考的素材才需绑定真实槽位；未选择 STYLE_MOTHER 时，该策略报告只作为质量诊断，不阻止提示词编译。
