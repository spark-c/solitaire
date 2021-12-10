from dataclasses import dataclass


@dataclass
class Card:
    value: int
    suit: str
    _visible: bool = False
    
    @property
    def visible(self) -> bool:
        return self._visible


    def reveal(self) -> None:
        self._visible = True


    def hide(self) -> None:
        self._visible = False