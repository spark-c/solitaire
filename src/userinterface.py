from dataclasses import dataclass
from typing import List, Dict, Optional
from src.stack import Stack
from src.board import Board


@dataclass
class UserInput:
    """ Represents one piece of input submitted by the user """
    raw: str
    cleaned: str
    # TODO: maybe remove self.content
    content: tuple[str, str, int]|None = None # src, dest, amt
    _is_valid: bool = False
    err: str|None = None

        
class UserInterface:
    """ Handles collecting, validating, and enacting user input/commands """

    def __init__(self, board: Board):
        self.board: Board = board
        self.current_input: Optional[UserInput] = None
        self.KEYMAP: Dict[str, Stack] = {
            "w": self.board.waste,
            "1": self.board.tableau[0],
            "2": self.board.tableau[1],
            "3": self.board.tableau[2],
            "4": self.board.tableau[3],
            "5": self.board.tableau[4],
            "6": self.board.tableau[5],
            "7": self.board.tableau[6],
            "8": self.board.foundations[0],
            "9": self.board.foundations[1],
            "0": self.board.foundations[2],
            "-": self.board.foundations[3],
        }


    def _get_input(self, manual_input:str|None=None) -> None:
        """ Prompts user for input, collects, and returns as UserInput """
        if manual_input is not None:
            raw_in:str = manual_input
        else:
            raw_in: str = input()

        cleaning: List[str] = list(filter(lambda c: c.isalnum(), raw_in))
        cleaned: str = "".join(cleaning)
        self.current_input = UserInput(raw=raw_in, cleaned=cleaned)


    def _validate(self, input:Optional[UserInput]) -> None:
        """ Checks that user input is in a valid format """
        if input is None:
            return

        cmd: str = input.cleaned
        if cmd == "help":
            input._is_valid = True
            return

        if len(cmd) != 3:
            input._is_valid = False
            input.err = f"Too many or not enough arguments! You entered: {input.raw}"
            return

        input._is_valid = True


    def _parse(self) -> tuple[Stack, Stack, int]:
        """ Parses valid userinput into a tuple(src:Stack, dest:Stack, amt:int) """
        cmd: str = input.cleaned
        return (self.KEYMAP[cmd[0]], self.KEYMAP[cmd[1]], int(cmd[2]))


    def _enact(self, user_input: tuple) -> None:
        """ Receives a valid command tuple and """
        # try:
            # self.board.move_cards()
        pass


    def main_loop(self) -> None:
        pass


    def print_help(self) -> None:
        print("HELP COMMAND")