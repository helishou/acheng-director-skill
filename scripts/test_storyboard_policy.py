import copy
import unittest
from pathlib import Path
from storyboard_policy import diagnostics, check, render
from audit_storyboard_quality import read_data, compile_segment, shot_text


def fixture():
    return {"storyboard_policy": {"version": 1}, "character_registry": [{"id": "A", "name": "Alice"}, {"id": "B", "name": "Bob"}],
            "shots": [{"id": "Q", "start_frame": 0, "end_frame": 48, "camera": {"framing": "CU", "attention_subject_ids": ["A"], "editorial_reason": "Her question changes the strategy"}, "characters": [{"id": "A"}, {"id": "B"}], "visual": "Alice asks, Bob listens.", "dialogues": [{"character_id": "A", "text": "Why?"}]},
                      {"id": "R", "start_frame": 48, "end_frame": 120, "camera": {"framing": "CU", "attention_subject_ids": ["B"], "editorial_reason": "Hold on his hesitant response"}, "characters": [{"id": "B"}], "visual": "Bob hesitates before answering.", "dialogues": [{"character_id": "B", "text": "Wait."}]}],
            "segments": [{"id": "S", "start_frame": 0, "end_frame": 120, "shot_ids": ["Q", "R"]}]}


class StoryboardPolicyTests(unittest.TestCase):
    def test_reverse_shots_and_short_shot(self):
        self.assertEqual(diagnostics(fixture()), [])
        self.assertIn("close-up", render(fixture()["shots"][0], fixture()))
        self.assertIn("Alice", render(fixture()["shots"][0], fixture()))

    def test_required_fields_and_objects(self):
        for field in ("framing", "attention_subject_ids", "editorial_reason"):
            p = fixture(); del p["shots"][0]["camera"][field]
            with self.assertRaisesRegex(ValueError, "shots.0.camera"):
                check(p)
        p = fixture(); p["shots"][0]["camera"]["attention_subject_ids"] = ["unknown"]
        self.assertTrue(any(d["code"] == "STORYBOARD_ATTENTION_INVALID" for d in diagnostics(p)))

    def test_gap_overlap_and_scope(self):
        for start in (47, 49):
            p = fixture(); p["shots"][1]["start_frame"] = start
            with self.assertRaisesRegex(ValueError, "FRAME_CLOSURE"):
                check(p)
        p = fixture(); p["shots"].append({"id": "OLD"})
        check(p, {"Q", "R"})
        with self.assertRaises(ValueError): check(p)

    def test_legacy_and_unknown_version(self):
        p = fixture(); del p["storyboard_policy"]
        p["shots"][0]["camera"] = {}
        self.assertEqual(diagnostics(p), [])
        for version in (True, 2, "1"):
            p["storyboard_policy"] = {"version": version}
            with self.assertRaises(ValueError): check(p)

    def test_warnings_do_not_block_or_rewrite(self):
        p = fixture(); p["shots"][0]["camera"]["framing"] = "MS"
        p["shots"][0]["dialogues"].append({"character_id": "B", "text": "Wait."})
        before = copy.deepcopy(p); check(p)
        self.assertEqual(p, before)
        self.assertEqual({d["code"] for d in diagnostics(p)}, {"DIALOGUE_WIDE_COVERAGE", "DIALOGUE_ATTENTION_REVIEW"})

    def test_listener_offscreen_voice_narration_and_silence(self):
        p = fixture(); p["shots"][1]["dialogues"] = [{"character_id": "A", "text": "Listen.", "voiceover": False}]
        check(p)  # Actor speech can continue over a listener close-up.
        p["shots"][0]["camera"]["framing"] = "MS"
        p["shots"][0]["dialogues"][0]["voiceover"] = True
        p["shots"][1]["dialogues"] = []
        self.assertEqual(diagnostics(p), [])

    def test_prose_conflicts(self):
        p = fixture(); p["shots"][0]["visual"] = "A medium two-shot; cut to Bob."
        self.assertEqual({d["code"] for d in diagnostics(p)}, {"FRAMING_PROSE_CONFLICT", "EDITORIAL_CUT_IN_PROSE"})

    def test_invalid_framing_type_returns_diagnostic(self):
        p = fixture(); p['shots'][0]['camera']['framing'] = []
        self.assertTrue(any(d['code'] == 'STORYBOARD_FRAMING_REQUIRED' for d in diagnostics(p)))

    def test_real_compiler_preserves_local_shots_and_speech(self):
        p = read_data(Path(__file__).resolve().parents[1] / "examples/02-drama.production.json")
        p["storyboard_policy"] = {"version": 1}
        for s in p["shots"]:
            s["camera"].update(framing="CU", attention_subject_ids=[s["characters"][0]["id"]], editorial_reason="Read the actor's changing strategy and response")
        for segment in p["segments"]:
            text = compile_segment(p, segment)
            for n, sid in enumerate(segment["shot_ids"], 1):
                self.assertIn(f"[Shot {n}]", text)
                shot = next(s for s in p["shots"] if s["id"] == sid)
                self.assertIn("Framing: close-up", text)
                for line in shot["dialogues"]:
                    self.assertIn(f'<d>[{line["language"]}] {line["text"]}</d>', text)


if __name__ == "__main__": unittest.main()
