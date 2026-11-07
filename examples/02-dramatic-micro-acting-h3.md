# 文戏对峙｜把钥匙交出来

状态：完整生产卡及提示词已编译；图像仅有随包灰模构图示意，未调用影视生成模型。

- 总时长：20 秒；最大生成窗：10 秒；24 fps。
- 数据真值源：[02-drama.production.json](02-drama.production.json)。
- 声音：现场音；非叙事配乐 N/A。

## 剧情与人物选择

受伤的陆川一开始仍攥着钥匙；岑禾没有抢夺，只留出接收的手。陆川承认之前拒绝协作，并把钥匙交给她。岑禾以共同行动回应，右腕伤势没有因为情绪转变消失。

A：钥匙是否交出。
B：独断保护转向共同承担。
C：前次事故仅由明确台词提出，本段不擅自补回忆。

五阶段可见弧光：开场攥钥匙保留控制 → 看见包扎手腕承受旧选择代价 → 松开拇指先试探 → 交钥匙承担失去控制 → 停手不夺回，接受一起行动。

## 登记场景与人物

```json
{
  "scenes": [
    {
      "id": "S01",
      "name": "维修室",
      "space": "One desk, east window, west doorway and a fixed brass-key hook",
      "version": "v1",
      "entrances": [
        "west service route"
      ],
      "exits": [
        "east service route"
      ],
      "landmarks": [
        "One desk, east window, west doorway and a fixed brass-key hook"
      ],
      "key_light": "fixed world-east source",
      "prompt_description": "The maintenance room contains one wooden desk, an east-facing window, a west doorway and a brass-key hook on the rear dark wall. Soft east-window light crosses the desk and falls off toward the west wall."
    }
  ],
  "characters": [
    {
      "id": "CHAR_LU",
      "name": "Lu Chuan",
      "height_m": 1.8,
      "identity": "Original design; appearance defined by the production prose, not by a franchise reference",
      "prompt_description": "Lu Chuan is a 34-year-old man, 1.80 meters tall, with balanced adult proportions, naturally broad shoulders, a square jaw, short dark hair and a short scar above his right eyebrow. He wears a gray woven work jacket over a gray shirt and a functional waist belt."
    },
    {
      "id": "CHAR_CEN",
      "name": "Cen He",
      "height_m": 1.7,
      "identity": "Original design; appearance defined by the production prose, not by a franchise reference",
      "prompt_description": "Cen He is a 32-year-old woman, 1.70 meters tall, with a lean adult build, oval face, dark almond-shaped eyes and dark hair tied low behind her head. She wears an olive canvas coat over a cream work shirt and dark straight trousers."
    }
  ]
}
```

## 逐镜生产卡

### FILM-S01-SH001｜0.000–10.000 秒

Lu Chuan, an adult men with a short scar over the right eyebrow and a gray work jacket, sits on the left side of the maintenance desk with his bandaged right wrist supported on a folded cloth and the brass key held in his left hand at the edge of the desk. Cen He, an adult technician with tied dark hair and a pale workshop coat, sits on the right with both forearms on the desk and her receiving palm open between them, empty, a hand's width from the key. The east window throws soft gray daylight across the desk from behind Cen's shoulder, so Lu's face carries the shadow side and Cen's hands stay lit; the brass key picks up one small highlight along its ring. The wooden desk, the window, the west doorway and the brass hook on the rear wall hold fixed positions, and the room's only sound is ventilation under distant rain. The camera advances twenty centimeters in a medium close two-shot, keeping Lu's eyes, both shoulder lines and his left hand visible without a cut, and it never crosses the desk edge. Framing holds Lu on the left and Cen on the right with the open palm between them. Nothing passes in front of the lens. Lu's first change is a movement of attention, not of body: his gaze leaves the key, travels to Cen's open palm, rests there long enough to register that the palm is not reaching, and then rises to her eyes. He interrupts one inhale halfway, swallows once, and releases a longer breath than the one he took. His left shoulder settles downward by a small visible amount, and the fingers of his left hand loosen on the key ring without letting go. His jaw stays tense until the breath finishes and only then eases, which is the first moment his face stops bracing against the room. Cen does not answer the movement with a movement of her own. She keeps her eyes on his rather than on the key, her shoulders stay level, and her open palm remains exactly where it was, close enough to receive and far enough to leave him room to decline. Her breath stays quiet, with one small inhale before she speaks. Nothing in her posture asks him to hurry. When Lu speaks, he speaks slowly in a low, slightly rough voice, with the admission landing before the offer: he says the previous refusal was his own, and then tells her to take it now. His left thumb slides off the key ring as the last clause ends, so the hand movement finishes after the words instead of anticipating them. Fabric shifts softly at his elbow, the brass key rings once against the desk, and the ventilation continues underneath. At the end of the shot the key is still in Lu's left hand but no longer gripped, his thumb is off the ring, the bandaged right wrist stays on the cloth, and Cen's palm is still open with nothing in it.

