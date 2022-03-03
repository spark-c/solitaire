from colorama import Fore
import os
from unittest import TestCase, mock
from src.board import Board
from src.card import Card, MsgCard
from src.deck import Deck


@mock.patch.dict(os.environ, {"GAME_LOGIC": "True"})
class TestLogic(TestCase):

    def setUp(self):
        deck = Deck()
        self.board = Board()
        self.board.deal(deck)


    def test_cannot_move_hidden_cards(self):
        b: Board = self.board
        for card in b.tableau[6]:
            card.hide()
        target: int = len(b.tableau[6])
        b.move_cards(b.tableau[6], b.tableau[0], -1)

        self.assertEqual(len(b.tableau[6]), target)


    def test_cannot_repeat_color(self):
        b: Board = Board()
        b.tableau[0].add_cards([Card(10, Card.SPADES)])
        b.tableau[0].add_cards([Card(9, Card.CLUBS)])
        self.assertEqual(len(b.tableau[0]), 1)
        

    def test_get_err_on_repeat_suits(self):
        pass
