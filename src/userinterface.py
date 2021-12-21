from dataclasses import dataclass
from typing import List, Dict, Optional, TypedDict
from src.config import Config
from src.stack import Stack
from src.board import Board


@dataclass
class UserInput:
    """ Represents one piece of input submitted by the user """

    raw: str
    # cache for self.clean; unnecessary but makes me feel good
    _cleaned: str|None = None
    # extra_command flag indicates that the cmd is not the typical format of src,dest,amt. e.g. "s(flip stock)" or "help"
    extra_command: bool = False
    # self.board.current_input.err should be checked by the renderer in each render, and the msg displayed
    err: str|None = None

    
    @property
    def clean(self) -> str:
        if self._cleaned:
            return self._cleaned
            
        else:
            no_specials: List[str] = list(filter(lambda c: c.isalnum(), self.raw))
            self._cleaned = "".join(no_specials).lower()
            return self._cleaned


    @property
    def is_valid(self) -> bool:
        """ Checks that user input is in a valid format """
        cmd: str = self.clean
        if cmd in Config.EXTRA_COMMANDS:
            self.extra_command = True
            return True

        if cmd[0] == cmd[1]:
            self.err = f"Source and Destination can't be the same. You entered: {self.raw}"
            return False

        if len(cmd) != 3:
            self.err = f"Too many or not enough arguments! You entered: {self.raw}"
            return False

        return True


    class ParsedCmd(TypedDict):
        """ Contains the cleaned user input, and its parsed pieces """
        command: str|None
        src: str
        dest: str
        amt: int


    @property
    def parsed(self) -> ParsedCmd:
        """ Parses valid userinput into a dict(src:str, dest:str, amt:int) """
        if not self.is_valid:
            raise Exception("Invalid Input! TODO: replace this exception")

        cmd: str = self.clean
        return {
            "command": self.clean,
            "src": cmd[0] if not self.extra_command else "",
            "dest": cmd[1] if not self.extra_command else "",
            "amt": int(cmd[2]) if not self.extra_command else 0
        }

        
class UserInterface:
    """ Handles collecting, validating, and enacting user input/commands """

    def __init__(self, board: Board):
        self.board: Board = board
        self.current_input: Optional[UserInput] = None
        self.KEYMAP: Dict[str, Stack] = {
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


    def _enact(self) -> None:
        """ Receives a valid ParsedCmd dict and makes it so """
        if self.current_input is None: # to make the typechecker happy
            self.err = "Attempted to make a move with no input"
            return

        if self.current_input.extra_command is True:
            self.board.extra_commands[self.current_input.clean]()
            return

        src: Stack = self.KEYMAP[self.current_input.parsed["src"]]
        dest: Stack = self.KEYMAP[self.current_input.parsed["dest"]]
        amt: int = self.current_input.parsed["amt"]

        self.board.move_cards(src, dest, amt)


    def main_loop(self) -> None:
        """ This function should run one iteration of gathering -> handling input """
        pass


    def print_help(self) -> None:
        print("HELP COMMAND")