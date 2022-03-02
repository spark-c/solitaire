from colorama import Fore, Style
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
        return Fore.RED if self.suit in [Card.HEARTS, Card.DIAMONDS] else Fore.WHITE


    @property
    def face_value(self, peek:bool=True) -> str:
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
            return f"< {self.face_value} {self.color}{self.suit}{Style.RESET_ALL} >" if self.face_value != "10" else f"< {self.face_value}{self.color}{self.suit}{Style.RESET_ALL} >"
        else:
            return "< ??? >"


    def reveal(self) -> None:
        self._visible = True


    def hide(self) -> None:
        self._visible = False


@dataclass
class MsgCard(Card):
    """ Used to display short messages in place of Cards on the game board. """
    content: str = ""
    value: int = 0
    suit: str = Card.HEARTS
    _visible: bool = True


    def __str__(self):
        return self.content

    
@dataclass
class NoneCard(Card):
    """ Used to indicate an empty place, usually when the user asks for more cards than are present in a Stack. """

    content: str = "       "
    value: int = 0
    suit: str = Card.HEARTS
    _visible: bool = True
    

    def __str__(self):
        return self.content


    def hide(self) -> None:
        """ Always visible """
        return


    def reveal(self) -> None:
        """ Always visible """
        return