```json
{
  "id": "FILM-S01-SH001",
  "scene_id": "S01",
  "start_frame": 0,
  "end_frame": 240,
  "visual": "Lu Chuan, an adult men with a short scar over the right eyebrow and a gray work jacket, sits on the left side of the maintenance desk with his bandaged right wrist supported on a folded cloth and the brass key held in his left hand at the edge of the desk. Cen He, an adult technician with tied dark hair and a pale workshop coat, sits on the right with both forearms on the desk and her receiving palm open between them, empty, a hand's width from the key. The east window throws soft gray daylight across the desk from behind Cen's shoulder, so Lu's face carries the shadow side and Cen's hands stay lit; the brass key picks up one small highlight along its ring. The wooden desk, the window, the west doorway and the brass hook on the rear wall hold fixed positions, and the room's only sound is ventilation under distant rain. The camera advances twenty centimeters in a medium close two-shot, keeping Lu's eyes, both shoulder lines and his left hand visible without a cut, and it never crosses the desk edge. Framing holds Lu on the left and Cen on the right with the open palm between them. Nothing passes in front of the lens. Lu's first change is a movement of attention, not of body: his gaze leaves the key, travels to Cen's open palm, rests there long enough to register that the palm is not reaching, and then rises to her eyes. He interrupts one inhale halfway, swallows once, and releases a longer breath than the one he took. His left shoulder settles downward by a small visible amount, and the fingers of his left hand loosen on the key ring without letting go. His jaw stays tense until the breath finishes and only then eases, which is the first moment his face stops bracing against the room. Cen does not answer the movement with a movement of her own. She keeps her eyes on his rather than on the key, her shoulders stay level, and her open palm remains exactly where it was, close enough to receive and far enough to leave him room to decline. Her breath stays quiet, with one small inhale before she speaks. Nothing in her posture asks him to hurry. When Lu speaks, he speaks slowly in a low, slightly rough voice, with the admission landing before the offer: he says the previous refusal was his own, and then tells her to take it now. His left thumb slides off the key ring as the last clause ends, so the hand movement finishes after the words instead of anticipating them. Fabric shifts softly at his elbow, the brass key rings once against the desk, and the ventilation continues underneath. At the end of the shot the key is still in Lu's left hand but no longer gripped, his thumb is off the ring, the bandaged right wrist stays on the cloth, and Cen's palm is still open with nothing in it.",
  "camera": {
    "previs_id": "103",
    "lens_mm": 65,
    "sensor_basis": "full-frame equivalent",
    "shutter_angle": 180,
    "movement": "slow controlled push",
    "path": "twenty-centimeter slow push toward the shared desk plane",
    "target": "the visible action and contact plane",
    "adaptation": "project-specific amplitude and speed; source ID is a motion-family reference",
    "description": "The camera advances twenty centimeters in a medium close two-shot, keeping Lu's eyes, both shoulder lines and his left hand visible without a cut."
  },
  "characters": [
    {
      "id": "CHAR_LU",
      "position": [
        0.35,
        0.55
      ],
      "facing": "toward screen right",
      "gaze": "toward Cen He",
      "weapon_hand": "both hands visible and unarmed",
      "weapon_direction": "no weapon present in this scene"
    },
    {
      "id": "CHAR_CEN",
      "position": [
        0.7,
        0.55
      ],
      "facing": "toward screen left",
      "gaze": "toward Lu Chuan",
      "weapon_hand": "both hands visible and unarmed",
      "weapon_direction": "no weapon present in this scene"
    }
  ],
  "features": {
    "core_emotion": true,
    "combat": false,
    "supernatural_vfx": false,
    "colossal": false
  },
  "dialogues": [
    {
      "speaker_id": "S1",
      "speaker_name": "Lu Chuan",
      "language": "Chinese",
      "text": "上次是我没听。现在你来。",
      "delivery": "speaking slowly in a low, slightly rough voice",
      "start": 144,
      "end": 222,
      "voiceover": false
    }
  ],
  "audio": {
    "foley": [
      "Fabric shifts softly at the elbow and the brass key makes one small ring."
    ],
    "low_frequency_hz": null,
    "no_low_frequency_reason": "A quiet desk conversation has no designed bass event."
  },
  "outcome_events": [],
  "state_in": {
    "characters": {
      "CHAR_LU": {
        "ammo": 0,
        "trauma_phase": 1
      },
      "CHAR_CEN": {
        "ammo": 0,
        "trauma_phase": null
      }
    },
    "scenes": {
      "S01": 0
    },
    "props": {
      "BRASS_KEY": "CHAR_LU"
    }
  },
  "state_out": {
    "characters": {
      "CHAR_LU": {
        "ammo": 0,
        "trauma_phase": 1
      },
      "CHAR_CEN": {
        "ammo": 0,
        "trauma_phase": null
      }
    },
    "scenes": {
      "S01": 0
    },
    "props": {
      "BRASS_KEY": "CHAR_LU"
    }
  },
  "state_description": "Lu's bandaged right wrist is supported on the desk. The brass key is in his left hand; Cen's receiving palm is empty."
}
```

