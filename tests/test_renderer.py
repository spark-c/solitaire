import os
from unittest import TestCase, main, mock
import contextlib
from io import StringIO
from types import NoneType
from src.renderer import Renderer
from src.board import Board
from src.deck import Deck
from src.card import Card
from src.userinterface import UserInterface


class TestAssembleHeader(TestCase):
    def setUp(self):
        d = Deck()
        b = Board()
        r = Renderer(b)

        b.deal(d, shuffle=False)
        self.header = r._assemble_header() #type: ignore


    def test_contents_are_correct_type(self):
        for row_i, row in enumerate(self.header):
            for item_i, item in enumerate(row):
                self.assertIsInstance(item, (Card, NoneType), f"Error in row{row_i} col{item_i}")


    def test_correct_number_rows(self):
        self.assertEqual(len(self.header), 4)            


    def test_correct_number_columns(self):
        for row in self.header:
            self.assertEqual(len(row), 7)


class TestAssembleTableau(TestCase):
    def setUp(self):
        d = Deck()
        b = Board()
        r = Renderer(b)

        b.deal(d, shuffle=False)
        self.board = b
        self.tableau = r._assemble_tableau() #type: ignore


    def test_contents_are_correct_type(self):
        for column in self.tableau:
            for item in column:
                self.assertIsInstance(item, (Card, NoneType))

    
    def test_correct_number_rows(self):
        for column in self.tableau:
            self.assertEqual(len(column), self.board.len_max_tableau)


    def test_correct_number_columns(self):
        self.assertEqual(len(self.tableau), 7)


class TestRenderer(TestCase):
    #TODO: Finish renderer tests
    def setUp(self):
        self.b = Board()
        self.ui = UserInterface(self.b)
        self.r = Renderer(self.b, self.ui)
        self.f = StringIO()


    # def test_i_did_stdout_correctly(self):
    #     f = StringIO()
    #     with contextlib.redirect_stdout(f):
    #         print("helloworld", end="")
    #         self.assertEqual(f.getvalue(), "helloworld")


    def test_draw_header(self):
        pass


    def test_draw_tableau(self):
        pass


    def test_draw(self):
        pass


    def test_no_err_msg_without_err(self):
        """ Ensures that self.err render is empty if there is no err """
        with contextlib.redirect_stdout(self.f):
            self.r._draw_err() #type: ignore       
                
        self.assertEqual(self.f.getvalue(), "\n")


    @mock.patch.dict(os.environ, {"GAME_LOGIC": "False"})
    def test_no_err_msg_without_err_after_move(self):
        """ Same as previous, except makes a move first """
        d = Deck()
        b = Board()
        b.deal(d)
        ui = UserInterface(b)
        r = Renderer(b, ui)
        with contextlib.redirect_stdout(self.f):
            ui.main_loop(manual_input="121")
            r._draw_err() #type: ignore

        self.assertEqual(self.f.getvalue(), "\n")


    def test_renders_userinput_err(self):
        """ Ensures self.err is printed if there is an err """
        with contextlib.redirect_stdout(self.f):
            self.ui._get_input(manual_input="this errs") #type: ignore
            self.ui.current_input.is_valid
            self.r._draw_err() #type: ignore

        self.assertNotIn(self.f.getvalue(), ["", "\n"])


if __name__ == "__main__":
    main()