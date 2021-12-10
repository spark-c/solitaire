from dataclasses import dataclass
from typing import Dict, ClassVar


@dataclass
class Card:
    HEARTS: ClassVar[str] = "\u2665"
    SPADES: ClassVar[str] = "\u2660"
    DIAMONDS: ClassVar[str] = "\u2666"
    CLUBS: ClassVar[str] = "\u2663"

    value: int
    suit: str
    _visible: bool = False
    

    @property
    def visible(self) -> bool:
        return self._visible

    
    @property
    def color(self) -> str:
        return "red" if self.suit in [Card.HEARTS, Card.DIAMONDS] else "black"


    @property
    def face_value(self, peek=True) -> str:
        face_lookup: Dict[str, str] = {
            "1": "A",
            "11": "J",
            "12": "Q",
            "13": "K"
        }
        # dict.get(value-to-lookup, [fallback-return-value])
        return face_lookup.get(str(self.value), str(self.value))

    
    def __str__(self):
        if self._visible:
            return f"< {self.face_value}{self.suit} >"
        else:
            return "< ?? >"


    def reveal(self) -> None:
        self._visible = True


    def hide(self) -> None:
        self._visible = False