### FILM-S01-SH002｜10.000–20.000 秒

A medium-close view favors Cen on the right of the wooden desk, with Lu on the left, his hand at the desk edge and the key now resting across his open fingers. Cen leaves her open palm between them with enough distance for Lu to decline, and her eyes stay on his face. East-window light still lands on her hands and the near half of the desk, the west doorway stays unlit, and the brass hook on the rear wall keeps its position, so the room has not changed around them. The camera drifts ten centimeters toward Cen while retaining Lu's hand at the lower edge of frame; the desk and the window preserve the same spatial axis, and the move stops before the framing loses his fingers. Lu's hand moves first. He turns the key once between thumb and forefinger so the ring faces Cen, then pushes it across the wood with the flat of his fingers rather than dropping it, and withdraws his hand only after the key has left his skin. His shoulders stay dropped and his jaw stays loose through the transfer, and he keeps his eyes on the key until it reaches the center of her palm and then lifts them to her face. Cen holds eye contact without widening her eyes or looking down at the key, keeps her fingers open until the metal actually touches her palm, and closes them only after contact, one finger at a time, so the receiving hand does the emotional work instead of her face. Her shoulders relax once the key is closed, her neck stays straight, and her breath is quiet until she answers. She speaks softly with clear consonants, offering to open the door together rather than thanking him, which keeps the exchange practical. The brass key rings once as it settles in her palm and again, softer, when her fingers close; fabric shifts at both elbows; the ventilation and the distant rain continue without a break. At the end of the shot the key rests in Cen's closed hand, both mouths are closed after the line, Lu's left hand is empty and flat on the desk, and the room holds the same axis, light and furniture positions it started with.

