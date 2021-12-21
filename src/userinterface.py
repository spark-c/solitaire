from dataclasses import dataclass
from typing import List, Dict, Optional
from src.config import Config
from src.stack import Stack
from src.board import Board


@dataclass
class UserInput:
    """ Represents one piece of input submitted by the user """

    raw: str
    # cache for self.clean; unnecessary but makes me feel good
    _cleaned: str|None = None 
    err: str|None = None

    
    @property
    def clean(self) -> str:
        if self._cleaned:
            return self._cleaned
            
        else:
            no_specials: List[str] = list(filter(lambda c: c.isalnum(), self.raw))
            self._cleaned = "".join(no_specials) 
            return self._cleaned


    @property
    def is_valid(self) -> bool:
        """ Checks that user input is in a valid format """
        cmd: str = self.clean
        if cmd == "help":
            return True

        if len(cmd) != 3:
            self.err = f"Too many or not enough arguments! You entered: {input.raw}"
            return False

        return True

    
    @property
    def parsed(self) -> tuple[str, str, int]:
        """ Parses valid userinput into a tuple(src:str, dest:str, amt:int) """
        cmd: str = input.cleaned
        return (cmd[0], cmd[1], int(cmd[2]))

        
class UserInterface:
    """ Handles collecting, validating, and enacting user input/commands """

    def __init__(self, board: Board):
        self.board: Board = board
        self.current_input: Optional[UserInput] = None
        self.KEYMAP: Dict[str, Stack] = {
            # Config.KEYMAP["flip_stock"]: None,
            Config.KEYMAP["waste"]: self.board.waste,
            Config.KEYMAP["tableau0"]: self.board.tableau[0],
            Config.KEYMAP["tableau1"]: self.board.tableau[1],
            Config.KEYMAP["tableau2"]: self.board.tableau[2],
            Config.KEYMAP["tableau3"]: self.board.tableau[3],
            Config.KEYMAP["tableau4"]: self.board.tableau[4],
            Config.KEYMAP["tableau5"]: self.board.tableau[5],
            Config.KEYMAP["tableau6"]: self.board.tableau[6],
            Config.KEYMAP["foundations0"]: self.board.foundations[0],
            Config.KEYMAP["foundations1"]: self.board.foundations[1],
            Config.KEYMAP["foundations2"]: self.board.foundations[2],
            Config.KEYMAP["foundations3"]: self.board.foundations[3],
        }


    def _get_input(self, manual_input:str|None=None) -> None:
        """ Prompts user for input, collects, and returns as UserInput """
        if manual_input is not None:
            raw_in:str = manual_input
        else:
            raw_in: str = input()

        self.current_input = UserInput(raw=raw_in)


    def _enact(self, user_input: tuple) -> None:
        """ Receives a valid command tuple and """
        # try:
            # self.board.move_cards()
        pass


    def main_loop(self) -> None:
        """ This function should run one iteration of gathering -> handling input """
        pass


    def print_help(self) -> None:
        print("HELP COMMAND")