# H3 视频交付总览 · Acheng Director 生产台

## 总控台

项目：SERIAL_TIDE_ARCHIVE
总时长：180 秒 · 24/1 fps
段落数量：12 · 模式：autonomous_file_batch
状态：机器检查不等于平台已上传或影像已生成；缺素材与合同缺项保持草案。

## 创作摘要

三集各一分钟的沿海调查样例。档案员梅林起初把制度认证当作真相；工务员柏保留旧案责任。两人用不同来源交叉核对潮汐记录，区分抄录事实与责任人身份，最终保留异议而非用新结论覆盖旧证据。八条线路在12个完整场次内交汇；这是跨集机制示例，不声称已制作长篇成片。

## 资产目录与提示词

以下是可直接交给画布 Agent 的独立资产图提示词。提示词文件是生成指令，不是已经生成的图片；状态为 PLANNED 时仍需先补齐真实参考素材。

| 资产 | 状态 | 用途 | 参考依赖 | 提示词文件 |
|---|---|---|---|---|
| Meilin · neutral_identity · v1.0 (`ART_MEI`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_MEI.image.txt](asset_prompts/ART_MEI.image.txt) |
| Bo · neutral_identity · v1.0 (`ART_BO`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_BO.image.txt](asset_prompts/ART_BO.image.txt) |
| 潮汐档案室·空间母图 · v1.0 (`ART_ARCHIVE`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_ARCHIVE.image.txt](asset_prompts/ART_ARCHIVE.image.txt) |
| 码头值班亭·空间母图 · v1.0 (`ART_DOCK`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_DOCK.image.txt](asset_prompts/ART_DOCK.image.txt) |
| 两份潮汐原件·道具基准 · v1.0 (`ART_LEDGER`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_LEDGER.image.txt](asset_prompts/ART_LEDGER.image.txt) |
| 潮汐表与航运单·道具基准 · v1.0 (`ART_TIDE`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_TIDE.image.txt](asset_prompts/ART_TIDE.image.txt) |
| 封存通知与异议·道具基准 · v1.0 (`ART_NOTICE`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_NOTICE.image.txt](asset_prompts/ART_NOTICE.image.txt) |
| 门槛沙袋·道具基准 · v1.0 (`ART_SANDBAG`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_SANDBAG.image.txt](asset_prompts/ART_SANDBAG.image.txt) |
| 铅笔纸签与独立比对页 · v1.0 (`ART_STATIONERY`) | PROMPT_READY | Create the single still specified in the complete prompt. | 无 | [asset_prompts/ART_STATIONERY.image.txt](asset_prompts/ART_STATIONERY.image.txt) |
| 第一集开场·原件对照 · v1.0 (`ART_KEYFRAME_01`) | PLANNED | Create the single still specified in the complete prompt. | Reference image 1: ART_MEI, Reference image 2: ART_BO, Reference image 3: ART_ARCHIVE, Reference image 4: ART_LEDGER, Reference image 5: ART_STATIONERY | [asset_prompts/ART_KEYFRAME_01.draft.txt](asset_prompts/ART_KEYFRAME_01.draft.txt) |
| 第二集开场·保留异议 · v1.0 (`ART_KEYFRAME_05`) | PLANNED | Create the single still specified in the complete prompt. | Reference image 1: ART_MEI, Reference image 2: ART_BO, Reference image 3: ART_ARCHIVE, Reference image 4: ART_LEDGER, Reference image 5: ART_NOTICE | [asset_prompts/ART_KEYFRAME_05.draft.txt](asset_prompts/ART_KEYFRAME_05.draft.txt) |
| 第三集开场·独立佐证 · v1.0 (`ART_KEYFRAME_09`) | PLANNED | Create the single still specified in the complete prompt. | Reference image 1: ART_MEI, Reference image 2: ART_BO, Reference image 3: ART_ARCHIVE, Reference image 4: ART_LEDGER, Reference image 5: ART_STATIONERY | [asset_prompts/ART_KEYFRAME_09.draft.txt](asset_prompts/ART_KEYFRAME_09.draft.txt) |

### 可复制资产提示词

#### Meilin · neutral_identity · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_MEI.image.txt](asset_prompts/ART_MEI.image.txt)

独立上传卡：[ART_MEI.asset-upload.md](ART_MEI.asset-upload.md)

### Meilin · neutral_identity · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：character · 状态版本：neutral_identity / 未指定