```json
{
  "id": "FILM-S01-SH002",
  "scene_id": "S01",
  "start_frame": 240,
  "end_frame": 480,
  "visual": "A medium-close view favors Cen on the right of the wooden desk, with Lu on the left, his hand at the desk edge and the key now resting across his open fingers. Cen leaves her open palm between them with enough distance for Lu to decline, and her eyes stay on his face. East-window light still lands on her hands and the near half of the desk, the west doorway stays unlit, and the brass hook on the rear wall keeps its position, so the room has not changed around them. The camera drifts ten centimeters toward Cen while retaining Lu's hand at the lower edge of frame; the desk and the window preserve the same spatial axis, and the move stops before the framing loses his fingers. Lu's hand moves first. He turns the key once between thumb and forefinger so the ring faces Cen, then pushes it across the wood with the flat of his fingers rather than dropping it, and withdraws his hand only after the key has left his skin. His shoulders stay dropped and his jaw stays loose through the transfer, and he keeps his eyes on the key until it reaches the center of her palm and then lifts them to her face. Cen holds eye contact without widening her eyes or looking down at the key, keeps her fingers open until the metal actually touches her palm, and closes them only after contact, one finger at a time, so the receiving hand does the emotional work instead of her face. Her shoulders relax once the key is closed, her neck stays straight, and her breath is quiet until she answers. She speaks softly with clear consonants, offering to open the door together rather than thanking him, which keeps the exchange practical. The brass key rings once as it settles in her palm and again, softer, when her fingers close; fabric shifts at both elbows; the ventilation and the distant rain continue without a break. At the end of the shot the key rests in Cen's closed hand, both mouths are closed after the line, Lu's left hand is empty and flat on the desk, and the room holds the same axis, light and furniture positions it started with.",
  "camera": {
    "previs_id": "106",
    "lens_mm": 85,
    "sensor_basis": "full-frame equivalent",
    "shutter_angle": 180,
    "movement": "slow controlled lateral translation",
    "path": "ten-centimeter drift on the south side of the desk",
    "target": "the visible action and contact plane",
    "adaptation": "project-specific amplitude and speed; source ID is a motion-family reference",
    "description": "The camera drifts ten centimeters toward Cen while retaining Lu's hand at the lower edge; the desk and window preserve the same spatial axis."
  },
  "characters": [
    {
      "id": "CHAR_LU",
      "position": [
        0.35,
        0.55
      ],
      "facing": "toward screen right",
      "gaze": "toward Cen He",
      "weapon_hand": "both hands visible and unarmed",
      "weapon_direction": "no weapon present in this scene"
    },
    {
      "id": "CHAR_CEN",
      "position": [
        0.7,
        0.55
      ],
      "facing": "toward screen left",
      "gaze": "toward Lu Chuan",
      "weapon_hand": "both hands visible and unarmed",
      "weapon_direction": "no weapon present in this scene"
    }
  ],
  "features": {
    "core_emotion": true,
    "combat": false,
    "supernatural_vfx": false,
    "colossal": false
  },
  "dialogues": [
    {
      "speaker_id": "S2",
      "speaker_name": "Cen He",
      "language": "Chinese",
      "text": "那就一起把门打开。",
      "delivery": "speaking softly with clear consonants and an even pace",
      "start": 160,
      "end": 224,
      "voiceover": false
    }
  ],
  "audio": {
    "foley": [
      "Fabric shifts softly at the elbow and the brass key makes one small ring."
    ],
    "low_frequency_hz": null,
    "no_low_frequency_reason": "A quiet desk conversation has no designed bass event."
  },
  "outcome_events": [
    "EV_KEY"
  ],
  "state_in": {
    "characters": {
      "CHAR_LU": {
        "ammo": 0,
        "trauma_phase": 1
      },
      "CHAR_CEN": {
        "ammo": 0,
        "trauma_phase": null
      }
    },
    "scenes": {
      "S01": 0
    },
    "props": {
      "BRASS_KEY": "CHAR_LU"
    }
  },
  "state_out": {
    "characters": {
      "CHAR_LU": {
        "ammo": 0,
        "trauma_phase": 1
      },
      "CHAR_CEN": {
        "ammo": 0,
        "trauma_phase": null
      }
    },
    "scenes": {
      "S01": 0
    },
    "props": {
      "BRASS_KEY": "CHAR_CEN"
    }
  },
  "state_description": "Lu's bandaged right wrist is supported on the desk. The brass key is in his left hand; Cen's receiving palm is empty."
}
```

