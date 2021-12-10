class Card:
    def __init__(self, value, suit) -> None:
        self.value: int = value
        self.suit: str = suit
        self.revealed: bool = False
