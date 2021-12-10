import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def test_card_has_value(self):
        card = Card(value=1, suit="hearts")
        self.assertEqual(card.value, 1)


    def test_card_has_suit(self):
        card = Card(value=1, suit="hearts")
        self.assertEqual(card.suit, "hearts")

    
    def test_starts_not_visible(self):
        card = Card(value=1, suit="hearts")
        self.assertFalse(card.visible)


    def test_reveal_card_hidden_card(self):
        card = Card(value=1, suit="hearts")
        card.reveal()
        self.assertTrue(card.visible)


    def test_hide_visible_card(self):
        card = Card(value=1, suit="hearts", _visible=True)
        card.hide()
        self.assertFalse(card.visible)



if __name__ == "__main__":
    unittest.main()
