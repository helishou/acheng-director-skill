import copy
import unittest
from asset_plan import DEFAULT_CHARACTER_TURNAROUND_LAYOUT, DEFAULT_CHARACTER_VIEW_LAYOUT, prepare_asset_card


class CharacterLayoutTests(unittest.TestCase):
    def test_new_character_defaults_to_one_identity_image(self):
        card = prepare_asset_card({'id': 'Cuizi', 'asset_kind': 'character', 'prompt': 'Silk qipao.'}, {})
        for text in ('single-frame neutral full-body identity image', 'exactly one person', 'not a contact sheet', 'hands remain empty'):
            self.assertIn(text, card['prompt'])
        self.assertEqual(card['view_layout']['type'], 'single_character_identity_image')
        self.assertEqual(card['view_layout']['order'], 'single')
        self.assertNotIn('Top left:', card['prompt'])
        self.assertNotIn('nine tails', card['prompt'])
        self.assertEqual(prepare_asset_card(card, {})['prompt'], card['prompt'])

    def test_reject_conflicting_order_and_legacy_views(self):
        layout = copy.deepcopy(DEFAULT_CHARACTER_VIEW_LAYOUT)
        layout['order'] = 'left_to_right'
        with self.assertRaises(ValueError):
            prepare_asset_card({'id': 'x', 'asset_kind': 'character', 'view_layout': layout}, {})
        with self.assertRaises(ValueError):
            prepare_asset_card({'id': 'x', 'asset_kind': 'character', 'prompt': 'arranged left to right'}, {})

    def test_noncharacter_unchanged(self):
        card = {'id': 'snake', 'asset_kind': 'effect', 'prompt': 'Three snake views.'}
        self.assertEqual(prepare_asset_card(card, {}), card)

    def test_reject_equal_rows(self):
        layout = copy.deepcopy(DEFAULT_CHARACTER_TURNAROUND_LAYOUT)
        layout['selection'] = 'user_explicit'
        layout['selection_reason'] = 'The selected identity image is ready for a second-stage board.'
        layout['row_height_ratio'] = [1, 1]
        with self.assertRaises(ValueError):
            prepare_asset_card({'id': 'x', 'asset_kind': 'character', 'view_layout': layout}, {})


if __name__ == '__main__':
    unittest.main()
