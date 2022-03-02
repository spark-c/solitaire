import os
from unittest import TestCase, mock
from src.board import Board
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

