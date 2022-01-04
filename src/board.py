from typing import List, Dict, Callable
from src.stack import Stack
from src.card import Card
from src.deck import Deck


class Foundation(Stack):
    
    def __init__(self, suit:str="") -> None:
        super().__init__()
        self.suit: str = suit


    # TODO: when an ace is put in self.contents, should update self.suit
    def validate_suit(self, stack:Stack, suit:str):
        """ To be used as a @validate_suit decorator for self.add_cards method """
        pass   
    
    # TODO: validation logic for what cards can be put into contents


class Board:
        
    CARD_WIDTH: int =    7 # "< ?? >"
    SPACE: str =         " " * CARD_WIDTH
    SEP: str =           " | "
    EMPTY_ACE: str =     " [Ace] "
    # TODO: Fix this type annot mess below. ex_comm["s"](Board)() should be ex_comm["s"](Board). used in userinterface.py
    extra_commands: Dict[str, Callable[["Board"], Callable[[], None]]] = {
        "s": lambda board: board.stock_next,
    }

    #TODO: connect UserInterface error messages to self.err on board to be rendered with the game board

    def __init__(self) -> None:
        # Four Foundations; suits shouldn't be predefined, will be decided as player moves their aces.
        self.foundations: List[Foundation] = [Foundation() for _ in range(4)]
        self.tableau: List[Stack] = [Stack() for _ in range(7)]
        self.stock: Stack = Stack()
        self.waste: Stack = Stack()


    @property
    def len_max_tableau(self) -> int:
        """ For use in determining how many rows are needed to draw the board. """
        return max([len(tab) for tab in self.tableau])


    def deal(self, deck:Deck, shuffle:bool=True) -> None:
        """ Takes a deck, pre_deal()s it, and places the card Stacks where they belong on the board. """
        # populate the tableau columns w/facedown cards
        for index, stack in enumerate(deck.pre_deal(shuffle=shuffle)):
            self.tableau[index].add_cards(stack.contents)
        # deal the final card to each column and reveal its face
        for tableau in self.tableau:
            tableau.add_cards(deck.pop_from_top().contents)
            tableau.contents[-1].reveal()
        # everything else goes to the stock
        self.stock.add_cards(deck.contents)


    def move_cards(self, source:Stack, destination:Stack, amt:int) -> None:
        if amt == -1:
            amt = len(source)

        cards_moving: Stack = source.pop_from_top(amt)
        destination.add_cards(cards_moving.contents)


    def flip_stock(self):
        """ Takes up to three cards from stock and flips them into waste """
        flipped_cards: List[Card] = self.stock.pop_from_top(3).contents
        for card in flipped_cards:
            card.reveal()
        flipped_cards.reverse()
        self.waste.add_cards(flipped_cards)


    def cycle_stock(self):
        """ Moves all waste cards and flips them into stock """
        # TODO: test this method
        for card in self.waste.contents:
            card.hide()

        self.move_cards(self.waste, self.stock, -1)


    def stock_next(self):
        """ Plays the next stock move, flip or cycle, depending on how many cards in stock """
        if len(self.stock) > 0:
            self.flip_stock()
        else:
            self.cycle_stock()