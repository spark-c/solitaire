import unittest
import collections
from src.deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck_has_52_cards(self):
        deck = Deck()
        self.assertEqual(deck.length, 52)


    def test_deck_has_all_suits(self):
        deck = Deck()
        c = collections.Counter([card.suit for card in deck.all_cards])

        for suit in ["hearts", "spades", "diamonds", "clubs"]:
            self.assertEqual(c[suit], 13)


    def test_deck_has_all_values(self):
        deck = Deck()
        c = collections.Counter([str(card.value) for card in deck.all_cards])

        for value in range(1, 14):
            self.assertEqual(c[str(value)], 4)



if __name__ == "__main__":
    unittest.main()