## GPT Image 2 / 2.5 可直接复制提示词

按主体、媒介、构图、光材、密度、受控细节、当前风险顺序编译。执行尺寸和采样设置留给实际出图入口。

参考图：不需要，可纯文字生成。

```text
Lu Chuan is a 34-year-old man, 1.80 meters tall, with balanced adult proportions, naturally broad shoulders, a square jaw, short dark hair and a short scar above his right eyebrow. He wears a gray woven work jacket over a gray shirt and a functional waist belt. Cen He is a 32-year-old woman, 1.70 meters tall, with a lean adult build, oval face, dark almond-shaped eyes and dark hair tied low behind her head. She wears an olive canvas coat over a cream work shirt and dark straight trousers. Create one live-action medium-close two-person keyframe in the maintenance room. Lu Chuan, an adult man with a short scar above his right eyebrow and a gray woven work jacket, sits on the left; his bandaged right wrist rests on the desk, and his left hand holds one brass key. Cen He, an adult woman with tied dark hair and an olive coat, sits on the right with an empty palm held between them. Capture the single moment before Lu releases the key. Use a 65 mm equivalent lens from the south side, showing eyes, shoulders and both hands together. One east window casts soft directional light across their cheek planes; a weak wall reflection leaves the shadow side readable. Skin has broad soft highlights, cloth folds retain fibrous edges only near the hands, and the brass key catches a narrow highlight. The rear wall and key hook remain quiet low-frequency shapes. Preserve identity, hand ownership, the bandage and the room geometry. Avoid waxy faces, extra hands and ghost texture.
```


## DRAMA_SEG01｜H3 T2VA 完整提示词

