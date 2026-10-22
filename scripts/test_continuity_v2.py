"""Contract tests for registered-state replay, not semantic fact discovery."""
import unittest

from continuity_v2 import audit, coverage_digest, legacy_coverage_digest


def production():
    scene = {"id": "SC01", "scene_id": "ROOM", "blocks": [{"id": "B01", "kind": "action", "text": "A remains in the blue coat."}]}
    shot = {"id": "SH01", "scene_id": "ROOM", "characters": [{"id": "A"}], "required_assets": [],
            "start_frame": 0, "end_frame": 24, "timeline_id": "main", "story_order": 0,
            "continuity_facts": ["F_COAT"]}
    return {
        "character_registry": [{"id": "A"}], "scene_registry": [{"id": "ROOM"}], "asset_plan": [],
        "script_scenes": [scene], "shots": [shot], "segments": [{"id": "SEG01", "shot_ids": ["SH01"]}],
        "ledger": {
            "contract_version": 2,
            "facts": [{"id": "F_COAT", "object_kind": "character", "object_id": "A", "allowed_values": ["blue", "red"]}],
            "timelines": [{"id": "main"}],
            "initial": [{"timeline_id": "main", "fact_id": "F_COAT", "value": "blue"}],
            "events": [],
            "requirements": [{"id": "R_HOLD", "timeline_id": "main", "shot_id": "SH01", "fact_id": "F_COAT", "kind": "hold", "value": "blue"}],
            "coverage": [{"id": "C_B01", "timeline_id": "main", "source_anchor": {"block_id": "B01"},
                          "source_digest": coverage_digest(scene, scene["blocks"][0]),
                          "evidence_kind": "explicit_hold", "fact_ids": ["F_COAT"], "event_ids": [], "shot_ids": ["SH01"]}],
        },
    }


class ContinuityV2Tests(unittest.TestCase):
    def test_no_event_is_valid_only_with_explicit_hold_and_source_coverage(self):
        result = audit(production())
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["semanticDiscovery"], "not_performed")
        self.assertEqual(result["trajectories"]["SH01"]["start"]["F_COAT"], "blue")

    def test_empty_events_without_coverage_do_not_pass(self):
        value = production()
        value["ledger"]["coverage"] = []
        result = audit(value)
        self.assertEqual(result["status"], "blocked")
        self.assertIn("CONTINUITY_COVERAGE_MISSING", {item["code"] for item in result["diagnostics"]})

    def test_changed_source_makes_coverage_stale(self):
        value = production()
        value["script_scenes"][0]["blocks"][0]["text"] = "A changes to the red coat."
        result = audit(value)
        diagnostic = next(item for item in result["diagnostics"] if item["code"] == "CONTINUITY_COVERAGE_STALE")
        self.assertEqual(diagnostic["coverageRowId"], "C_B01")
        self.assertEqual(diagnostic["blockId"], "B01")
        self.assertEqual(diagnostic["evidenceKind"], "explicit_hold")

    def test_multiple_stale_rows_for_one_block_are_individually_addressable(self):
        value = production()
        source = value["ledger"]["coverage"][0]
        value["ledger"]["coverage"].append({**source, "id": "C_B01_INHERITED", "evidence_kind": "inherited_fact", "fact_ids": ["F_COAT"]})
        value["script_scenes"][0]["blocks"][0]["text"] = "A changes to the red coat."
        result = audit(value)
        stale = [item for item in result["diagnostics"] if item["code"] == "CONTINUITY_COVERAGE_STALE"]
        self.assertEqual({item["coverageRowId"] for item in stale}, {"C_B01", "C_B01_INHERITED"})
        self.assertTrue(all(item["blockId"] == "B01" for item in stale))

    def test_bad_before_state_blocks_the_consumer_segment(self):
        value = production()
        value["ledger"]["events"] = [{"id": "EV01", "timeline_id": "main", "fact_id": "F_COAT", "shot_id": "SH01",
                                       "frame": 12, "before": "red", "after": "blue", "reason": "Restore blue coat",
                                       "source_anchor": {"block_id": "B01"}}]
        result = audit(value)
        diagnostic = next(item for item in result["diagnostics"] if item["code"] == "CONTINUITY_BEFORE_MISMATCH")
        self.assertEqual(diagnostic["affectedTargets"], ["SEG01"])
        self.assertEqual(diagnostic["expected"], "blue")
        self.assertEqual(diagnostic["actual"], "red")
        self.assertEqual(diagnostic["sourceBlockId"], "B01")

    def test_unknown_timeline_state_blocks_consumers(self):
        value = production()
        value["ledger"]["initial"][0]["value"] = "unknown"
        result = audit(value)
        self.assertTrue(any(item["code"] == "CONTINUITY_BASELINE_UNKNOWN" for item in result["diagnostics"]))

    def test_unrelated_later_segment_does_not_enter_selected_scope(self):
        value = production()
        value["shots"].append({"id": "SH02", "scene_id": "ROOM", "characters": [{"id": "A"}], "required_assets": [],
                               "start_frame": 24, "end_frame": 48, "timeline_id": "main", "story_order": 1,
                               "continuity_facts": ["F_COAT"]})
        value["segments"].append({"id": "SEG02", "shot_ids": ["SH02"]})
        result = audit(value, ["SEG01"])
        self.assertFalse(any(item.get("affectedTargets") == ["SEG02"] for item in result["diagnostics"]))

    def test_replays_are_idempotent(self):
        value = production()
        self.assertEqual(audit(value), audit(value))

    def test_display_fields_and_line_endings_do_not_stale_coverage(self):
        value = production()
        scene = value["script_scenes"][0]
        block = scene["blocks"][0]
        edited = {**block, "display_summary": "readable copy", "note": "layout scratch",
                  "text": "\r\nA remains in the blue coat.  \r\n"}
        self.assertEqual(coverage_digest(scene, edited), coverage_digest(scene, block))
        self.assertNotEqual(legacy_coverage_digest(scene, edited), legacy_coverage_digest(scene, block))
        scene["blocks"][0] = edited
        self.assertEqual(audit(value)["status"], "passed")

    def test_legacy_digest_keeps_existing_coverage_valid(self):
        value = production()
        scene = value["script_scenes"][0]
        value["ledger"]["coverage"][0]["source_digest"] = legacy_coverage_digest(scene, scene["blocks"][0])
        self.assertEqual(audit(value)["status"], "passed")

    def test_requirement_edit_keeps_coverage_digests_and_scope(self):
        value = production()
        scene = value["script_scenes"][0]
        before = [coverage_digest(scene, scene["blocks"][0])]
        value["ledger"]["requirements"][0]["value"] = "red"
        result = audit(value, ["SEG01"])
        self.assertEqual(before, [coverage_digest(scene, scene["blocks"][0])])
        self.assertTrue(any(item["code"] == "CONTINUITY_HOLD_MISMATCH" for item in result["diagnostics"]))
        self.assertTrue(all(item.get("affectedTargets", []) in ([], ["SEG01"]) for item in result["diagnostics"]))


if __name__ == "__main__":
    unittest.main()
