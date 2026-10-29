"""Explicit editorial structure; warnings are not aesthetic verdicts."""
import re

FRAMINGS = {"EWS": "extreme wide shot", "WS": "wide shot", "FS": "full shot", "MS": "medium shot", "MCU": "medium close-up", "CU": "close-up", "ECU": "extreme close-up"}


def rows(value):
    return value if isinstance(value, list) else []


def diagnostics(source, shot_ids=None):
    policy = source.get("storyboard_policy")
    if policy is None:
        return []
    result = []
    def issue(code, path, message, target=None, severity="error"):
        result.append({"code": code, "path": "director.source." + path, "message": message, "severity": severity, **({"targetId": target} if target else {})})
    if not isinstance(policy, dict) or type(policy.get("version")) is not int or policy["version"] != 1:
        issue("STORYBOARD_POLICY_VERSION", "storyboard_policy.version", "Supported storyboard policy version is 1")
        return result
    registered = {item.get("entity_id") or item.get("asset_id") or item.get("id") for field in ("character_registry", "scene_registry", "asset_plan", "asset_cards") for item in rows(source.get(field)) if isinstance(item, dict)}
    registered.discard(None)
    shots = [s for s in rows(source.get("shots")) if isinstance(s, dict)]
    selected = [s for s in shots if shot_ids is None or s.get("id") in shot_ids]
    by_id = {s.get("id"): s for s in shots}
    for shot in selected:
        index = shots.index(shot)
        sid = shot.get("id")
        path = f"shots.{index}"
        camera = shot.get("camera") if isinstance(shot.get("camera"), dict) else {}
        if not isinstance(camera.get("framing"), str) or camera["framing"] not in FRAMINGS:
            issue("STORYBOARD_FRAMING_REQUIRED", path + ".camera.framing", "Declare framing: " + ", ".join(FRAMINGS), sid)
        attention = camera.get("attention_subject_ids")
        if not isinstance(attention, list) or not attention or any(not isinstance(x, str) or x not in registered for x in attention):
            issue("STORYBOARD_ATTENTION_INVALID", path + ".camera.attention_subject_ids", "Declare a nonempty list of registered attention subjects", sid)
        reason = camera.get("editorial_reason")
        if not isinstance(reason, str) or len(reason.strip()) < 3 or re.fullmatch(r"TBD|TODO|unknown|待填|示例|N/A|\.+|…", reason.strip(), re.I):
            issue("STORYBOARD_EDITORIAL_REASON_REQUIRED", path + ".camera.editorial_reason", "Explain why this shot cuts in or holds and what information/reaction it carries", sid)
        spoken = [d for d in rows(shot.get("dialogues")) if isinstance(d, dict) and not d.get("voiceover")]
        if spoken and camera.get("framing") in ("EWS", "WS", "FS", "MS") and len(rows(shot.get("characters"))) > 1:
            issue("DIALOGUE_WIDE_COVERAGE", path + ".camera.framing", "Review whether shared framing makes the speaking/listening reactions readable", sid, "warning")
        if len({d.get("character_id") or d.get("speaker_id") for d in spoken}) > 1:
            issue("DIALOGUE_ATTENTION_REVIEW", path + ".camera.attention_subject_ids", "Multiple speakers share one shot; review attention changes and the reason for holding", sid, "warning")
        visual = str(shot.get("visual", ""))
        if re.search(r"\b(?:hard[- ]cut|cut to|reverse angle|cut once)\b|切到|反打|切镜", visual, re.I):
            issue("EDITORIAL_CUT_IN_PROSE", path + ".visual", "A change of editorial viewpoint must be an independent Shot with its own frame window", sid, "warning")
        if camera.get("framing") in ("CU", "ECU") and re.search(r"\b(?:medium two-shot|medium three-shot|wide shot|full shot)\b", visual, re.I):
            issue("FRAMING_PROSE_CONFLICT", path + ".visual", "Declared close-up conflicts with wider framing in visual prose", sid, "warning")
    for i, segment in enumerate(rows(source.get("segments"))):
        if not isinstance(segment, dict):
            continue
        ids = rows(segment.get("shot_ids"))
        if shot_ids is not None and not set(ids).intersection(shot_ids):
            continue
        covered = [by_id.get(sid) for sid in ids]
        if not covered or any(s is None for s in covered):
            issue("STORYBOARD_SHOT_COVERAGE", f"segments.{i}.shot_ids", "Segment requires registered shots", segment.get("id"))
            continue
        cursor = segment.get("start_frame")
        for shot in covered:
            start, end = shot.get("start_frame"), shot.get("end_frame")
            if type(start) is not int or type(end) is not int or start != cursor or end <= start:
                issue("STORYBOARD_FRAME_CLOSURE", f"shots.{shots.index(shot)}.start_frame", "Shot windows must cover their Segment in order without gaps or overlaps", shot.get("id"))
            cursor = end
        if cursor != segment.get("end_frame"):
            issue("STORYBOARD_FRAME_CLOSURE", f"segments.{i}.end_frame", "Shot coverage does not close at Segment end", segment.get("id"))
    return result


def check(source, shot_ids=None):
    errors = [d for d in diagnostics(source, shot_ids) if d["severity"] == "error"]
    if errors:
        raise ValueError("; ".join(f"{d['code']} {d['path']}: {d['message']}" for d in errors))


def render(shot, source):
    if source.get("storyboard_policy") is None and not shot.get("camera", {}).get("framing"):
        return ""
    camera = shot["camera"]
    if not isinstance(camera.get("framing"), str) or camera["framing"] not in FRAMINGS or not isinstance(camera.get("attention_subject_ids"), list) or not isinstance(camera.get("editorial_reason"), str):
        return ""  # Incomplete draft retains authored prose; strict compilation rejects it.
    names = {}
    for field in ("character_registry", "scene_registry", "asset_plan", "asset_cards"):
        for item in rows(source.get(field)):
            identifier = item.get("entity_id") or item.get("asset_id") or item.get("id")
            name = (source.get("prompt_bindings") or {}).get(identifier) or item.get("name") or item.get("asset_name")
            if name:
                names.setdefault(identifier, name)
    subjects = [names.get(sid, "the declared reference subject") for sid in camera["attention_subject_ids"]]
    scoped_labels = {subject.get('entity_id'): subject.get('label') for segment in rows(source.get('segments')) if shot['id'] in rows(segment.get('shot_ids')) for subject in rows(segment.get('subjects')) if shot['id'] in rows(subject.get('shot_ids'))}
    subjects = [scoped_labels.get(sid, names.get(sid, "the declared reference subject")) for sid in camera["attention_subject_ids"]]
    return f"Framing: {FRAMINGS[camera['framing']]}. Primary attention: {', '.join(subjects)}. Editorial purpose: {camera['editorial_reason']}."