[完整提示词/草案](<asset_prompts/ART_MEI.image.txt>) · SHA-256：48f5b81d764aed312cea2d88d281bdeaad563f360ac75f7d7dead4d75f1cb44a

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
This is the Meilin character identity asset in the approved neutral_identity state. Create one clean four-view character turnaround board in a fixed 2x2 grid. Top left: front face above the clavicle. Top right: right profile face above the clavicle. Bottom left: headless front costume full body starting below the clavicle; completely crop out head and face, arms relaxed down, legs and shoes complete. Bottom right: complete back full body from back of head to soles, showing all rear attachments actually defined for this character. Neutral light-grey background, orthographic, no perspective distortion. Identity references lock only specified character traits, never background or pose. Do not invent traits from another character. Keep the same proportions, costume, hairstyle, facial features, neutral standing pose, lighting and background across all four panels; preserve only the project's actual character features and visual style. No text, letters, numbers, symbols, watermark, logo or UI. Avoid head or face in the bottom-left panel, missing legs or shoes, exaggerated perspective, action poses, weapons, extra figures or costume changes. Top and bottom row heights must be in a 1:2 ratio: top row occupies one third of the board height, bottom row occupies two thirds. The two columns have equal widths. Do not use four equal-height panels. Create a neutral full-body live-action character reference. Meilin is a 32-year-old woman with a narrow oval face, straight black eyebrows and chin-length dark hair tucked behind her left ear. She wears a faded blue cotton jacket, cream shirt and dark straight trousers; her hands are uninjured. Use one broad upper-left light with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### Bo · neutral_identity · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_BO.image.txt](asset_prompts/ART_BO.image.txt)

独立上传卡：[ART_BO.asset-upload.md](ART_BO.asset-upload.md)

### Bo · neutral_identity · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：character · 状态版本：neutral_identity / 未指定

[完整提示词/草案](<asset_prompts/ART_BO.image.txt>) · SHA-256：bb1f33e4f648264ca218db68c8189b372631da5700942baf2fdbe92b19fe0457

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
This is the Bo character identity asset in the approved neutral_identity state. Create one clean four-view character turnaround board in a fixed 2x2 grid. Top left: front face above the clavicle. Top right: right profile face above the clavicle. Bottom left: headless front costume full body starting below the clavicle; completely crop out head and face, arms relaxed down, legs and shoes complete. Bottom right: complete back full body from back of head to soles, showing all rear attachments actually defined for this character. Neutral light-grey background, orthographic, no perspective distortion. Identity references lock only specified character traits, never background or pose. Do not invent traits from another character. Keep the same proportions, costume, hairstyle, facial features, neutral standing pose, lighting and background across all four panels; preserve only the project's actual character features and visual style. No text, letters, numbers, symbols, watermark, logo or UI. Avoid head or face in the bottom-left panel, missing legs or shoes, exaggerated perspective, action poses, weapons, extra figures or costume changes. Top and bottom row heights must be in a 1:2 ratio: top row occupies one third of the board height, bottom row occupies two thirds. The two columns have equal widths. Do not use four equal-height panels. Create a neutral full-body live-action character reference. Bo is a 40-year-old man with a broad face, short salt-and-pepper hair and a small pale scar on his left cheek. He wears a brown canvas vest over a rolled-sleeve gray shirt and dark work trousers; his hands are uninjured. Use one broad upper-left light with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 潮汐档案室·空间母图 · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_ARCHIVE.image.txt](asset_prompts/ART_ARCHIVE.image.txt)

独立上传卡：[ART_ARCHIVE.asset-upload.md](ART_ARCHIVE.asset-upload.md)

### 潮汐档案室·空间母图 · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_ARCHIVE.image.txt>) · SHA-256：bf5e7afc10966b8c9519a7a2f836436e679593a4f2d951f74179f4c08a31d38e

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
Create an unoccupied live-action environment reference. The harbor archive has a waist-high oak reading table, one frosted east window, a north shelf of cloth-bound ledgers and a west door. Soft window light falls across the table; the shelf remains in broad shadow. Use the stated world-space light source, keeping its direction consistent across the scene, with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 码头值班亭·空间母图 · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_DOCK.image.txt](asset_prompts/ART_DOCK.image.txt)

独立上传卡：[ART_DOCK.asset-upload.md](ART_DOCK.asset-upload.md)

