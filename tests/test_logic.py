import os
from unittest import TestCase, mock
from src.board import Board
from src.card import Card
from src.deck import Deck
from src.userinterface import UserInterface


@mock.patch.dict(os.environ, {"GAME_LOGIC": "True"})
class TestLogic(TestCase):

    def setUp(self):
        deck = Deck()
        self.board = Board()
        self.ui = UserInterface(self.board)
        self.board.deal(deck)


    def test_cannot_move_hidden_cards(self):
        b: Board = self.board
        for card in b.tableau[6]:
            card.hide()
        target: int = len(b.tableau[6])
        self.ui._get_input( #type: ignore
            manual_input="121"
        )
        self.ui._enact() #type: ignore

        self.assertEqual(len(b.tableau[6]), target)


    def test_cannot_repeat_color(self):
        b: Board = Board()
        b.tableau[0].add_cards([Card(10, Card.SPADES)])
        b.tableau[1].add_cards([Card(9, Card.CLUBS)])

        self.ui._get_input( #type: ignore
            manual_input="121"
        )
        self.ui._enact() #type: ignore

        self.assertEqual(len(b.tableau[0]), 1)
        

    def test_get_err_on_repeat_suits(self):
        pass


    def test_can_place_king_on_empty_tableau_value(self):
        b = Board()
        ui = UserInterface(b)
        king = Card(13, Card.CLUBS, _visible=True)
        b.tableau[0].add_cards([king])

        ui._get_input(manual_input="121") #type: ignore
        ui._enact() #type: ignore
                
        self.assertEqual(b.tableau[0].length, 0)


    def test_can_place_king_on_empty_tableau_suit(self):
        b = Board()
        ui = UserInterface(b)
        king = Card(13, Card.HEARTS, _visible=True)
        b.tableau[0].add_cards([king])

        ui._get_input(manual_input="121") #type: ignore
        ui._enact() #type: ignore
                
        self.assertEqual(b.tableau[0].length, 0)