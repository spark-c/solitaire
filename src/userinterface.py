from dataclasses import dataclass


@dataclass
class UserInput:
    """ Represents one piece of input submitted by the user """
    raw: str
    content: tuple[str, str, int]|None = None # src, dest, amt
    _is_valid: bool = False
        

class UserInterface:
    """ Handles collecting, validating, and enacting user input/commands """

    def __init__(self, board):
        self.board = board
        self.current_input: UserInput|None = None


    def _get_input(self) -> UserInput:
        """ Prompts user for input, collects, and returns as UserInput """
        user_in: str = input()
        return UserInput(raw=user_in)


    def _validate(self, raw_input:str) -> None:
        """ Checks that user input is in a valid format """
        pass


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