### 码头值班亭·空间母图 · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_DOCK.image.txt>) · SHA-256：c7cbd2ea77f5ade8db196a33f0b0675209e1d60a747711e3831d926527d8bf8b

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
Create an unoccupied live-action environment reference. The dock watch hut has a fixed timber counter, an east window overlooking the tide gauge, a west door and a brass bell mounted on its north post. A waist-high manual-bypass cabinet below the east window bears an unbroken paper seal. Broad overcast daylight enters from the east; wet boards remain matte except at small puddles. Use the stated world-space light source, keeping its direction consistent across the scene, with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 两份潮汐原件·道具基准 · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_LEDGER.image.txt](asset_prompts/ART_LEDGER.image.txt)

独立上传卡：[ART_LEDGER.asset-upload.md](ART_LEDGER.asset-upload.md)

### 两份潮汐原件·道具基准 · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_LEDGER.image.txt>) · SHA-256：eda69c6833115519ff111575b1f0479b91e3c5cf7862f7b29b6f51dc7e75e7ea

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
Create a live-action reference of two cloth-bound tide ledgers lying open side by side, with cream paper and matching tiny ink notches in their right margins. Other writing is indistinct, with no invented readable text. Use one broad upper-left light with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 潮汐表与航运单·道具基准 · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_TIDE.image.txt](asset_prompts/ART_TIDE.image.txt)

独立上传卡：[ART_TIDE.asset-upload.md](ART_TIDE.asset-upload.md)

### 潮汐表与航运单·道具基准 · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_TIDE.image.txt>) · SHA-256：5054c0b2ffb8cd5c29703ba1d28d440175b10fee64a5d656812ad961200a198c

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
Create a live-action reference of a cream tide sheet and a separate shipping manifest lying flat side by side on aged timber. Show neat columns and small ink marks without invented legible writing. Use one broad upper-left light with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 封存通知与异议·道具基准 · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_NOTICE.image.txt](asset_prompts/ART_NOTICE.image.txt)

独立上传卡：[ART_NOTICE.asset-upload.md](ART_NOTICE.asset-upload.md)

### 封存通知与异议·道具基准 · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_NOTICE.image.txt>) · SHA-256：e2eb81f98d6dc1798ebd27824c27bf3291e185965dfe2e9b118bc3c2fcd70147

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
Create a live-action prop reference of one cream closure notice and a separate written objection on an oak tabletop. Use visible ruled receipt fields and a small blue signature mark, with other writing indistinct and no invented legible text. Use one broad upper-left light with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 门槛沙袋·道具基准 · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_SANDBAG.image.txt](asset_prompts/ART_SANDBAG.image.txt)

独立上传卡：[ART_SANDBAG.asset-upload.md](ART_SANDBAG.asset-upload.md)

### 门槛沙袋·道具基准 · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_SANDBAG.image.txt>) · SHA-256：ceb8bb6e51002b2f8a6e102ef1abd15084af63c801d943489923534043a84ba2

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
Create a live-action prop reference of one squat tan canvas sandbag tied with dark cord. Its bottom flattens under its weight and its seams remain visible; the canvas has a few broad folds and no printed writing. Use one broad upper-left light with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 铅笔纸签与独立比对页 · v1.0 · PROMPT_READY

完整文件：[asset_prompts/ART_STATIONERY.image.txt](asset_prompts/ART_STATIONERY.image.txt)

独立上传卡：[ART_STATIONERY.asset-upload.md](ART_STATIONERY.asset-upload.md)

### 铅笔纸签与独立比对页 · v1.0 · 资产图上传卡

状态：PROMPT_READY · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_STATIONERY.image.txt>) · SHA-256：c652b1247a28df5530015bf270efe94477d4063a8f31d87b00e8a6193e2a575b

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

本资产无需上传参考图；按完整正文制作，生成后仍需批准。

下一步：核对生成模式并复制完整提示词，无需上传参考图；生成后记录真实文件、版本和人工批准。


