#type: ignore
import unittest
from src.stack import Stack
from src.card import Card, NoneCard


class TestStack(unittest.TestCase):

    def test_starts_empty(self):
        s = Stack()
        self.assertEqual(s.contents, list())


    def test_add_card_to_top_of_stack(self):
        s = Stack()
        ace_hearts = Stack(input=[Card(1, Card.HEARTS)])
        three_spades = Stack(input=[Card(3, Card.SPADES)])

        s.add_cards(ace_hearts.contents)
        s.add_cards(three_spades.contents)

        self.assertEqual(s.contents[-1], three_spades.contents[0])


    def test_add_card_to_bottom_of_stack(self):
        s = Stack()        
        ace_hearts = Stack(input=[Card(1, Card.HEARTS)])
        three_spades = Stack(input=[Card(3, Card.SPADES)])


        s.add_cards(ace_hearts.contents)
        s.add_cards(three_spades.contents, to="bottom")

        self.assertEqual(s.contents[0], three_spades.contents[0])


    def test_pop_from_top(self):
        s = Stack(
            input=[
                Card(1, Card.HEARTS),
                Card(3, Card.SPADES),
                Card(5, Card.DIAMONDS)
            ]
        )
        new_stack = s.pop_from_top(last=2)
        self.assertEqual(s.length, 1)
        self.assertEqual(new_stack.contents, [Card(3, Card.SPADES), Card(5, Card.DIAMONDS)])


    def test_pop_from_bottom(self):
        s = Stack(
            input=[
                Card(1, Card.HEARTS),
                Card(3, Card.SPADES),
                Card(5, Card.DIAMONDS)
            ]
        )
        new_stack = s.pop_from_bottom(first=2)
        self.assertEqual(s.length, 1)
        self.assertEqual(new_stack.contents, [Card(1, Card.HEARTS), Card(3, Card.SPADES)])


    def test_peek_from_top_with_enough_cards(self):
        s = Stack(
            input=[
                Card(1, Card.HEARTS),
                Card(3, Card.SPADES),
                Card(5, Card.DIAMONDS),
                Card(7, Card.CLUBS)                
            ]
        )
        result: List[Card] = s.peek_from_top(last=3)

        self.assertEqual(result, [Card(3, Card.SPADES), Card(5, Card.DIAMONDS), Card(7, Card.CLUBS)])


    def test_peek_from_top_with_insufficient_cards(self):
        s = Stack(
            input=[
                Card(1, Card.HEARTS),
                Card(3, Card.SPADES),             
            ]
        )
        result: List[Card] = s.peek_from_top(last=3)

        self.assertEqual(result, [NoneCard(), Card(1, Card.HEARTS), Card(3, Card.SPADES)])


    def test_peek_from_top_with_no_cards(self):
        s = Stack(
        )
        result: List[Card] = s.peek_from_top(last=3)

        self.assertEqual(result, [NoneCard(), NoneCard(), NoneCard()])


    def test_peek_from_bottom_with_enough_cards(self):
        s = Stack(
            input=[
                Card(1, Card.HEARTS),
                Card(3, Card.SPADES),
                Card(5, Card.DIAMONDS),
                Card(7, Card.CLUBS)                
            ]
        )
        result: List[Card] = s.peek_from_bottom(first=3)

        self.assertEqual(result, [Card(1, Card.HEARTS), Card(3, Card.SPADES), Card(5, Card.DIAMONDS)])


    def test_peek_from_bottom_with_insufficient_cards(self):
        s = Stack(
            input=[
                Card(1, Card.HEARTS),
                Card(3, Card.SPADES),             
            ]
        )
        result: List[Card] = s.peek_from_bottom(first=3)

        self.assertEqual(result, [Card(1, Card.HEARTS), Card(3, Card.SPADES), NoneCard()])

    
    def test_peek_from_bottom_with_no_cards(self):
        s = Stack()
        result: List[Card] = s.peek_from_bottom(first=3)

        self.assertEqual(result, [NoneCard(), NoneCard(), NoneCard()])


if __name__ == "__main__":
    unittest.main()