from dataclasses import dataclass
from typing import Dict


@dataclass
class Card:
    value: int
    suit: str
    _visible: bool = False
    

    @property
    def visible(self) -> bool:
        return self._visible

    
    @property
    def color(self) -> str:
        return "red" if self.suit in ["hearts", "diamonds"] else "black"


    @property
    def face_value(self, peek=True) -> str:
        face_lookup: Dict[str, str] = {
            "1": "ace",
            "11": "jack",
            "12": "queen",
            "13": "king"
        }
        # dict.get(value-to-lookup, [fallback-return-value])
        return face_lookup.get(str(self.value), str(self.value))

    
    def __str__(self):
        if self._visible:
            return f"< {self.face_value} of {self.suit} >"
        else:
            return "< ?????????? >"


    def reveal(self) -> None:
        self._visible = True


    def hide(self) -> None:
        self._visible = False