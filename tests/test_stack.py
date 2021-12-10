import unittest
from src.stack import Stack
from src.card import Card


class TestStack(unittest.TestCase):

    def test_starts_empty(self):
        s = Stack()
        self.assertEqual(s.contents, list())


    def test_add_card_to_top_of_stack(self):
        s = Stack()
        ace_hearts = Stack(input=[Card(1, "hearts")])
        three_spades = Stack(input=[Card(3, "spades")])

        s.add_cards(ace_hearts.contents)
        s.add_cards(three_spades.contents)

        self.assertEqual(s.contents[-1], three_spades.contents[0])


    def test_add_card_to_bottom_of_stack(self):
        s = Stack()        
        ace_hearts = Stack(input=[Card(1, "hearts")])
        three_spades = Stack(input=[Card(3, "spades")])


        s.add_cards(ace_hearts.contents)
        s.add_cards(three_spades.contents, to="bottom")

        self.assertEqual(s.contents[0], three_spades.contents[0])



if __name__ == "__main__":
    unittest.main()