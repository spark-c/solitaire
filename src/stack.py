from typing import List
from src.card import Card


class Stack():

    def __init__(self):
        self.contents: List[Card|None] = list()


    @property
    def length(self):
        return len(self.contents)

    
    def add_card(card, to="top"):
        pass