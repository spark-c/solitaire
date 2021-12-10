import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def test_card_has_value(self):
        card = Card(value=1, suit="hearts")
        self.assertEqual(card.value, 1)


    def test_card_has_suit(self):
        card = Card(value=1, suit="hearts")
        self.assertEqual(card.suit, "hearts")


if __name__ == "__main__":
    unittest.main()
