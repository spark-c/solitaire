import unittest
from src.board import Board
from src.deck import Deck
from src.renderer import Renderer
from src.userinterface import UserInterface


class TestCommands(unittest.TestCase):
    def setUp(self) -> None:
        d = Deck()
        self.b = Board()
        self.b.deal(d)
        self.ui = UserInterface(self.b)


    def test_move_with_3chars(self):
        input_string = "121"
        self.ui.main_loop(manual_input=input_string)
        
        self.assertEqual(len(self.b.tableau[1]), 3)


    def test_move_with_2chars(self):
        input_string = "12"
        self.ui.main_loop(manual_input=input_string)
        
        self.assertEqual(len(self.b.tableau[1]), 3)


    def test_reveal_top_card_in_stack(self):
        """ Entering just the selector for a stack should reveal its top card """
        input_string = "2"
        self.b.tableau[1].pop_from_top()
        self.assertFalse(self.b.tableau[1][-1]._visible)

        self.ui.main_loop(manual_input=input_string)

        self.assertTrue(self.b.tableau[1][-1]._visible)