```text
integrated_multimodal_description:
Motion language: live_action at 24 fps, exposed on ones. Timing principle: let a small preparatory change precede the decisive hand action and hold the resulting state. Camera principle: keep the eye-line, receiving hand and prop contact readable before drifting closer. Staging principle: preserve the desk axis, left-right positions and the injured wrist limitation. Sound principle: keep room tone continuous and make each key contact a local foley event. Cut language: continuous.
This is a self-contained production instruction and must be readable without the production file, an earlier segment, or a hidden character bible. For every shot, explicitly state: the medium and visible subject appearance, screen position and facing; the current environment, landmarks and light direction; the exact starting pose, prop ownership, contact points and state; the factual trigger for each change; the chronological action, reaction and physical consequence; the camera framing, lens, movement type, direction, path, amplitude, speed and target; the source and timing of dialogue, foley, room tone and breath; the exact held state at the end and what can continue into the next shot. Render objective, social strategy and subtext as observable gaze, breath, posture, hand, facial and voice behavior. Keep cause and effect physically, spatially, temporally and socially coherent. Do not replace a visible action with a vague adjective, skip the transition between beats, collapse preparation, accent, follow-through or settle into one verb, or invent dialogue, objects, voices, cuts or state changes that are not written below.
[Shot 1] Live-action cinematic staging uses restrained facial movement and natural cloth response. Write this shot as a complete independent instruction: restate who is visible and where they are, the environment and light, the start state, the trigger, the ordered action and reaction, the camera path and speed, synchronized sound, and the resulting held state. Lu Chuan is a 34-year-old man, 1.80 meters tall, with balanced adult proportions, naturally broad shoulders, a square jaw, short dark hair and a short scar above his right eyebrow. He wears a gray woven work jacket over a gray shirt and a functional waist belt. Cen He is a 32-year-old woman, 1.70 meters tall, with a lean adult build, oval face, dark almond-shaped eyes and dark hair tied low behind her head. She wears an olive canvas coat over a cream work shirt and dark straight trousers. The maintenance room contains one wooden desk, an east-facing window, a west doorway and a brass-key hook on the rear dark wall. Soft east-window light crosses the desk and falls off toward the west wall. At the start of this shot: Lu's bandaged right wrist is supported on the desk. The brass key is in his left hand; Cen's receiving palm is empty. Lu Chuan, an adult men with a short scar over the right eyebrow and a gray work jacket, sits on the left side of the maintenance desk with his bandaged right wrist supported on a folded cloth and the brass key held in his left hand at the edge of the desk. Cen He, an adult technician with tied dark hair and a pale workshop coat, sits on the right with both forearms on the desk and her receiving palm open between them, empty, a hand's width from the key. The east window throws soft gray daylight across the desk from behind Cen's shoulder, so Lu's face carries the shadow side and Cen's hands stay lit; the brass key picks up one small highlight along its ring. The wooden desk, the window, the west doorway and the brass hook on the rear wall hold fixed positions, and the room's only sound is ventilation under distant rain. The camera advances twenty centimeters in a medium close two-shot, keeping Lu's eyes, both shoulder lines and his left hand visible without a cut, and it never crosses the desk edge. Framing holds Lu on the left and Cen on the right with the open palm between them. Nothing passes in front of the lens. Lu's first change is a movement of attention, not of body: his gaze leaves the key, travels to Cen's open palm, rests there long enough to register that the palm is not reaching, and then rises to her eyes. He interrupts one inhale halfway, swallows once, and releases a longer breath than the one he took. His left shoulder settles downward by a small visible amount, and the fingers of his left hand loosen on the key ring without letting go. His jaw stays tense until the breath finishes and only then eases, which is the first moment his face stops bracing against the room. Cen does not answer the movement with a movement of her own. She keeps her eyes on his rather than on the key, her shoulders stay level, and her open palm remains exactly where it was, close enough to receive and far enough to leave him room to decline. Her breath stays quiet, with one small inhale before she speaks. Nothing in her posture asks him to hurry. When Lu speaks, he speaks slowly in a low, slightly rough voice, with the admission landing before the offer: he says the previous refusal was his own, and then tells her to take it now. His left thumb slides off the key ring as the last clause ends, so the hand movement finishes after the words instead of anticipating them. Fabric shifts softly at his elbow, the brass key rings once against the desk, and the ventilation continues underneath. At the end of the shot the key is still in Lu's left hand but no longer gripped, his thumb is off the ring, the bandaged right wrist stays on the cloth, and Cen's palm is still open with nothing in it. The camera advances twenty centimeters in a medium close two-shot, keeping Lu's eyes, both shoulder lines and his left hand visible without a cut. The camera uses a 65 mm lens under the full-frame equivalent convention, with a 180-degree shutter-angle convention; movement: slow controlled push; path: twenty-centimeter slow push toward the shared desk plane; target: the visible action and contact plane. At shot entry, Lu Chuan has normalized screen anchor x=0.35, y=0.55 (left-to-right and top-to-bottom); facing toward screen right; gaze toward Cen He; hand or weapon state: both hands visible and unarmed; weapon direction or absence: no weapon present in this scene. At shot entry, Cen He has normalized screen anchor x=0.7, y=0.55 (left-to-right and top-to-bottom); facing toward screen left; gaze toward Lu Chuan; hand or weapon state: both hands visible and unarmed; weapon direction or absence: no weapon present in this scene. Fabric shifts softly at the elbow and the brass key makes one small ring. During 6.000–9.250 seconds within this shot, Lu Chuan (S1), speaking slowly in a low, slightly rough voice, says: <d>[Chinese] 上次是我没听。现在你来。</d> Keep every word intelligible: synchronize visible mouth shapes to the original words, preserve the written pauses and emphasis, and keep competing action noise below the voice unless the production data explicitly requires overlap. At the end of this shot, carry forward these recorded constraints: Lu Chuan remains in the stabilized or treated injury state; preserve the described functional limitations; the brass key remains with Lu Chuan.

overall_soundscape:
Quiet ventilation and distant rain remain under breathing, a sleeve brushing the desk and the small ring of a brass key.

non_diegetic_music:
N/A
```