```text
Create a live-action prop reference of one short wooden pencil, two narrow cream paper markers and one loose comparison sheet with two ruled columns. Keep the paper matte and the graphite tip dark; marks are indistinct without invented readable words. Use one broad upper-left light with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 第一集开场·原件对照 · v1.0 · PLANNED

完整文件：[asset_prompts/ART_KEYFRAME_01.draft.txt](asset_prompts/ART_KEYFRAME_01.draft.txt)

独立上传卡：[ART_KEYFRAME_01.asset-upload.md](ART_KEYFRAME_01.asset-upload.md)

### 第一集开场·原件对照 · v1.0 · 资产图上传卡

状态：PLANNED · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_KEYFRAME_01.draft.txt>) · SHA-256：062eb70e986a8a1b1536d363d7dbb5073666834b0f65f7c6eca3264ffb6d1277

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

逐项上传实际图片；不上传 .image.txt，缺失槽位不重排编号。

| 槽位 | 实际图片/缺项 | 用途/对象 | 版本 | 必须保留 | 禁止继承 |
|---|---|---|---|---|---|
| 1 | 待提供：ART_MEI；生成并批准后重新编译 | identity / Meilin the adult archive clerk | v1.0 | her face, hair, adult proportions and blue cotton jacket | unrelated pose, crop and lighting; use the target composition described below |
| 2 | 待提供：ART_BO；生成并批准后重新编译 | identity / Bo the adult dock mechanic | v1.0 | his face, cheek scar and brown canvas vest | unrelated pose, crop and lighting; use the target composition described below |
| 3 | 待提供：ART_ARCHIVE；生成并批准后重新编译 | scene / the archive room | v1.0 | the oak table, east window, north shelf and west door | unrelated pose, crop and lighting; use the target composition described below |
| 4 | 待提供：ART_LEDGER；生成并批准后重新编译 | composition / the two original ledgers | v1.0 | the two cloth bindings and matching ink notches | unrelated pose, crop and lighting; use the target composition described below |
| 5 | 待提供：ART_STATIONERY；生成并批准后重新编译 | composition / the pencil and paper markers | v1.0 | the short wooden pencil and narrow cream paper markers | source background and camera position |

下一步：先补齐缺项或修复正文合同，再重新导出到新目录；当前草案不可提交。


```text
DRAFT — required references or standalone prompt contract is unresolved.

Reference image 1 supplies identity guidance for Meilin the adult archive clerk. Preserve her face, hair, adult proportions and blue cotton jacket. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 2 supplies identity guidance for Bo the adult dock mechanic. Preserve his face, cheek scar and brown canvas vest. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 3 supplies scene guidance for the archive room. Preserve the oak table, east window, north shelf and west door. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 4 supplies composition guidance for the two original ledgers. Preserve the two cloth bindings and matching ink notches. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 5 supplies composition guidance for the pencil and paper markers. Preserve the short wooden pencil and narrow cream paper markers. Do not inherit source background and camera position.

Create one live-action medium two-shot before any gesture begins. Meilin is a 32-year-old woman with a narrow oval face, straight black eyebrows and chin-length dark hair tucked behind her left ear. She wears a faded blue cotton jacket, cream shirt and dark straight trousers; her hands are uninjured. Bo is a 40-year-old man with a broad face, short salt-and-pepper hair and a small pale scar on his left cheek. He wears a brown canvas vest over a rolled-sleeve gray shirt and dark work trousers; his hands are uninjured. The harbor archive has a waist-high oak reading table, one frosted east window, a north shelf of cloth-bound ledgers and a west door. Soft window light falls across the table; the shelf remains in broad shadow. Meilin stands left and Bo right, both looking down at two open ledgers lying flat between them. Their hands rest separately on the table edge. Use the stated world-space light source, keeping its direction consistent across the scene, with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text. A short wooden pencil and two narrow cream paper markers lie beside the original ledgers.
```

#### 第二集开场·保留异议 · v1.0 · PLANNED

完整文件：[asset_prompts/ART_KEYFRAME_05.draft.txt](asset_prompts/ART_KEYFRAME_05.draft.txt)

独立上传卡：[ART_KEYFRAME_05.asset-upload.md](ART_KEYFRAME_05.asset-upload.md)

### 第二集开场·保留异议 · v1.0 · 资产图上传卡

状态：PLANNED · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_KEYFRAME_05.draft.txt>) · SHA-256：753f21f8f407ad478d1faa0f999ff2306e96a425a8e73d439e2e89ef142bab35

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

逐项上传实际图片；不上传 .image.txt，缺失槽位不重排编号。

| 槽位 | 实际图片/缺项 | 用途/对象 | 版本 | 必须保留 | 禁止继承 |
|---|---|---|---|---|---|
| 1 | 待提供：ART_MEI；生成并批准后重新编译 | identity / Meilin the adult archive clerk | v1.0 | her face, hair, adult proportions and blue cotton jacket | unrelated pose, crop and lighting; use the target composition described below |
| 2 | 待提供：ART_BO；生成并批准后重新编译 | identity / Bo the adult dock mechanic | v1.0 | his face, cheek scar and brown canvas vest | unrelated pose, crop and lighting; use the target composition described below |
| 3 | 待提供：ART_ARCHIVE；生成并批准后重新编译 | scene / the archive room | v1.0 | the oak table, east window, north shelf and west door | unrelated pose, crop and lighting; use the target composition described below |
| 4 | 待提供：ART_LEDGER；生成并批准后重新编译 | composition / the two original ledgers | v1.0 | the two cloth bindings and matching ink notches | unrelated pose, crop and lighting; use the target composition described below |
| 5 | 待提供：ART_NOTICE；生成并批准后重新编译 | composition / the closure notice and objection | v1.0 | their paper format and ruled receipt fields | unrelated pose, crop and lighting; use the target composition described below |

下一步：先补齐缺项或修复正文合同，再重新导出到新目录；当前草案不可提交。


```text
DRAFT — required references or standalone prompt contract is unresolved.

