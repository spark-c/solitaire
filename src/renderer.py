from typing import List, Any
from src.card import Card, MsgCard


class Renderer:

    def __init__(self):
        pass


    def _assemble_header(self, board) -> None:
        stock: List[Card|None] = board.stock.peek_from_top(last=3)
        waste: List[Card|None] = board.waste.peek_from_top(last=3)
        foundations: List[Card|None] = list()
        for f in board.foundations:
            found_card: Card|None = f.peek_from_top()[0]
            if found_card is None:
                foundations.append(MsgCard(content="[Ace] "))
            else:
                foundations.append(found_card)

        header: List[List[Card|str]] = [
            # stock0, waste0, 5spaces
            [
                stock[0],
                waste[0],
                board.SPACE,
                board.SPACE,
                board.SPACE,
                board.SPACE,
                board.SPACE
            ],

            # stock1, waste1, 1spaces, 4found
            [
                stock[1],
                waste[1],
                board.SPACE,
                foundations[0],
                foundations[1],
                foundations[2],
                foundations[3]
            ],

            # stock2, waste2, 5spaces
            [
                stock[2],
                waste[2],
                board.SPACE,
                board.SPACE,
                board.SPACE,
                board.SPACE,
                board.SPACE
            ],

            # 7spaces
            [board.SPACE for _ in range(7)]
        ]

        return header


    def _assemble_tableau(self, board) -> None:
        pass


    def _draw_header(self, board) -> None:
        header = self._assemble_header(board)
        for row in header:
            for card in row:
                if card is not None:
                    print(str(card), end=board.SEP)
                else:
                    print(board.SPACE, end=board.SEP)

            print("\n", end="")


    def _draw_tableau(self) -> None:
        pass


    def draw(self, board) -> None:
        header: List[List[Card|None]] = self._assemble_header()
        tableau: List[List[Card|None]] = self._assemble_tableau()

        self._draw_header(header)
        self._draw_tableau(tableau)


        """
        draw0
            stock
            tab0
        draw1
            waste
            tab1
        draw2
            tab2
        draw3
            tab3
            found0
        draw4
            tab4
            found1
        draw5
            tab5
            found2
        draw6
            tab6
            found3
        """

        """
        1. Find longest tableau
        2. Grid should be 7 wide x len(tableau) + 4
        Row0: stock0 waste0 5spaces
        Row1: stock1 waste1 1spaces found0 found1 found2 found3
        Row2: stock2 waste2 5spaces
        Row3: 7spaces
        """

        """
        < ?? > | < SS > |
        < ?? > | < SS > |        | < SS > | < SS > | < SS > | < SS > |
        < ?? > | < SS > |

        < SS > | < SS > | < SS > | < SS > | < SS > | < SS > | < SS > |
        """