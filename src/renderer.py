from typing import List, Any
from src.card import Card, MsgCard


class Renderer:

    def __init__(self):
        pass


    def _assemble_header(self, board) -> List[List[Card|None]]:
        """
        Pulls in all cards from the board that will need to be drawn,
        and arranges them according to the structure of the header.

        Returns List[List[Card|None]].
        Each List[Card|None] represents one row of text in the console.
        None indicates no card in that spot.
        """
        
        stock: List[Card|None] = board.stock.peek_from_top(last=3)
        waste: List[Card|None] = board.waste.peek_from_top(last=3)
        foundations: List[Card|None] = list()
        for f in board.foundations:
            found_card: Card|None = f.peek_from_top()[0]
            if found_card is None:
                foundations.append(MsgCard(content=board.EMPTY_ACE))
            else:
                foundations.append(found_card)

        header: List[List[Card|None]] = [
            # stock0, waste0, 5spaces
            [
                stock[0],
                waste[0],
                None,
                None,
                None,
                None,
                None
            ],

            # stock1, waste1, 1spaces, 4found
            [
                stock[1],
                waste[1],
                None,
                foundations[0],
                foundations[1],
                foundations[2],
                foundations[3]
            ],

            # stock2, waste2, 5spaces
            [
                stock[2],
                waste[2],
                None,
                None,
                None,
                None,
                None
            ],

            # 7spaces
            [None for _ in range(7)]
        ]

        return header


    def _assemble_tableau(self, board) -> List[List[Card|None]]:
        """
        Pulls in all cards from the board that will need to be drawn,
        and arranges them according to the structure of the tableau.

        Returns List[List[Card|None]].
        Each List[Card|None] represents one row of text in the console.
        None indicates no card in that spot.
        """
        pass


    def _draw_header(self, board) -> None:
        """ Receives cards and their placement in the header, and translates that into ASCII text. """

        header = self._assemble_header(board)
        for row in header:
            for card in row:
                if card is not None:
                    print(str(card), end=board.SEP)
                else:
                    print(board.SPACE, end=board.SEP)

            print("\n", end="")


    def _draw_tableau(self) -> None:
        """ Receives cards and their placement in the tableau, and translates that into ASCII text. """
        pass


    def draw(self, board) -> None:
        """ One method to call them all, and to the console draw them. """

        header: List[List[Card|None]] = self._assemble_header(board)
        tableau: List[List[Card|None]] = self._assemble_tableau(board)

        self._draw_header(header)
        self._draw_tableau(tableau)

        """
        1. Find longest tableau
        2. Grid should be 7 wide x len(tableau) + 4
        """

        """
        < ?? > | < SS > |
        < ?? > | < SS > |        | < SS > | < SS > | < SS > | < SS > |
        < ?? > | < SS > |

        < SS > | < SS > | < SS > | < SS > | < SS > | < SS > | < SS > |
        """