Reference image 1 supplies identity guidance for Meilin the adult archive clerk. Preserve her face, hair, adult proportions and blue cotton jacket. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 2 supplies identity guidance for Bo the adult dock mechanic. Preserve his face, cheek scar and brown canvas vest. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 3 supplies scene guidance for the archive room. Preserve the oak table, east window, north shelf and west door. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 4 supplies composition guidance for the two original ledgers. Preserve the two cloth bindings and matching ink notches. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 5 supplies composition guidance for the closure notice and objection. Preserve their paper format and ruled receipt fields. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Create one live-action medium two-shot before any gesture begins. Meilin is a 32-year-old woman with a narrow oval face, straight black eyebrows and chin-length dark hair tucked behind her left ear. She wears a faded blue cotton jacket, cream shirt and dark straight trousers; her hands are uninjured. Bo is a 40-year-old man with a broad face, short salt-and-pepper hair and a small pale scar on his left cheek. He wears a brown canvas vest over a rolled-sleeve gray shirt and dark work trousers; his hands are uninjured. The harbor archive has a waist-high oak reading table, one frosted east window, a north shelf of cloth-bound ledgers and a west door. Soft window light falls across the table; the shelf remains in broad shadow. Meilin stands left and Bo right, both looking down at two open ledgers lying flat between them. Their hands rest separately on the table edge. A closure notice and separate written objection lie beside the ledgers, with the receipt line visible. Use the stated world-space light source, keeping its direction consistent across the scene, with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

#### 第三集开场·独立佐证 · v1.0 · PLANNED

完整文件：[asset_prompts/ART_KEYFRAME_09.draft.txt](asset_prompts/ART_KEYFRAME_09.draft.txt)

独立上传卡：[ART_KEYFRAME_09.asset-upload.md](ART_KEYFRAME_09.asset-upload.md)

### 第三集开场·独立佐证 · v1.0 · 资产图上传卡

状态：PLANNED · NOT_UPLOADED · visual_status=UNVERIFIED

生成模式：GENERATE · 资产类型：未指定 · 状态版本：未指定 / 未指定

[完整提示词/草案](<asset_prompts/ART_KEYFRAME_09.draft.txt>) · SHA-256：b58b3a36d7a651f960ecd280ade0a676e7e6dd4b55f084a8f7f3e47102bfee2b

本卡用于生成这一个资产；H3 视频请求的参考图和编号另见对应 Segment 上传卡。

逐项上传实际图片；不上传 .image.txt，缺失槽位不重排编号。

