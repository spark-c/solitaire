from src.config import config
from src.stack import Stack
from typing import TypedDict


class Values(TypedDict):
    src: Stack
    dest: Stack
    amt: int    

class Ruling(TypedDict):
    is_legal: bool
    values: Values
    err_msg: str


def check_logic(src: Stack, dest: Stack, amt: int) -> Ruling:
    # Return early if game logic disabled
    if config.GAME_LOGIC is False:
        return {
            "is_legal": True,
            "values": {"src": src, "dest": dest, "amt": amt},
            "err_msg": ""
        }

    # Check for repeating colors


    # Disallow moving cards that are hidden
    for card in src.contents:
        if card.visible is False:
            amt -= 1

    return {
        "is_legal": True,
        "values": {"src": src, "dest": dest, "amt": amt},
        "err_msg": ""
    }