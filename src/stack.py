from typing import List
from src.card import Card


class Stack():
    
    def __init__(self):
        self.contents: List[Card|None] = list()

    
    def add_card(card, to="top"):
        pass