| 槽位 | 实际图片/缺项 | 用途/对象 | 版本 | 必须保留 | 禁止继承 |
|---|---|---|---|---|---|
| 1 | 待提供：ART_MEI；生成并批准后重新编译 | identity / Meilin the adult archive clerk | v1.0 | her face, hair, adult proportions and blue cotton jacket | unrelated pose, crop and lighting; use the target composition described below |
| 2 | 待提供：ART_BO；生成并批准后重新编译 | identity / Bo the adult dock mechanic | v1.0 | his face, cheek scar and brown canvas vest | unrelated pose, crop and lighting; use the target composition described below |
| 3 | 待提供：ART_ARCHIVE；生成并批准后重新编译 | scene / the archive room | v1.0 | the oak table, east window, north shelf and west door | unrelated pose, crop and lighting; use the target composition described below |
| 4 | 待提供：ART_LEDGER；生成并批准后重新编译 | composition / the two original ledgers | v1.0 | the two cloth bindings and matching ink notches | unrelated pose, crop and lighting; use the target composition described below |
| 5 | 待提供：ART_STATIONERY；生成并批准后重新编译 | composition / the independent comparison sheet | v1.0 | its two ruled columns and short wooden pencil | unrelated pose, crop and lighting; use the target composition described below |

下一步：先补齐缺项或修复正文合同，再重新导出到新目录；当前草案不可提交。


```text
DRAFT — required references or standalone prompt contract is unresolved.

Reference image 1 supplies identity guidance for Meilin the adult archive clerk. Preserve her face, hair, adult proportions and blue cotton jacket. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 2 supplies identity guidance for Bo the adult dock mechanic. Preserve his face, cheek scar and brown canvas vest. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 3 supplies scene guidance for the archive room. Preserve the oak table, east window, north shelf and west door. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 4 supplies composition guidance for the two original ledgers. Preserve the two cloth bindings and matching ink notches. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Reference image 5 supplies composition guidance for the independent comparison sheet. Preserve its two ruled columns and short wooden pencil. Do not inherit unrelated pose, crop and lighting; use the target composition described below.

Create one live-action medium two-shot before any gesture begins. Meilin is a 32-year-old woman with a narrow oval face, straight black eyebrows and chin-length dark hair tucked behind her left ear. She wears a faded blue cotton jacket, cream shirt and dark straight trousers; her hands are uninjured. Bo is a 40-year-old man with a broad face, short salt-and-pepper hair and a small pale scar on his left cheek. He wears a brown canvas vest over a rolled-sleeve gray shirt and dark work trousers; his hands are uninjured. The harbor archive has a waist-high oak reading table, one frosted east window, a north shelf of cloth-bound ledgers and a west door. Soft window light falls across the table; the shelf remains in broad shadow. Meilin stands left and Bo right, both looking down at two open ledgers lying flat between them. Their hands rest separately on the table edge. A separate two-column comparison sheet lies beside both original ledgers, its edge aligned with them. Use the stated world-space light source, keeping its direction consistent across the scene, with readable shadow planes and localized contact shadows. Keep the principal silhouette and functional details clear, with broad quiet background shapes. Separate the stated materials through their surface response. Avoid ghost texture, duplicated anatomy and unintended text.
```

## 段落地图（分段地图）

| 段落 | 时间 | 时长 | H3模式 | 创作事件/意图 | 状态 |
|---|---|---:|---|---|---|
| SERIAL_SEG_01 | 0.000s–15.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_02 | 15.000s–30.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_03 | 30.000s–45.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_04 | 45.000s–60.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_05 | 60.000s–75.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_06 | 75.000s–90.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_07 | 90.000s–105.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_08 | 105.000s–120.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_09 | 120.000s–135.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_10 | 135.000s–150.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_11 | 150.000s–165.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |
| SERIAL_SEG_12 | 165.000s–180.000s | 15s | T2VA | 见完整 H3 正文 | READY_TO_UPLOAD |

## 每段上传参考助手

每张卡只覆盖一个 Segment；先看状态与实际文件，再按标签顺序上传。Subject 是内容对象，不是额外上传槽位。

### SERIAL_SEG_01 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_01.h3.txt) · [独立上传卡](SERIAL_SEG_01.upload.md)

绑定版本：`50c0e130d5fa1ba0147592d9785c5222b33d5aafe7a45af819e45245f73a032d` · 正文 SHA-256：`d3a7a9ff652c6d29fc5cd93b7c4fb56847fb2743fd0bf0e2e3d608fa39fbcd80`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_02 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_02.h3.txt) · [独立上传卡](SERIAL_SEG_02.upload.md)

绑定版本：`5e0bb2b50b7221ca413323bb282ed79b6e6af1f51268175c45a8a909fa97b0c7` · 正文 SHA-256：`54de992e7dc18c1ef9bf10f6fc1d14277fb3e7239d0f3c73ac82f792e2ca4405`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_03 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_03.h3.txt) · [独立上传卡](SERIAL_SEG_03.upload.md)

