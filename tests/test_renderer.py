import unittest
from types import NoneType
from src.renderer import Renderer
from src.board import Board
from src.deck import Deck
from src.card import Card


class TestAssembleHeader(unittest.TestCase):
    def setUp(self):
        d = Deck()
        b = Board()
        r = Renderer(b)

        b.deal(d, shuffle=False)
        self.header = r._assemble_header()


    def test_contents_are_correct_type(self):
        for row_i, row in enumerate(self.header):
            for item_i, item in enumerate(row):
                self.assertIsInstance(item, (Card, NoneType), f"Error in row{row_i} col{item_i}")


    def test_correct_number_rows(self):
        self.assertEqual(len(self.header), 4)            


    def test_correct_number_columns(self):
        for row in self.header:
            self.assertEqual(len(row), 7)


class TestAssembleTableau(unittest.TestCase):
    def setUp(self):
        d = Deck()
        b = Board()
        r = Renderer(b)

        b.deal(d, shuffle=False)
        self.board = b
        self.tableau = r._assemble_tableau()


    def test_contents_are_correct_type(self):
        for column in self.tableau:
            for item in column:
                self.assertIsInstance(item, (Card, NoneType))

    
    def test_correct_number_rows(self):
        for column in self.tableau:
            self.assertEqual(len(column), self.board.len_max_tableau)


    def test_correct_number_columns(self):
        self.assertEqual(len(self.tableau), 7)


class TestRenderer(unittest.TestCase):
    #TODO: Finish renderer tests
    def test_draw_header(self):
        pass


    def test_draw_tableau(self):
        pass


    def test_draw(self):
        pass



if __name__ == "__main__":
    unittest.main()