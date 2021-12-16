import unittest
from src.board import Board
from src.stack import Stack
from src.deck import Deck
from src.card import Card


class TestBoard(unittest.TestCase):
    
    def test_create_all_fields(self):
        b = Board()
        self.assertIsInstance(b.foundations[3], Stack)
        self.assertIsInstance(b.tableau[6], Stack)
        self.assertIsInstance(b.stock, Stack)
        self.assertIsInstance(b.waste, Stack)

    
    def test_len_max_tableau(self):
        b = Board()
        d = Deck()
        b.deal(d)

        self.assertEqual(b.len_max_tableau, 7)

    
    def test_deal_correctly(self):
        deck = Deck()
        board = Board()
        board.deal(deck)

        self.assertEqual(board.tableau[0].length, 1)
        self.assertEqual(board.tableau[6].length, 7)
        self.assertEqual(board.stock.length, 24)


    def test_last_card_revealed(self):
        deck = Deck()
        board = Board()
        board.deal(deck)

        self.assertTrue(board.tableau[-1][-1]._visible)

    
class TestMoveCards(unittest.TestCase):

    def test_move(self):
        b = Board()
        b.tableau[0].add_cards([Card(value=10, suit=Card.HEARTS, _visible=True)])
        b.tableau[1].add_cards(
            [
                Card(value=10, suit=Card.DIAMONDS, _visible=True),
                Card(value=9, suit=Card.SPADES, _visible=True),
                Card(value=8, suit=Card.HEARTS, _visible=True)                
            ]
        )

        b.move_cards(b.tableau[1], b.tableau[0], 2)

        self.assertEqual(
            b.tableau[0].contents,
            [
                Card(value=10, suit=Card.HEARTS, _visible=True),
                Card(value=9, suit=Card.SPADES, _visible=True),
                Card(value=8, suit=Card.HEARTS, _visible=True) 
            ]
        )

    
    def test_move_all(self):
        b = Board()
        b.tableau[0].add_cards([Card(value=11, suit=Card.SPADES, _visible=True)])
        b.tableau[1].add_cards(
            [
                Card(value=10, suit=Card.DIAMONDS, _visible=True),
                Card(value=9, suit=Card.SPADES, _visible=True),
                Card(value=8, suit=Card.HEARTS, _visible=True)                
            ]
        )

        b.move_cards(b.tableau[1], b.tableau[0], 0)

        self.assertEqual(
            b.tableau[0].contents,
            [
                Card(value=11, suit=Card.SPADES, _visible=True),
                Card(value=10, suit=Card.DIAMONDS, _visible=True),
                Card(value=9, suit=Card.SPADES, _visible=True),
                Card(value=8, suit=Card.HEARTS, _visible=True)                
            ]
        )


class TestStockAndWaste(unittest.TestCase):

    def test_flip_stock(self):
        deck = Deck()
        board = Board()
        board.deal(deck)

        board.flip_stock()
        self.assertEqual(len(board.waste), 3, "Sufficient cards not moved to waste")
        self.assertTrue(board.waste[-1]._visible, "Waste card not visible")


    def test_flip_stock_with_less_than_three_cards(self):
        deck = Deck()
        board = Board()
        board.deal(deck)
        board.stock = board.stock.pop_from_top(2)

        board.flip_stock()
        # there are only two cards in stock but it should add a None, so len==3
        self.assertEqual(len(board.waste), 3)
        self.assertIsNone(board.waste[-1])


    def test_cycle_stock_with_no_none(self):
        """ After stock emptied with a full three cards into waste """        
        deck = Deck()
        board = Board()
        board.deal(deck)
        top_card = board.stock[-1]
        board.move_cards(board.stock, board.waste, 0)

        board.cycle_stock()

        self.assertEqual(len(board.waste), 0)
        self.assertEqual(len(board.stock), 24)
        self.assertEqual(board.stock[-1], top_card)

    
    def test_cycle_stock_with_none_values(self):
        """ After stock only had one or two cards to flip into waste """
        deck = Deck()
        board = Board()
        board.deal(deck)
        bottom_card = board.stock[0]
        board.stock.pop_from_top(2)
        board.move_cards(board.stock, board.waste, 0)

        board.cycle_stock()

        self.assertEqual(len(board.waste), 0)
        self.assertEqual(len(board.stock), 22)
        self.assertEqual(board.stock[0], bottom_card)
        


if __name__ == "__main__":
    unittest.main()