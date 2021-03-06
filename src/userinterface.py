from dataclasses import dataclass
from typing import Any, List, Dict, Optional, TypedDict
from src.card import NoneCard
from src.config import config
from src.logic import check_logic, Ruling
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
            filtered: List[str] = list(filter(
                lambda c: c.lower() in config.accepted_chars,
                self.raw
            ))
            self._cleaned = "".join(filtered).lower()
            return self._cleaned


    @property
    def is_valid(self) -> bool:
        """ Checks that user input is in a valid format """
        cmd: str = self.clean
        if cmd in config.EXTRA_COMMANDS:
            self.extra_command = True
            return True

        if len(cmd) == 0:
            self.err = "Empty input!"
            return False

        # this format used to invoke card.reveal()
        if len(cmd) == 1 and cmd in config.KEYMAP.values():
            return True

        if cmd[0] == cmd[1]:
            self.err = f"Source and Destination can't be the same. You entered: {self.raw}"
            return False

        if len(cmd) > 3:
            self.err = f"Command not recognized (Too many chars)! You entered: {self.raw}"
            return False

        for index, char in enumerate(cmd):
            if char not in config.KEYMAP.values():
                if char not in config.SPECIALS.values() or index != 2: #cmd[2], which is allowed to be "."
                    self.err = f"Selector '{char}' not recognized! You entered: {self.raw}"
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
        src: str = ""
        dest: str = ""
        amt: int = 0

        if self.extra_command:
            return {
                "command": cmd,
                "src": src,
                "dest": dest,
                "amt": 0
            }

        src = cmd[0]
        dest = cmd[1]
        if len(cmd) == 2:
            amt = 1 # default move 1 card if not specified
        elif cmd[-1] == ".":
            amt = -1
        else:
            amt = int(cmd[2])

        return {
                "command": cmd,
                "src": src,
                "dest": dest,
                "amt": amt
            }

    
    def encode(self) -> Dict[str, Any]:
        return self.__dict__

        
class UserInterface:
    """ Handles collecting, validating, and enacting user input/commands """

    def __init__(self, board: Board):
        self.board: Board = board
        self.current_input: UserInput = UserInput(raw="")
        self.KEYMAP: Dict[str, Stack] = {
            config.KEYMAP["waste"]: self.board.waste,
            config.KEYMAP["tableau0"]: self.board.tableau[0],
            config.KEYMAP["tableau1"]: self.board.tableau[1],
            config.KEYMAP["tableau2"]: self.board.tableau[2],
            config.KEYMAP["tableau3"]: self.board.tableau[3],
            config.KEYMAP["tableau4"]: self.board.tableau[4],
            config.KEYMAP["tableau5"]: self.board.tableau[5],
            config.KEYMAP["tableau6"]: self.board.tableau[6],
            config.KEYMAP["foundations0"]: self.board.foundations[0],
            config.KEYMAP["foundations1"]: self.board.foundations[1],
            config.KEYMAP["foundations2"]: self.board.foundations[2],
            config.KEYMAP["foundations3"]: self.board.foundations[3],
        }


    def encode(self) -> Dict[str, Any]:
        return self.__dict__


    def _get_input(self, manual_input:Optional[str]=None) -> None:
        """ Prompts user for input, collects, and returns as UserInput """
        if manual_input is None:
            raw_in: str = input("Enter move: ")
        else:
            raw_in:str = manual_input

        if raw_in == "qwer":
            raise Exception("test exception")

        self.current_input = UserInput(raw=raw_in)


    def _enact(self) -> None:
        """ Receives a valid ParsedCmd dict and makes it so """
        if self.current_input is None: # to make the typechecker happy
            self.err = "Attempted to make a move with no input"
            return

        # execute a command found in board.extra_commands mapping
        if self.current_input.extra_command is True:
            self.board.extra_commands[self.current_input.clean](self.board)
            return

        # used to .reveal() topcard in a column
        if len(self.current_input.clean) == 1:
            stack: Stack = self.KEYMAP[self.current_input.clean]
            stack[-1].reveal()
            return

        src: Stack = self.KEYMAP[self.current_input.parsed["src"]]
        dest: Stack = self.KEYMAP[self.current_input.parsed["dest"]]
        amt: int = self.current_input.parsed["amt"]

        # need to check legality of just the cards moving, not the whole tableau
        # also, ignore NoneCards
        src_no_nones: Stack = Stack(
            list(filter(
                lambda card: type(card) is not NoneCard,
                src.contents
            ))
        )
        src_to_check = Stack(src_no_nones.peek_from_top(last=amt))
       
        ruling: Ruling = check_logic(src_to_check, dest, amt)
        allowed_amt = ruling["amt"]

        if ruling["is_legal"]:
            self.board.move_cards(src, dest, allowed_amt)
            self.current_input.err = ruling['err_msg']
        else:
            self.current_input.err = ruling["err_msg"]


    def main_loop(self, manual_input:Optional[str]=None) -> None:
        """ This function should run one iteration of gathering -> handling input """
        if manual_input is None:
            self._get_input()
        else:
            self._get_input(manual_input=manual_input)

        if self.current_input.is_valid:
            self._enact()


    def print_help(self) -> None:
        print("HELP COMMAND")