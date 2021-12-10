from src.stack import Stack
from src.card import Card


class Deck(Stack):

    def __init__(self):
        self.all_cards = []

        for suit in ["hearts", "spades", "diamonds", "clubs"]:
            for value in range(1, 14):
                new_card = Card(suit=suit, value=value)
                self.all_cards.append(new_card)

    @property
    def length(self):
        return len(self.all_cards)
