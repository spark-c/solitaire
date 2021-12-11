from dataclasses import dataclass
from typing import List
from src.stack import Stack


class AceRow(Stack):
    
    def __init__(self, suit="") -> None:
        self.suit: str = suit


    # TODO: when an ace is put in self.contents, should update self.suit
    def validate_suit(self, stack, suit):
        """ To be used as a @validate_suit decorator for self.add_cards method """
        pass   
    
    # TODO: validation logic for what cards can be put into contents


class Board:

    def __init__(self) -> None:
        # Four AceRows; suits shouldn't be predefined, will be decided as player moves their aces.
        self.foundations: List[AceRow] = [AceRow() for _ in range(4)]
        self.tableau: List[Stack] = [Stack() for _ in range(7)]
        self.stock: Stack = Stack()
        self.waste: Stack = Stack()


    @property
    def _len_max_tableau(self) -> int:
        return max([len(tab) for tab in self.tableau])


    def deal(self, deck) -> None:
        # populate the tableau columns w/facedown cards
        for index, stack in enumerate(deck.pre_deal()):
            self.tableau[index].add_cards(stack.contents)
        # deal the final card to each column and reveal its face
        for tableau in self.tableau:
            tableau.add_cards(deck.pop_from_top().contents)
            tableau.contents[-1].reveal()
        # everything else goes to the stock
        self.stock.add_cards(deck.contents)

    
    def draw(self) -> None:
        def draw_header() -> None:
            pass
        pass

        """
        draw0
            stock
            tab0
        draw1
            waste
            tab1
        draw2
            tab2
        draw3
            tab3
            found0
        draw4
            tab4
            found1
        draw5
            tab5
            found2
        draw6
            tab6
            found3
        """

        """
        1. Find longest tableau
        2. Grid should be 7 wide x len(tableau) + 4
        Row0: stock0 waste0 5spaces
        Row1: stock1 waste1 1spaces found0 found1 found2 found3
        Row2: stock2 waste2 5spaces
        Row3: 7spaces
        """

        """
        < ?? > | < SS > |
        < ?? > | < SS > |        | < SS > | < SS > | < SS > | < SS > |
        < ?? > | < SS > |

        < SS > | < SS > | < SS > | < SS > | < SS > | < SS > | < SS > |
        """