绑定版本：`6c88bfe8dbaa5e0a5f6d01899ee3ba3ee766266ae940afae17b7d82e7e175149` · 正文 SHA-256：`b8d96507560e5814055bf71d58f06d718e470a753ecaed570f3d01e58a84c692`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_04 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_04.h3.txt) · [独立上传卡](SERIAL_SEG_04.upload.md)

绑定版本：`2268020a4036b7def023a77908153f2e0f41b01d192dbd62f220c58b8020878d` · 正文 SHA-256：`c711c3fb0ad338c032f4fa2146d1bffe55cf1337bb296a349feda379cc534fef`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_05 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_05.h3.txt) · [独立上传卡](SERIAL_SEG_05.upload.md)

绑定版本：`16bdfd3c894f6c64b99086888bf74a01e5aa7ff8acb1d6e500aa320ea53c067a` · 正文 SHA-256：`4615ab438d1afc7140801db1331c07110e7372dd0b242ce1b7b1e6f0cbdce4a2`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_06 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_06.h3.txt) · [独立上传卡](SERIAL_SEG_06.upload.md)

绑定版本：`990d3144997b9857d6eaebbf6564ac2ec40a3911c4789079f7b181c0f15769be` · 正文 SHA-256：`32611201b460da4842454f290046d8cad0f19a53d453857f1c4c31489e454e3a`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_07 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_07.h3.txt) · [独立上传卡](SERIAL_SEG_07.upload.md)

绑定版本：`b31583e392bd0bf3ddf2c0f8ef7b1acd3b8cfcbe7f5534e064f69ecf13f2cd5c` · 正文 SHA-256：`4a544167dc10d5e394bb3f410499612148f200a67a6f3fdfdf245be1940f21ea`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_08 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_08.h3.txt) · [独立上传卡](SERIAL_SEG_08.upload.md)

绑定版本：`519dd7fabbf6a6c9a75f304cbbdb64294397a88e4932188b37bb951fc433398b` · 正文 SHA-256：`600ff5dbe5724d3fc75406e7b200b0491f7ed19150456f84e846e869644a5e49`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_09 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_09.h3.txt) · [独立上传卡](SERIAL_SEG_09.upload.md)

绑定版本：`efe110d50e0d6ceec36af9b2ae71b22fa770fd8944fd55d1680796cdacb15f9a` · 正文 SHA-256：`ccddea27af764c97fb82f17bc5e621e094f7cb86463df5149047b5d58e97f16a`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_10 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_10.h3.txt) · [独立上传卡](SERIAL_SEG_10.upload.md)

绑定版本：`d7059790351812a26fa0090cc5a9590da1d30cdf70573f8a44655706fd9ea4fb` · 正文 SHA-256：`e7584a143888782d6b2c8a4ec5f0629b4ced2285221b7ba5c0713787293b077f`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_11 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_11.h3.txt) · [独立上传卡](SERIAL_SEG_11.upload.md)

绑定版本：`f0b77abc539e6e10e406b909eb8f42a57cebf89be4a4f55b7eb1df000d98fc90` · 正文 SHA-256：`c3efa0117fda08011aa4660ec7e69ddbb7ba68ccc97f2b911d5b7193f090c5fd`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

### SERIAL_SEG_12 · T2VA · 15 秒

提交状态：READY_TO_UPLOAD · 本地绑定不等于平台已上传 · visual_status=UNVERIFIED

[完整正文/草案](SERIAL_SEG_12.h3.txt) · [独立上传卡](SERIAL_SEG_12.upload.md)

绑定版本：`bb358354f04125b73389e3c17243e5dfd123def5cb66f8e984a3f5dc72f1c19f` · 正文 SHA-256：`5d505a81bbf3699cf389d14db6e740b63f444c7bb3f1d38998434b63572ef584`

参考图上传助手：本段无需上传参考图；已明确选择 T2VA。跨段身份效果仍需生成后检查。


下一步：依次上传本卡真实媒体，在实际入口核对模式、时长、分类编号和素材版本，再粘贴完整正文。未完成入口核对前不宣称可直接提交。
平台上传：当前卡不证明云端已有素材。上传确认必须另附绑定本段、正文与素材哈希的入口回执。

## H3 正文文件

每个文件都是独立请求；请复制对应文件的完整正文，不把本页说明、manifest 或上传卡混入模型输入。

