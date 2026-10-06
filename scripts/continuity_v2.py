"""Deterministic validation and replay for authored Canvas continuity ledgers.

This validates the structure and replay of facts the director registered. It
does not claim to discover facts omitted from natural-language source text.
"""
import hashlib
import json
import re
import sys


EVIDENCE = {"explicit_change", "explicit_hold", "inherited_fact", "not_applicable_with_rule", "unresolved_review"}
NOT_APPLICABLE_RULES = {"non_narrative_note", "transition_without_registered_fact", "dialogue_without_state_change"}


def digest(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _rows(value):
    return value if isinstance(value, list) else []


def audit(source, target_ids=None):
    """Return scope-labeled diagnostics and source-derived state trajectories."""
    ledger = source.get("ledger") if isinstance(source, dict) else None
    shots = _rows(source.get("shots"))
    segments = _rows(source.get("segments"))
    issues = []
    trajectories = {}
    full_shots = {str(row.get("id")): row for row in shots if row.get("id")}
    segment_by_shot = {}
    for segment in segments:
        sid = str(segment.get("id", ""))
        for shot_id in segment.get("shot_ids", []) if isinstance(segment.get("shot_ids"), list) else []:
            segment_by_shot.setdefault(str(shot_id), []).append(sid)

    def issue(code, message, shot_id=None, fact_id=None, path="source.ledger"):
        targets = segment_by_shot.get(str(shot_id), []) if shot_id else []
        if not targets and path.startswith("source.script_scenes."):
            scene_key = path.split(".")[2]
            scene_row = next((row for row in source_scenes if str(row.get("id", "")) == scene_key), {})
            scene_id = str(scene_row.get("scene_id", ""))
            source_scene_id = str(scene_row.get("id", ""))
            targets = sorted({segment for shot in shots if str(shot.get("scene_id", "")) == scene_id or str(shot.get("source_scene_id", "")) == source_scene_id
                              for segment in segment_by_shot.get(str(shot.get("id", "")), [])})
        issues.append({"code": code, "path": path, "message": message,
                       **({"targetId": str(shot_id)} if shot_id else {}),
                       **({"factId": str(fact_id)} if fact_id else {}),
                       "affectedTargets": targets})

    if not isinstance(ledger, dict) or ledger.get("contract_version") != 2:
        legacy_status = "unavailable"
        try:
            from audit_storyboard_quality import ContractError, replay
            replay(source)
            legacy_status = "structural_pass"
        except (ImportError, KeyError, TypeError, ValueError, ContractError) as error:
            legacy_status = "structural_blocked"
            issues.append({"code": "LEGACY_CONTINUITY_DIAGNOSTIC", "severity": "warning", "message": str(error)})
        return {"status": "diagnosticOnly", "coverageStatus": "not_assessed", "semanticDiscovery": "not_performed",
                "legacyReplay": legacy_status, "diagnostics": issues, "trajectories": {}, "factObjects": {}, "sourceDigest": digest(source),
                "limits": ["旧版结构重放结果仅供诊断，不评估剧本覆盖，不作为新版生产回执。"]}

    facts = {str(item.get("id")): item for item in _rows(ledger.get("facts")) if isinstance(item, dict) and item.get("id")}
    timelines = {str(item.get("id")): item for item in _rows(ledger.get("timelines")) if isinstance(item, dict) and item.get("id")}
    initial_rows = _rows(ledger.get("initial"))
    events = _rows(ledger.get("events"))
    requirements = _rows(ledger.get("requirements"))
    coverage = _rows(ledger.get("coverage"))
    source_scenes = _rows(source.get("script_scenes"))
    blocks = {}
    for scene in source_scenes:
        for block in _rows(scene.get("blocks")):
            if block.get("id"):
                blocks[str(block["id"])] = (scene, block)

    def unique(rows, label):
        seen = set()
        for row in rows:
            if not isinstance(row, dict) or not row.get("id"):
                issue("CONTINUITY_ID_REQUIRED", f"{label} 必须有稳定 ID")
                continue
            key = str(row["id"])
            if key in seen:
                issue("CONTINUITY_DUPLICATE_ID", f"{label} ID 重复：{key}")
            seen.add(key)
    for rows, label in ((ledger.get("facts"), "事实"), (ledger.get("timelines"), "时间线"), (events, "事件"), (requirements, "连续性要求"), (coverage, "覆盖证据")):
        unique(_rows(rows), label)

    registries = {
        "character": {str(x.get("id")) for x in _rows(source.get("character_registry")) if x.get("id")},
        "scene": {str(x.get("id")) for x in _rows(source.get("scene_registry")) if x.get("id")},
        "asset": {str(x.get("id") or x.get("asset_id")) for x in _rows(source.get("asset_plan")) if x.get("id") or x.get("asset_id")},
    }
    for fact_id, fact in facts.items():
        object_kind, object_id = fact.get("object_kind"), str(fact.get("object_id", ""))
        if object_kind not in registries or object_id not in registries.get(object_kind, set()):
            issue("CONTINUITY_UNKNOWN_OBJECT", f"事实 {fact_id} 引用了未登记对象 {object_kind}:{object_id}", fact_id=fact_id)
        allowed = fact.get("allowed_values")
        if not isinstance(allowed, list) or not allowed or any(not isinstance(x, str) or not x.strip() or x == "unknown" for x in allowed) or len(set(allowed)) != len(allowed):
            issue("CONTINUITY_ALLOWED_VALUES", f"事实 {fact_id} 必须声明不含 unknown 的唯一合法状态值", fact_id=fact_id)

    shot_order = {}
    for shot_id, shot in full_shots.items():
        timeline_id = str(shot.get("timeline_id", ""))
        order = shot.get("story_order")
        if timeline_id not in timelines or type(order) is not int or order < 0:
            issue("CONTINUITY_SHOT_TIMELINE", f"{shot_id} 必须绑定已登记时间线和非负 story_order", shot_id)
            continue
        key = (timeline_id, order)
        if key in shot_order:
            issue("CONTINUITY_DUPLICATE_STORY_ORDER", f"时间线 {timeline_id} 的 story_order {order} 重复", shot_id)
        shot_order[key] = shot_id

    initial = {}
    for row in initial_rows:
        if not isinstance(row, dict):
            issue("CONTINUITY_INITIAL_INVALID", "初态必须是对象")
            continue
        timeline_id, fact_id, value = str(row.get("timeline_id", "")), str(row.get("fact_id", "")), row.get("value")
        key = (timeline_id, fact_id)
        if timeline_id not in timelines or fact_id not in facts or not isinstance(value, str):
            issue("CONTINUITY_INITIAL_INVALID", f"初态引用无效对象/事实或状态：{timeline_id}/{fact_id}", fact_id=fact_id)
            continue
        allowed = facts[fact_id].get("allowed_values", [])
        if value != "unknown" and value not in allowed:
            issue("CONTINUITY_INITIAL_VALUE", f"初态值不在事实 {fact_id} 的合法状态中", fact_id=fact_id)
        if key in initial:
            issue("CONTINUITY_INITIAL_DUPLICATE", f"时间线 {timeline_id} 的事实 {fact_id} 有重复初态", fact_id=fact_id)
        initial[key] = value

    event_ids = set()
    ordered_events = {}
    for event in events:
        if not isinstance(event, dict):
            issue("CONTINUITY_EVENT_INVALID", "事件必须是对象")
            continue
        event_id = str(event.get("id", "")); timeline_id = str(event.get("timeline_id", "")); fact_id = str(event.get("fact_id", "")); shot_id = str(event.get("shot_id", ""))
        if not event_id or event_id in event_ids:
            issue("CONTINUITY_EVENT_ID", f"事件 ID 缺失或重复：{event_id}", shot_id, fact_id)
        event_ids.add(event_id)
        shot = full_shots.get(shot_id); frame = event.get("frame"); before = event.get("before"); after = event.get("after")
        if timeline_id not in timelines or fact_id not in facts or not shot or str(shot.get("timeline_id", "")) != timeline_id:
            issue("CONTINUITY_EVENT_REFERENCE", f"事件 {event_id} 引用未知时间线、事实或镜头", shot_id, fact_id)
            continue
        if type(frame) is not int or frame < int(shot.get("start_frame", 0)) or frame >= int(shot.get("end_frame", 0)):
            issue("CONTINUITY_EVENT_FRAME", f"事件 {event_id} 不在镜头播放帧窗内", shot_id, fact_id)
        allowed = facts[fact_id].get("allowed_values", [])
        if before != "unknown" and before not in allowed or after != "unknown" and after not in allowed:
            issue("CONTINUITY_EVENT_VALUE", f"事件 {event_id} 使用事实 {fact_id} 不支持的状态", shot_id, fact_id)
        anchor = event.get("source_anchor")
        if not isinstance(anchor, dict) or str(anchor.get("block_id", "")) not in blocks:
            issue("CONTINUITY_EVENT_SOURCE", f"事件 {event_id} 缺少有效剧本块来源", shot_id, fact_id)
        if len(str(event.get("reason", "")).strip()) < 8:
            issue("CONTINUITY_EVENT_REASON", f"事件 {event_id} 缺少具体原因", shot_id, fact_id)
        ordered_events.setdefault(timeline_id, []).append(event)

    req_by_shot_fact = {}
    for req in requirements:
        if not isinstance(req, dict):
            issue("CONTINUITY_REQUIREMENT_INVALID", "连续性要求必须是对象")
            continue
        shot_id, fact_id, timeline_id = str(req.get("shot_id", "")), str(req.get("fact_id", "")), str(req.get("timeline_id", ""))
        if shot_id not in full_shots or fact_id not in facts or str(full_shots.get(shot_id, {}).get("timeline_id", "")) != timeline_id:
            issue("CONTINUITY_REQUIREMENT_REFERENCE", "连续性要求引用无效镜头、事实或时间线", shot_id, fact_id)
            continue
        kind = req.get("kind")
        if kind not in {"change", "hold", "unresolved"}:
            issue("CONTINUITY_REQUIREMENT_KIND", "要求 kind 必须为 change/hold/unresolved", shot_id, fact_id)
        if kind == "change" and (not isinstance(req.get("event_ids"), list) or not req["event_ids"] or any(str(e) not in event_ids for e in req["event_ids"])):
            issue("CONTINUITY_CHANGE_EVENT_REQUIRED", "已声明变化必须关联登记事件", shot_id, fact_id)
        if kind == "hold" and (not isinstance(req.get("value"), str) or not req.get("value")):
            issue("CONTINUITY_HOLD_VALUE_REQUIRED", "保持要求必须声明当前状态值", shot_id, fact_id)
        if kind == "unresolved":
            issue("CONTINUITY_UNRESOLVED", str(req.get("reason") or "事实仍未解决"), shot_id, fact_id)
        req_by_shot_fact.setdefault((timeline_id, shot_id, fact_id), []).append(req)

    selected = set(target_ids or [])
    selected_shots = {str(shot_id) for segment in segments if not selected or str(segment.get("id", "")) in selected
                      for shot_id in segment.get("shot_ids", []) if str(shot_id) in full_shots}
    selected_scene_ids = {str(full_shots[shot_id].get("scene_id", "")) for shot_id in selected_shots}
    selected_source_scene_ids = {str(full_shots[shot_id].get("source_scene_id", "")) for shot_id in selected_shots}
    selected_script_scene_keys = {str(scene.get("id", "")) for scene in source_scenes if str(scene.get("scene_id", "")) in selected_scene_ids or str(scene.get("id", "")) in selected_source_scene_ids}
    expected_blocks = {block_id for block_id, (scene, _) in blocks.items() if not selected or str(scene.get("id", "")) in selected_script_scene_keys}
    covered_kinds = {}
    for row in coverage:
        if not isinstance(row, dict):
            issue("CONTINUITY_COVERAGE_INVALID", "覆盖证据必须是对象")
            continue
        anchor = row.get("source_anchor") if isinstance(row.get("source_anchor"), dict) else {}
        block_id = str(anchor.get("block_id", "")); evidence_kind = row.get("evidence_kind")
        if block_id not in blocks:
            issue("CONTINUITY_COVERAGE_SOURCE", f"覆盖证据引用未知剧本块 {block_id}")
            continue
        scene, block = blocks[block_id]
        current_digest = digest({"scene_id": scene.get("scene_id"), "block": block})
        if row.get("source_digest") != current_digest:
            issue("CONTINUITY_COVERAGE_STALE", f"覆盖证据 {block_id} 的原文已变化", path=f"source.script_scenes.{scene.get('id')}.blocks.{block_id}")
        kinds = covered_kinds.setdefault(block_id, set())
        if evidence_kind in kinds:
            issue("CONTINUITY_COVERAGE_DUPLICATE", f"剧本块 {block_id} 的 {evidence_kind} 覆盖重复")
        kinds.add(evidence_kind)
        if evidence_kind not in EVIDENCE:
            issue("CONTINUITY_EVIDENCE_KIND", f"剧本块 {block_id} 缺少有效覆盖证据类别")
            continue
        fact_ids = row.get("fact_ids") if isinstance(row.get("fact_ids"), list) else []
        event_refs = row.get("event_ids") if isinstance(row.get("event_ids"), list) else []
        shot_refs = row.get("shot_ids") if isinstance(row.get("shot_ids"), list) else []
        for shot_ref in shot_refs:
            if str(shot_ref) not in full_shots or str(full_shots[str(shot_ref)].get("timeline_id", "")) != str(row.get("timeline_id", "")):
                issue("CONTINUITY_COVERAGE_SHOT", f"剧本块 {block_id} 覆盖证据引用无效镜头 {shot_ref}")
        if any(str(value) not in facts for value in fact_ids) or any(str(value) not in event_ids for value in event_refs):
            issue("CONTINUITY_COVERAGE_REFERENCE", f"剧本块 {block_id} 覆盖证据引用未知事实或事件")
        if evidence_kind == "explicit_change" and (not fact_ids or not event_refs or not shot_refs):
            issue("CONTINUITY_COVERAGE_CHANGE_EMPTY", f"剧本块 {block_id} 的变化覆盖必须关联事实和事件")
        if evidence_kind == "explicit_change" and any(str(event.get("id")) in {str(x) for x in event_refs} and str(event.get("source_anchor", {}).get("block_id", "")) != block_id for event in events):
            issue("CONTINUITY_COVERAGE_EVENT_SOURCE", f"剧本块 {block_id} 变化覆盖引用的事件来源不匹配")
        if evidence_kind == "explicit_hold" and (not fact_ids or not shot_refs or any(not any(req.get("kind") == "hold" and str(req.get("value")) for req in req_by_shot_fact.get((str(row.get("timeline_id", "")), str(shot_id), str(fact_id)), [])) for fact_id in fact_ids for shot_id in shot_refs)):
            issue("CONTINUITY_COVERAGE_HOLD_EMPTY", f"剧本块 {block_id} 的保持覆盖缺少对应事实保持要求")
        if evidence_kind == "inherited_fact" and (not fact_ids or not shot_refs):
            issue("CONTINUITY_COVERAGE_INHERIT_EMPTY", f"剧本块 {block_id} 的继承覆盖必须引用事实")
        if evidence_kind == "not_applicable_with_rule" and (row.get("rule") not in NOT_APPLICABLE_RULES or len(str(row.get("reason", "")).strip()) < 8 or not str(row.get("review_ref", "")).strip() or not shot_refs):
            issue("CONTINUITY_COVERAGE_EXEMPTION", f"剧本块 {block_id} 的不适用判断需要受限规则、理由和复核引用")
        if evidence_kind == "unresolved_review":
            issue("CONTINUITY_COVERAGE_UNRESOLVED", f"剧本块 {block_id} 的覆盖仍未解决")
    for block_id in expected_blocks - set(covered_kinds):
        scene, _ = blocks[block_id]
        issue("CONTINUITY_COVERAGE_MISSING", f"剧本块 {block_id} 尚无连续性覆盖证据", path=f"source.script_scenes.{scene.get('id')}.blocks.{block_id}")
    for block_id, kinds in covered_kinds.items():
        if "not_applicable_with_rule" in kinds and len(kinds) > 1:
            issue("CONTINUITY_COVERAGE_EXEMPTION_CONFLICT", f"剧本块 {block_id} 同时标为不适用并登记了连续性事实")

    included_shots = set()
    for segment in segments:
        sid = str(segment.get("id", ""))
        if selected and sid not in selected:
            continue
        included_shots.update(str(value) for value in segment.get("shot_ids", []) if str(value) in full_shots)
    if not selected:
        included_shots = set(full_shots)

    final_by_timeline = {}
    for timeline_id, timeline in timelines.items():
        stream = sorted((shot for shot in shots if str(shot.get("timeline_id", "")) == timeline_id), key=lambda shot: (shot.get("story_order", -1), str(shot.get("id", ""))))
        values = {fact_id: value for (initial_timeline, fact_id), value in initial.items() if initial_timeline == timeline_id}
        relevant_facts = {fact_id for fact_id, fact in facts.items() if any(str(shot.get("id")) in included_shots and (str(fact.get("object_id")) in [str(x.get("id")) for x in shot.get("characters", []) if isinstance(x, dict)] or str(fact.get("object_id")) == str(shot.get("scene_id")) or fact_id in shot.get("continuity_facts", [])) for shot in stream)}
        same_frame = set()
        for shot in stream:
            shot_id = str(shot.get("id", "")); applies = shot_id in included_shots
            snapshot_in = dict(values)
            if applies:
                declared = {str(x) for x in shot.get("continuity_facts", []) if x}
                participant_ids = {str(x.get("id")) for x in shot.get("characters", []) if isinstance(x, dict) and x.get("id")}
                participant_ids.add(str(shot.get("scene_id", "")))
                participant_ids.update(str(x) for x in shot.get("required_assets", []) if x)
                participant_facts = {fact_id for fact_id, fact in facts.items() if str(fact.get("object_id")) in participant_ids}
                for fact_id in participant_facts | declared:
                    if (timeline_id, shot_id, fact_id) not in req_by_shot_fact:
                        issue("CONTINUITY_REQUIREMENT_MISSING", f"镜头参与对象的登记事实 {fact_id} 尚未声明保持、变化或未解决", shot_id, fact_id)
                local_relevant = {fact_id for fact_id, fact in facts.items() if str(fact.get("object_id")) in participant_ids or fact_id in declared}
                for fact_id in local_relevant:
                    if fact_id not in values or values[fact_id] == "unknown":
                        issue("CONTINUITY_BASELINE_UNKNOWN", f"镜头消费的事实 {fact_id} 没有已知初态", shot_id, fact_id)
                for fact_id in declared | participant_facts:
                    if fact_id not in values:
                        issue("CONTINUITY_BASELINE_MISSING", f"镜头事实 {fact_id} 缺少时间线初态", shot_id, fact_id)
            current_events = sorted((event for event in ordered_events.get(timeline_id, []) if str(event.get("shot_id")) == shot_id), key=lambda event: (event.get("frame", -1), str(event.get("id", ""))))
            for event in current_events:
                fact_id = str(event.get("fact_id", ""))
                event_key = (timeline_id, event.get("frame"), fact_id)
                if event_key in same_frame:
                    issue("CONTINUITY_DUPLICATE_FRAME_EVENT", f"同一帧同一事实 {fact_id} 不能重复变化", shot_id, fact_id)
                same_frame.add(event_key)
                prior = values.get(fact_id, "unknown")
                if prior != event.get("before"):
                    issue("CONTINUITY_BEFORE_MISMATCH", f"事件 {event.get('id')} 的 before 与重放状态不一致（期望 {prior}）", shot_id, fact_id)
                    values[fact_id] = "unknown"
                else:
                    values[fact_id] = event.get("after")
            if applies:
                trajectories[shot_id] = {"timelineId": timeline_id, "storyOrder": shot.get("story_order"), "start": snapshot_in, "end": dict(values), "eventIds": [str(event.get("id")) for event in current_events]}
                for fact_id, rows in req_by_shot_fact.items():
                    req_timeline, req_shot, req_fact = fact_id
                    if req_timeline != timeline_id or req_shot != shot_id:
                        continue
                    for req in rows:
                        if req.get("kind") == "hold" and snapshot_in.get(req_fact, "unknown") != req.get("value"):
                            issue("CONTINUITY_HOLD_MISMATCH", f"保持要求的事实 {req_fact} 与镜头起态不一致", shot_id, req_fact)
                        if req.get("kind") == "change" and not any(str(event.get("id")) in [str(x) for x in req.get("event_ids", [])] for event in current_events):
                            issue("CONTINUITY_CHANGE_EVENT_NOT_IN_SHOT", f"变化要求的事实 {req_fact} 没有本镜事件", shot_id, req_fact)
        final_by_timeline[timeline_id] = dict(values)

    scoped_issues = [item for item in issues if not selected or not item.get("affectedTargets") or selected.intersection(item.get("affectedTargets", []))]
    # Source-wide coverage diagnostics block any target because no target can claim
    # a complete review while a screenplay block remains unreviewed or stale.
    status = "blocked" if scoped_issues else "passed"
    coverage_status = "incomplete" if any(item["code"].startswith("CONTINUITY_COVERAGE") for item in scoped_issues) else "registered"
    return {"status": status, "coverageStatus": coverage_status, "semanticDiscovery": "not_performed",
            "sourceDigest": digest(source), "validatorVersion": "2.0.0", "diagnostics": scoped_issues,
            "trajectories": trajectories, "final": final_by_timeline,
            "factObjects": {fact_id: {"kind": fact.get("object_kind"), "id": fact.get("object_id")} for fact_id, fact in facts.items()},
            "limits": ["只核验结构化登记事实与覆盖证据；未登记在自然语言中的事实不会被自动发现。"]}


def contract():
    return {"contract_version": 2, "evidence_kinds": sorted(EVIDENCE), "not_applicable_rules": sorted(NOT_APPLICABLE_RULES),
            "fact": {"required": ["id", "object_kind", "object_id", "allowed_values"]},
            "timeline": {"required": ["id"]},
            "shot": {"required": ["timeline_id", "story_order"]},
            "event": {"required": ["id", "timeline_id", "fact_id", "shot_id", "frame", "before", "after", "reason", "source_anchor.block_id"]},
            "coverage": {"required": ["id", "source_anchor.block_id", "source_digest", "evidence_kind", "fact_ids", "event_ids"]}}


if __name__ == "__main__":
    request = json.load(sys.stdin)
    result = contract() if request.get("action") == "contract" else audit(request.get("source", {}), request.get("target_ids"))
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
