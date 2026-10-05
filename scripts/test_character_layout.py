import copy
import unittest
from asset_plan import DEFAULT_CHARACTER_VIEW_LAYOUT, prepare_asset_card


class CharacterLayoutTests(unittest.TestCase):
    def test_fixed_panels_and_no_foreign_traits(self):
        card = prepare_asset_card({'id': 'Cuizi', 'asset_kind': 'character', 'prompt': 'Silk qipao.'}, {})
        for text in ('Top left:', 'Top right:', 'Bottom left:', 'Bottom right:', 'completely crop out head and face', 'orthographic'):
            self.assertIn(text, card['prompt'])
        self.assertNotIn('arranged left to right', card['prompt'])
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


if __name__ == '__main__':
    unittest.main()
