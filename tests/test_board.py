import unittest
from src.board import Board
from src.stack import Stack
from src.deck import Deck


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
        # TODO: Complete this test after implememnting move() abstraction
        
        # deck = Deck()
        # board = Board()
        # board.deal(deck)

        # self.waste.add_cards(self.stock.pop_from_top(len(self.stock)))

    
    def test_cycle_stock_with_none_values(self):
        """ After stock only had one or two cards to flip into waste """
        pass
        


if __name__ == "__main__":
    unittest.main()