| 段落 | 状态 | 完整 H3/草案 | 独立上传卡 |
|---|---|---|---|
| SERIAL_SEG_01 | READY_TO_UPLOAD | [SERIAL_SEG_01.h3.txt](SERIAL_SEG_01.h3.txt) | [SERIAL_SEG_01.upload.md](SERIAL_SEG_01.upload.md) |
| SERIAL_SEG_02 | READY_TO_UPLOAD | [SERIAL_SEG_02.h3.txt](SERIAL_SEG_02.h3.txt) | [SERIAL_SEG_02.upload.md](SERIAL_SEG_02.upload.md) |
| SERIAL_SEG_03 | READY_TO_UPLOAD | [SERIAL_SEG_03.h3.txt](SERIAL_SEG_03.h3.txt) | [SERIAL_SEG_03.upload.md](SERIAL_SEG_03.upload.md) |
| SERIAL_SEG_04 | READY_TO_UPLOAD | [SERIAL_SEG_04.h3.txt](SERIAL_SEG_04.h3.txt) | [SERIAL_SEG_04.upload.md](SERIAL_SEG_04.upload.md) |
| SERIAL_SEG_05 | READY_TO_UPLOAD | [SERIAL_SEG_05.h3.txt](SERIAL_SEG_05.h3.txt) | [SERIAL_SEG_05.upload.md](SERIAL_SEG_05.upload.md) |
| SERIAL_SEG_06 | READY_TO_UPLOAD | [SERIAL_SEG_06.h3.txt](SERIAL_SEG_06.h3.txt) | [SERIAL_SEG_06.upload.md](SERIAL_SEG_06.upload.md) |
| SERIAL_SEG_07 | READY_TO_UPLOAD | [SERIAL_SEG_07.h3.txt](SERIAL_SEG_07.h3.txt) | [SERIAL_SEG_07.upload.md](SERIAL_SEG_07.upload.md) |
| SERIAL_SEG_08 | READY_TO_UPLOAD | [SERIAL_SEG_08.h3.txt](SERIAL_SEG_08.h3.txt) | [SERIAL_SEG_08.upload.md](SERIAL_SEG_08.upload.md) |
| SERIAL_SEG_09 | READY_TO_UPLOAD | [SERIAL_SEG_09.h3.txt](SERIAL_SEG_09.h3.txt) | [SERIAL_SEG_09.upload.md](SERIAL_SEG_09.upload.md) |
| SERIAL_SEG_10 | READY_TO_UPLOAD | [SERIAL_SEG_10.h3.txt](SERIAL_SEG_10.h3.txt) | [SERIAL_SEG_10.upload.md](SERIAL_SEG_10.upload.md) |
| SERIAL_SEG_11 | READY_TO_UPLOAD | [SERIAL_SEG_11.h3.txt](SERIAL_SEG_11.h3.txt) | [SERIAL_SEG_11.upload.md](SERIAL_SEG_11.upload.md) |
| SERIAL_SEG_12 | READY_TO_UPLOAD | [SERIAL_SEG_12.h3.txt](SERIAL_SEG_12.h3.txt) | [SERIAL_SEG_12.upload.md](SERIAL_SEG_12.upload.md) |

## 执行顺序与阻塞项

1. 待制作资产先按自己的上传卡上传实际参考图、提交完整资产提示词；生成后登记真实文件、版本、哈希并批准，再重新编译下游。已经批准且未变化的资产直接复用。
2. 打开每个 Segment 的上传卡，只上传该段表内的真实媒体，并在入口核对模式、时长和槽位编号。
3. 打开对应 H3 文件，复制完整正文提交；`CHAT_DELIVERY.md` 不替代 H3 正文文件。
4. 平台上传后另行保存入口回执；本地 `READY_TO_UPLOAD` 不等于平台已上传，`visual_status=UNVERIFIED` 不得升级。

当前阻塞：
- 资产 ART_KEYFRAME_01：先按独立上传卡补齐参考素材或正文合同；不可提交草案
- 资产 ART_KEYFRAME_05：先按独立上传卡补齐参考素材或正文合同；不可提交草案
- 资产 ART_KEYFRAME_09：先按独立上传卡补齐参考素材或正文合同；不可提交草案

自动文件模式：长 H3 正文留在独立文件；本页保留创作摘要、资产提示词、分段地图和每段上传助手，不能用总清单链接代替操作卡。

