from src.board import Foundation
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

    ####-----------------------####
    #### Rules for Foundations ####
    ####-----------------------####
    
    if type(dest) == Foundation:

        # Empty foundations must begin with Ace (value 1)
        if dest.length == 0:
            if src.contents[0].value != 1:
                return {
                    "is_legal": False,
                    "values": {"src": src, "dest": dest, "amt": amt},
                    "err_msg": "Foundations must begin with Ace."
                }

        # Foundations must match suit
        if src.contents[0].suit != dest.peek_from_bottom()[0].suit:
            return {
                "is_legal": False,
                "values": {"src": src, "dest": dest, "amt": amt},
                "err_msg": "Foundations must match suit."
            }

        # Foundations must increment upwards
        if src.contents[0].value != dest.peek_from_top()[0].value + 1:
            return {
                "is_legal": False,
                "values": {"src": src, "dest": dest, "amt": amt},
                "err_msg": "Foundations must increment upwards."
            }

        # SUCCESS
        return {
            "is_legal": True,
            "values": {"src": src, "dest": dest, "amt": amt},
            "err_msg": ""
        }


    ####--------------------####
    #### Rules for Tableaus ####
    ####--------------------####

    # Only Kings (value 13) on empty tableaus
    if dest.length == 0 and src.peek_from_bottom()[0].value != 13:
        return {
            "is_legal": False,
            "values": {"src": src, "dest": dest, "amt": amt},
            "err_msg": "Only Kings may be placed on empty tableaus"
        }

    # Tableaus must alternate colors
    if src.peek_from_bottom()[0].color == dest.peek_from_top()[0].color:
        return {
            "is_legal": False,
            "values": {"src": src, "dest": dest, "amt": amt},
            "err_msg": "Cannot repeat card colors."
        }

    # Tableaus must decrement
    if src.peek_from_bottom()[0].value != dest.peek_from_top()[0].value - 1:
        return {
            "is_legal": False,
            "values": {"src": src, "dest": dest, "amt": amt},
            "err_msg": "Tableau values must decrement"
        }

    # Disallow moving cards that are hidden
    for card in src.contents:
        if card.visible is False:
            amt -= 1


    # SUCCESS
    return {
        "is_legal": True,
        "values": {"src": src, "dest": dest, "amt": amt},
        "err_msg": ""
    }