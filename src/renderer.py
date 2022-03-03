import os
from typing import List, Optional
from src.config import Config
from src.card import Card, MsgCard, NoneCard
from src.board import Board
from src.userinterface import UserInterface


class Renderer:

    def __init__(self, board:Board, ui:Optional[UserInterface]=None) -> None:
        self.board: Board = board
        self.ui: UserInterface = ui if ui else UserInterface(board)


    def _assemble_header(self) -> List[List[Card]]:
        """
        Pulls in all cards from the board that will need to be drawn,
        and arranges them according to the structure of the header.

        Returns List[List[Card]].
        Each List[Card] represents one row of text in the console.
        None indicates no card in that spot.
        """
        board: Board = self.board

        stock: List[Card] = board.stock.peek_from_top(last=3)
        waste: List[Card] = board.waste.peek_from_top(last=3)
        foundations: List[Card] = list()
        for f in board.foundations:
            found_card: Card = f.peek_from_top()[0]
            if type(found_card) is NoneCard:
                foundations.append(MsgCard(content=board.EMPTY_ACE))
            else:
                foundations.append(found_card)

        header: List[List[Card]] = [
            # stock0, waste0, 5spaces
            [
                stock[0],
                waste[0],
                NoneCard(),
                MsgCard(content="   8   "),
                MsgCard(content="   9   "),
                MsgCard(content="   0   "),
                MsgCard(content="   -   ")
            ],

            # stock1, waste1, 1spaces, 4found
            [
                stock[1],
                waste[1],
                NoneCard(),
                foundations[0],
                foundations[1],
                foundations[2],
                foundations[3]
            ],

            # stock2, waste2, 5spaces
            [
                stock[2],
                waste[2],
                NoneCard(),
                NoneCard(),
                NoneCard(),
                NoneCard(),
                NoneCard()
            ],

            # 7spaces
            # TODO: Remove this. To be replaced with something in draw() method.
            [NoneCard() for _ in range(7)]
        ]

        return header


    def _assemble_tableau(self) -> List[List[Card]]:
        """
        Pulls in all cards from the board that will need to be drawn,
        and arranges them according to the structure of the tableau.

        Returns List[List[Card]].
        Each List[Card] represents one row of text in the console.
        None indicates no card in that spot.
        """
        board = self.board
        tableau: List[List[Card]] = list()
        # creating seven columns
        for _ in range(7):
            tableau.append(list())

        for i, column in enumerate(tableau):
            column.extend(board.tableau[i].contents) #TODO: may need to implement Stack.__iter__() protocol
            while len(column) < board.len_max_tableau:
                column.append(NoneCard())

        return tableau



    def _draw_header(self) -> None:
        """ Receives cards and their placement in the header, and translates that into ASCII text. """
        board = self.board
        header = self._assemble_header()
        for row in header:
            print(board.SEP, end="")
            for card in row:
                print(str(card), end=board.SEP)

            print("\n", end="")


    def _draw_tableau(self) -> None:
        """ Receives cards and their placement in the tableau, and translates that into ASCII text. """
        board = self.board
        tableau = self._assemble_tableau()
        for row_i in range(board.len_max_tableau):
            print(board.SEP, end="")
            for column in tableau:
                card = column[row_i]
                print(str(card), end=board.SEP)
        
            print("\n", end="")

        self._draw_section_separator(char=" ")

        for i, column in enumerate(tableau): # column numbers for controls reference
            print(board.SEP, f"   {i + 1}   ", sep="", end="")
        print(board.SEP)
        
    
    def _draw_section_separator(self, char:str="-"):
        board = self.board

        print(board.SEP, end="")
        for _ in range(7):
            print(board.CARD_WIDTH * char, end="")
            print(board.SEP, end="")
        print("\n", end="")


    def _draw_controls(self) -> None:
        # board: Board = self.board
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
            "Flip stock: s",
            "Move card with 'src dest [amt=1]'",
            sep="\t"
        )

    
    def _draw_err(self) -> None:
        if self.ui.current_input is None or self.ui.current_input.err is None:
            print()
            return
        
        print(f"{self.ui.current_input.err}")


    def draw(self) -> None:
        """ One method to call them all, and to the console draw them. """
        # board: Board = self.board

        os.system("cls||clear") # clears terminal
        self._draw_section_separator()
        self._draw_header()
        self._draw_section_separator()
        self._draw_tableau()
        self._draw_section_separator()
        self._draw_controls()
        self._draw_err()

        #TODO: This may move elsewhere
        self.board.cleanup_nonecards()
