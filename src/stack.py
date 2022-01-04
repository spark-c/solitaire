from typing import List, Optional
from src.card import Card, NoneCard


class Stack:
    """
    Used to give more semantic control over what are essentially lists of Cards.
    The Cards themselves are accessible via stack.contents
    """

    def __init__(self, input:Optional[List[Card]]=None) -> None:
        # default behavior
        if input is None:
            self.contents: List[Card] = list()
        # we should be getting a List[Card] as input
        elif type(input) is not list:
            raise TypeError("Argument 'contents' must be type 'list'")
        # input is a list; now we just hope that it contains Cards 
        # TODO: let's find a nice way to futher ensure that ^^^
        else:
            self.contents: List[Card] = input


    def __len__(self) -> int:
        return len(self.contents)


    @property
    def length(self) -> int:
        return len(self.contents)


    def __getitem__(self, n:int) -> Card:
        return self.contents[n]

    
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

        top: List[Card]
        bottom: List[Card]
        if to == "top":
            top = input
            bottom = self.contents
        else:
            top = self.contents
            bottom = input

        self.contents = bottom + top


    # TODO: add return type "Stack" without getting NameErrors.
    #       Use "Forward References"! Just surround "Stack" with quotes and Python will understand to resolve the reference later.
    def pop_from_top(self, last:int=1):
        """ Pops and returns the topmost card(s) from the Stack """
        returnable: List[Card] = list()
        for _ in range(last):
            if len(self.contents) > 0:
                returnable.insert(0, self.contents.pop(-1))
            else:
                returnable.insert(0, NoneCard())
        return Stack(input=returnable)


    def pop_from_bottom(self, first:int=1):
        """ Pops and returns the buried-most card(s) from the Stack. Not useful in standard Solitaire rules. """
        returnable: List[Card] = list()
        for _ in range(first):
            if len(self.contents) > 0:
                returnable.append(self.contents.pop(0))
            else:
                returnable.append(NoneCard())
        return Stack(input=returnable)


    def peek_from_top(self, last:int=1) -> List[Card]:
        """ Returns copies of the topmost card(s) from the Stack. Places None where there is no card available. """
        stop_index: int = 0 - last
        returnable: List[Card] = list()
        i: int = -1
        while i >= stop_index:
            try:
                returnable.insert(0, self.contents[i])
            except:
                returnable.insert(0, NoneCard())
            i -= 1
            
            if -100 > i > 100:
                raise Exception("Infinite while loop in Stack.peek_from_top()")

        return returnable


    def peek_from_bottom(self, first:int=1) -> List[Card]:
        """ Returns copies of the buried-most card(s) from the Stack. Places None where there is no card available. """
        stop_index: int = 0 + first
        returnable: List[Card] = list()
        i: int = 0
        while i < stop_index:
            try:
                returnable.append(self.contents[i])
            except:
                returnable.append(NoneCard())
            i += 1
            
            if -100 > i > 100:
                raise Exception("Infinite while loop in Stack.peek_from_bottom()")

        return returnable
