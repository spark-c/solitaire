import unittest
from colorama import init, deinit, Fore, Style
from src.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        init(autoreset=True)


    def tearDown(self):
        deinit()


    def test_card_has_value(self):
        card = Card(value=1, suit=Card.HEARTS)
        self.assertEqual(card.value, 1)


    def test_card_has_suit(self):
        card = Card(value=1, suit=Card.HEARTS)
        self.assertEqual(card.suit, Card.HEARTS)

    
    def test_color_red(self):
        card = Card(value=1, suit=Card.HEARTS)
        self.assertEqual(card.color, Fore.RED)


    def test_color_black(self):
        card = Card(value=3, suit=Card.SPADES)
        self.assertEqual(card.color, Fore.WHITE)

    
    def test_starts_not_visible(self):
        card = Card(value=1, suit=Card.HEARTS)
        self.assertFalse(card.visible)


    def test_reveal_card_hidden_card(self):
        card = Card(value=1, suit=Card.HEARTS)
        card.reveal()
        self.assertTrue(card.visible)


    def test_hide_visible_card(self):
        card = Card(value=1, suit=Card.HEARTS, _visible=True)
        card.hide()
        self.assertFalse(card.visible)

    
    def test_card_string_with_face_value(self):
        card = Card(value=1, suit=Card.HEARTS, _visible=True)
        self.assertEqual(
            card.__str__(),
            f"< A {Fore.RED}{Card.HEARTS}{Style.RESET_ALL} >"
        )

    
    def test_card_string_without_face_value(self):
        card = Card(value=3, suit=Card.SPADES, _visible=True)
        self.assertEqual(
            card.__str__(),
            f"< 3 {Fore.WHITE}{Card.SPADES}{Style.RESET_ALL} >"
        )


    def test_card_string_for_10(self):
        card = Card(value=10, suit=Card.SPADES, _visible=True)
        self.assertEqual(
            card.__str__(),
            f"< 10{Fore.WHITE}{Card.SPADES}{Style.RESET_ALL} >"
        )

    
    def test_card_string_without_visible(self):
        card = Card(value=3, suit=Card.SPADES)
        self.assertEqual(card.__str__(), "< ??? >")



if __name__ == "__main__":
    unittest.main()
