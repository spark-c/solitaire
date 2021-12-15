from dataclasses import dataclass
from contextlib import suppress
from typing import List
from src.stack import Stack
from src.card import Card


class Foundation(Stack):
    
    def __init__(self, suit="") -> None:
        super().__init__()
        self.suit: str = suit


    # TODO: when an ace is put in self.contents, should update self.suit
    def validate_suit(self, stack, suit):
        """ To be used as a @validate_suit decorator for self.add_cards method """
        pass   
    
    # TODO: validation logic for what cards can be put into contents


class Board:
        
    CARD_WIDTH =    7 # "< ?? >"
    SPACE =         " " * CARD_WIDTH
    SEP =           " | "
    EMPTY_ACE =     " [Ace] "

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


    def deal(self, deck, shuffle=True) -> None:
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


    def flip_stock(self):
        """ Takes up to three cards from stock and flips them into waste """
        flipped_cards: List[Card] = self.stock.pop_from_top(3).contents
        for card in flipped_cards:
            with suppress(AttributeError): # ignoring errors from 'NoneType.reveal()'
                card.reveal()
        flipped_cards.reverse()
        self.waste.add_cards(flipped_cards)

    def cycle_stock(self):
        """ Moves all waste cards and flips them into stock """
        # TODO: test this method
        for card in self.board.waste[-1:-4]:
            if card is None:
                self.board.waste.remove(card)
        self.board.waste.contents.reverse()
        self.board.stock = self.board.waste
        self.board.waste = Stack()


    def stock_next(self):
        """ Plays the next stock move, flip or cycle, depending on how many cards in stock """
        pass