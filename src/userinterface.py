from dataclasses import dataclass


@dataclass
class UserInput:
    """ Represents one piece of input submitted by the user """
    raw: str
    cleaned: str
    content: tuple[str, str, int]|None = None # src, dest, amt
    _is_valid: bool = False
    err: str|None = None
        

class UserInterface:
    """ Handles collecting, validating, and enacting user input/commands """

    def __init__(self, board):
        self.board = board
        self.current_input: UserInput|None = None


    def _get_input(self) -> None:
        """ Prompts user for input, collects, and returns as UserInput """
        raw_in: str = input()
        for char in raw_in:
            if not char.isalnum():
                raw_in.replace(char, "")
        cleaned: str = raw_in.lower()
        self.current_input = UserInput(raw=raw_in, cleaned=cleaned)


    def _validate(self, input:UserInput) -> None:
        """ Checks that user input is in a valid format """
        cmd: str = input.cleaned
        if cmd == "help":
            input._is_valid = True

        if len(cmd) != 3:
            input._is_valid = False
            input.err = f"Too many or not enough arguments! You entered: {input.raw}"

        # TODO: finish validate


    def _parse(self) -> tuple[str, str, int]:
        """ Parses valid userinput into a tuple(src:str, dest:str, amt:int) """
        return ("", "", 0)


    def _enact(self, user_input: tuple) -> None:
        """ Receives a valid command tuple and """
        pass


    def main_loop(self) -> None:
        pass


    def print_help(self) -> None:
        print("HELP COMMAND")