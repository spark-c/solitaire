class Card:
    def __init__(self, value:int, suit:str, *, visible:bool=False) -> None:
        self.value: int = value
        self.suit: str = suit
        self.visible = visible

    
    def reveal(self) -> None:
        self.visible = True

    
    def hide(self) -> None:
        self.visible = False