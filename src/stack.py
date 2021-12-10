from typing import List
from src.card import Card


class Stack:

    def __init__(self, input=None) -> None:
        # default behavior
        if input is None:
            self.contents: list = list()
        # we should be getting a List[Card] as input
        elif type(input) is not list:
            raise TypeError("Argument 'contents' must be type 'list'")
        # input is a list; now we just hope that it contains Cards 
        # TODO: let's find a nice way to futher ensure that ^^^
        else:
            self.contents: list = input


    @property
    def length(self) -> int:
        return len(self.contents)

    
    def add_cards(self, input:List[Card], *, to:str="top") -> None:
        """
        Accepts a list of Cards to add to the Stack.
        to="top" will place those cards at the end of the list, i.e. physically atop the existing stack.
        to="bottom" will place those cards at the beginning of the list, i.e. physically underneath the stack.
        """

        if to not in ["top", "bottom"]:
            print(f"{to=}")
            raise ValueError("kwarg 'to' accepts 'top'(default) or 'bottom'.")
        if type(input) is not list:
            raise ValueError(f"Argument 'input' must be a list of Cards. (Received {type(input)}).")

        if to == "top":
            top: List[Card] = input
            bottom: List[Card] = self.contents
        else:
            top: List[Card] = self.contents
            bottom: List[Card] = input

        self.contents = bottom + top


    # TODO: Figure out how to add return type "Stack" without getting NameErrors
    def pop_from_top(self, last=1):
        """ Pops and returns the topmost card(s) from the Stack """
        returnable: List[Card] = list()
        for i in range(last):
            returnable.insert(0, self.contents.pop(-1))
        return Stack(input=returnable)


    def pop_from_bottom(self, first=1):
        """ Pops and returns the buried-most card(s) from the Stack. Not useful in standard Solitaire rules. """
        returnable: List[Card] = list()
        for i in range(first):
            returnable.append(self.contents.pop(0))
        return Stack(input=returnable)


    def peek_from_top(self, last=1):
        """ Returns the topmost card(s) from the Stack """
        index: int = 0 - last
        return self.contents[index]


    def peek_from_bottom(self, first=1):
        """ Returns the buried-most card(s) from the Stack. Not useful in standard Solitaire rules. """
        index: int = 0 + first
        return self.contents[index]
