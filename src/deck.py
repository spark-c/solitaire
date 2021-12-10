from src.stack import Stack
from src.card import Card


class Deck(Stack):

    def __init__(self) -> None:
        super().__init__()

        for suit in ["hearts", "spades", "diamonds", "clubs"]:
            for value in range(1, 14):
                new_card: Card = Card(suit=suit, value=value)
                self.contents.append(new_card)
