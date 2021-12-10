import random
from typing import List
from src.stack import Stack
from src.card import Card


class Deck(Stack):
    """
    A special Stack that auto-populates with all of the appropriate cards upon creation,
    and with a couple helper methods.
    """

    def __init__(self) -> None:
        super().__init__()

        for suit in [Card.HEARTS, Card.SPADES, Card.DIAMONDS, Card.CLUBS]:
            for value in range(1, 14):
                new_card: Card = Card(suit=suit, value=value)
                self.contents.append(new_card)


    def shuffle(self) -> None:
        random.shuffle(self.contents)

    
    def pre_deal(self) -> List[Stack]:
        """ Deals from the top of the deck into a list of seven Stacks for placing upon the game board. """
        self.shuffle()
        return [self.pop_from_top(last=value) for value in range(7)]