## DRAMA_SEG02｜H3 T2VA 完整提示词

```text
integrated_multimodal_description:
Motion language: live_action at 24 fps, exposed on ones. Timing principle: let a small preparatory change precede the decisive hand action and hold the resulting state. Camera principle: keep the eye-line, receiving hand and prop contact readable before drifting closer. Staging principle: preserve the desk axis, left-right positions and the injured wrist limitation. Sound principle: keep room tone continuous and make each key contact a local foley event. Cut language: continuous.
This is a self-contained production instruction and must be readable without the production file, an earlier segment, or a hidden character bible. For every shot, explicitly state: the medium and visible subject appearance, screen position and facing; the current environment, landmarks and light direction; the exact starting pose, prop ownership, contact points and state; the factual trigger for each change; the chronological action, reaction and physical consequence; the camera framing, lens, movement type, direction, path, amplitude, speed and target; the source and timing of dialogue, foley, room tone and breath; the exact held state at the end and what can continue into the next shot. Render objective, social strategy and subtext as observable gaze, breath, posture, hand, facial and voice behavior. Keep cause and effect physically, spatially, temporally and socially coherent. Do not replace a visible action with a vague adjective, skip the transition between beats, collapse preparation, accent, follow-through or settle into one verb, or invent dialogue, objects, voices, cuts or state changes that are not written below.
[Shot 1] Live-action cinematic staging uses restrained facial movement and natural cloth response. Write this shot as a complete independent instruction: restate who is visible and where they are, the environment and light, the start state, the trigger, the ordered action and reaction, the camera path and speed, synchronized sound, and the resulting held state. Lu Chuan is a 34-year-old man, 1.80 meters tall, with balanced adult proportions, naturally broad shoulders, a square jaw, short dark hair and a short scar above his right eyebrow. He wears a gray woven work jacket over a gray shirt and a functional waist belt. Cen He is a 32-year-old woman, 1.70 meters tall, with a lean adult build, oval face, dark almond-shaped eyes and dark hair tied low behind her head. She wears an olive canvas coat over a cream work shirt and dark straight trousers. The maintenance room contains one wooden desk, an east-facing window, a west doorway and a brass-key hook on the rear dark wall. Soft east-window light crosses the desk and falls off toward the west wall. At the start of this shot: Lu's bandaged right wrist is supported on the desk. The brass key is in his left hand; Cen's receiving palm is empty. A medium-close view favors Cen on the right of the wooden desk, with Lu on the left, his hand at the desk edge and the key now resting across his open fingers. Cen leaves her open palm between them with enough distance for Lu to decline, and her eyes stay on his face. East-window light still lands on her hands and the near half of the desk, the west doorway stays unlit, and the brass hook on the rear wall keeps its position, so the room has not changed around them. The camera drifts ten centimeters toward Cen while retaining Lu's hand at the lower edge of frame; the desk and the window preserve the same spatial axis, and the move stops before the framing loses his fingers. Lu's hand moves first. He turns the key once between thumb and forefinger so the ring faces Cen, then pushes it across the wood with the flat of his fingers rather than dropping it, and withdraws his hand only after the key has left his skin. His shoulders stay dropped and his jaw stays loose through the transfer, and he keeps his eyes on the key until it reaches the center of her palm and then lifts them to her face. Cen holds eye contact without widening her eyes or looking down at the key, keeps her fingers open until the metal actually touches her palm, and closes them only after contact, one finger at a time, so the receiving hand does the emotional work instead of her face. Her shoulders relax once the key is closed, her neck stays straight, and her breath is quiet until she answers. She speaks softly with clear consonants, offering to open the door together rather than thanking him, which keeps the exchange practical. The brass key rings once as it settles in her palm and again, softer, when her fingers close; fabric shifts at both elbows; the ventilation and the distant rain continue without a break. At the end of the shot the key rests in Cen's closed hand, both mouths are closed after the line, Lu's left hand is empty and flat on the desk, and the room holds the same axis, light and furniture positions it started with. The camera drifts ten centimeters toward Cen while retaining Lu's hand at the lower edge; the desk and window preserve the same spatial axis. The camera uses a 85 mm lens under the full-frame equivalent convention, with a 180-degree shutter-angle convention; movement: slow controlled lateral translation; path: ten-centimeter drift on the south side of the desk; target: the visible action and contact plane. At shot entry, Lu Chuan has normalized screen anchor x=0.35, y=0.55 (left-to-right and top-to-bottom); facing toward screen right; gaze toward Cen He; hand or weapon state: both hands visible and unarmed; weapon direction or absence: no weapon present in this scene. At shot entry, Cen He has normalized screen anchor x=0.7, y=0.55 (left-to-right and top-to-bottom); facing toward screen left; gaze toward Lu Chuan; hand or weapon state: both hands visible and unarmed; weapon direction or absence: no weapon present in this scene. Fabric shifts softly at the elbow and the brass key makes one small ring. During 6.667–9.333 seconds within this shot, Cen He (S1), speaking softly with clear consonants and an even pace, says: <d>[Chinese] 那就一起把门打开。</d> Keep every word intelligible: synchronize visible mouth shapes to the original words, preserve the written pauses and emphasis, and keep competing action noise below the voice unless the production data explicitly requires overlap. At local shot time 00:07.917, the recorded state change is: Lu visibly places the brass key in Cen's open palm. At the end of this shot, carry forward these recorded constraints: Lu Chuan remains in the stabilized or treated injury state; preserve the described functional limitations; the brass key remains with Cen He.

overall_soundscape:
Quiet ventilation and distant rain remain under breathing, a sleeve brushing the desk and the small ring of a brass key.

non_diegetic_music:
N/A
```

