import os
from typing import List, Any
from src.config import Config
from src.card import Card, MsgCard


class Renderer:

    def __init__(self, board):
        self.board = board


    def _assemble_header(self) -> List[List[Card|None]]:
        """
        Pulls in all cards from the board that will need to be drawn,
        and arranges them according to the structure of the header.

        Returns List[List[Card|None]].
        Each List[Card|None] represents one row of text in the console.
        None indicates no card in that spot.
        """
        board = self.board

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
                MsgCard(content="   8   "),
                MsgCard(content="   9   "),
                MsgCard(content="   0   "),
                MsgCard(content="   -   ")
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
            # TODO: Remove this. To be replaced with something in draw() method.
            [None for _ in range(7)]
        ]

        return header


    def _assemble_tableau(self) -> List[List[Card|None]]:
        """
        Pulls in all cards from the board that will need to be drawn,
        and arranges them according to the structure of the tableau.

        Returns List[List[Card|None]].
        Each List[Card|None] represents one row of text in the console.
        None indicates no card in that spot.
        """
        board = self.board
        tableau: List[List[Card|None]] = list()
        # creating seven columns
        for _ in range(7):
            tableau.append(list())

        for i, column in enumerate(tableau):
            column.extend(board.tableau[i])
            while len(column) < board.len_max_tableau:
                column.append(None)

        return tableau



    def _draw_header(self) -> None:
        """ Receives cards and their placement in the header, and translates that into ASCII text. """
        board = self.board
        header = self._assemble_header()
        for row in header:
            print(board.SEP, end="")
            for card in row:
                if card is not None:
                    print(str(card), end=board.SEP)
                else:
                    print(board.SPACE, end=board.SEP)

            print("\n", end="")


    def _draw_tableau(self) -> None:
        """ Receives cards and their placement in the tableau, and translates that into ASCII text. """
        board = self.board
        tableau = self._assemble_tableau()
        for row_i in range(board.len_max_tableau):
            print(board.SEP, end="")
            for column in tableau:
                card = column[row_i]
                if card is not None:
                    print(str(card), end=board.SEP)
                else:
                    print(board.SPACE, end=board.SEP)
        
            print("\n", end="")

        self._draw_section_separator(char=" ")

        for i, column in enumerate(tableau): # column numbers for controls reference
            print(board.SEP, f"   {i + 1}   ", sep="", end="")
        print(board.SEP)
        
    
    def _draw_section_separator(self, char="-"):
        board = self.board

        print(board.SEP, end="")
        for _ in range(7):
            print(board.CARD_WIDTH * char, end="")
            print(board.SEP, end="")
        print("\n", end="")


    def _draw_controls(self) -> None:
        board = self.board
        t_legend: str = "".join([
            Config.KEYMAP["tableau0"],
            Config.KEYMAP["tableau1"],
            Config.KEYMAP["tableau2"],
            Config.KEYMAP["tableau3"],
            Config.KEYMAP["tableau4"],
            Config.KEYMAP["tableau5"],
            Config.KEYMAP["tableau6"],
        ])
        w_legend: str = "".join([
            Config.KEYMAP["foundations0"],
            Config.KEYMAP["foundations1"],
            Config.KEYMAP["foundations2"],
            Config.KEYMAP["foundations3"],
        ])

        print(
            f"Select waste with {Config.KEYMAP['waste']}",
            f"Select tableau with {t_legend}",
            f"Select foundations with {w_legend}",
            sep="\t"
        )
        print(
            f"Flip stock: {Config.KEYMAP['flip_stock']}",
            "Move card with 'src dest [amt=1]'",
            sep="\t"
        )


    def draw(self) -> None:
        """ One method to call them all, and to the console draw them. """
        board = self.board

        os.system("cls||clear") # clears terminal
        self._draw_section_separator()
        self._draw_header()
        self._draw_section_separator()
        self._draw_tableau()
        self._draw_section_separator()
        self._draw_controls()
