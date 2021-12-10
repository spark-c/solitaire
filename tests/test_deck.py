import unittest
import collections
from src.deck import Deck
from src.card import Card

class TestDeck(unittest.TestCase):
    def test_has_52_cards(self):
        deck = Deck()
        self.assertEqual(deck.length, 52)


    def test_has_all_suits(self):
        deck = Deck()
        c = collections.Counter([card.suit for card in deck.contents])

        for suit in [Card.HEARTS, Card.SPADES, Card.DIAMONDS, Card.CLUBS]:
            self.assertEqual(c[suit], 13)


    def test_has_all_values(self):
        deck = Deck()
        c = collections.Counter([str(card.value) for card in deck.contents])

        for value in range(1, 14):
            self.assertEqual(c[str(value)], 4)


    def test_shuffle_deck(self):
        """ Checks that the first three cards are no longer in original order. Could rarely false-negative. """
        deck = Deck()
        deck.shuffle()
        self.assertNotEqual(deck.contents[:3], [Card(1, Card.HEARTS), Card(2, Card.HEARTS), Card(3, Card.HEARTS)])


    def test_pre_deal(self):
        """ Should be handing back a list with seven Stacks, i.e. the initial game columns """
        deck = Deck()
        output = deck.pre_deal()
        for i in range(7):
            self.assertEqual(output[i].length, i)


if __name__ == "__main__":
    unittest.main()