## 场记末尾回写

```json
{
  "initial": {
    "characters": {
      "CHAR_LU": {
        "ammo": 0,
        "trauma_phase": 1
      },
      "CHAR_CEN": {
        "ammo": 0,
        "trauma_phase": null
      }
    },
    "scenes": {
      "S01": 0
    },
    "props": {
      "BRASS_KEY": "CHAR_LU"
    }
  },
  "events": [
    {
      "id": "EV_KEY",
      "frame": 430,
      "shot_id": "FILM-S01-SH002",
      "domain": "prop",
      "target": "BRASS_KEY",
      "before": "CHAR_LU",
      "after": "CHAR_CEN",
      "reason": "Lu visibly places the brass key in Cen's open palm."
    }
  ],
  "final": {
    "characters": {
      "CHAR_LU": {
        "ammo": 0,
        "trauma_phase": 1
      },
      "CHAR_CEN": {
        "ammo": 0,
        "trauma_phase": null
      }
    },
    "scenes": {
      "S01": 0
    },
    "props": {
      "BRASS_KEY": "CHAR_CEN"
    }
  }
}
```

## 结果验收

运行 audit_storyboard_quality.py 检查当前数据。实际生成后逐帧看身份、接触、主光、伤势和道具；音轨核对对白与频谱。未生成时视觉及声学实测保持 UNVERIFIED。
