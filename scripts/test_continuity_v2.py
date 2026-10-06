"""Contract tests for registered-state replay, not semantic fact discovery."""
import unittest

from continuity_v2 import audit, digest


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
                          "source_digest": digest({"scene_id": "ROOM", "block": scene["blocks"][0]}),
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
        self.assertIn("CONTINUITY_COVERAGE_STALE", {item["code"] for item in result["diagnostics"]})

    def test_bad_before_state_blocks_the_consumer_segment(self):
        value = production()
        value["ledger"]["events"] = [{"id": "EV01", "timeline_id": "main", "fact_id": "F_COAT", "shot_id": "SH01",
                                       "frame": 12, "before": "red", "after": "blue", "reason": "Restore blue coat",
                                       "source_anchor": {"block_id": "B01"}}]
        result = audit(value)
        diagnostic = next(item for item in result["diagnostics"] if item["code"] == "CONTINUITY_BEFORE_MISMATCH")
        self.assertEqual(diagnostic["affectedTargets"], ["SEG01"])

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


if __name__ == "__main__":
    unittest.main()
