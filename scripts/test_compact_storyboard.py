import copy
import unittest
from pathlib import Path
from audit_storyboard_quality import read_data, compile_segment, shot_text
from reference_bindings import shot_reference_text

class CompactStoryboardTests(unittest.TestCase):
    def test_reference_definitions_not_repeated_and_retain_scoped_labels(self):
        p = read_data(Path(__file__).resolve().parents[1] / 'examples/02-drama.production.json')
        p.pop('prompt_detail_policy', None)
        shot = p['shots'][0]
        segment = {'start_frame': shot['start_frame'], 'shot_ids': [shot['id']], 'references': [{'label': '<Picture 1>', 'shot_ids': [shot['id']], 'source_only': True, 'preserve': 'face only', 'exclude': 'source pose'}], 'subjects': [{'label': '<Subject 1>', 'shot_ids': [shot['id']], 'definition': 'Identity from <Picture 1>'}]}
        seen = set()
        first = shot_reference_text(segment, shot, p, seen=seen)
        second = shot_reference_text(segment, shot, p, seen=seen)
        self.assertEqual(second, '')
        self.assertTrue(first)
        self.assertIn('<Subject 1>', first)
        self.assertNotIn('Identity from', first)

    def test_voiceover_does_not_require_onscreen_speaker_mouth(self):
        p = read_data(Path(__file__).resolve().parents[1] / 'examples/02-drama.production.json')
        p.pop('prompt_detail_policy', None)
        shot = copy.deepcopy(p['shots'][0])
        shot['dialogues'][0]['voiceover'] = True
        text = shot_text(shot, p)
        self.assertIn('speaker remains offscreen', text)
        self.assertNotIn("corresponding on-screen character's lips", text)
