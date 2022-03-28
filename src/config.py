import os
from typing import Dict, List, Set


class Config:

    # Map board areas/stacks to selectors/keys
    KEYMAP: Dict[str, str] = {
            "waste": "/",
            "tableau0": "1",
            "tableau1": "2",
            "tableau2": "3",
            "tableau3": "4",
            "tableau4": "5",
            "tableau5": "6",
            "tableau6": "7",
            "foundations0": "8",
            "foundations1": "9",
            "foundations2": "0",
            "foundations3": "-"
        }

    SPECIALS: Dict[str, str] = {
        "all": "."
    }

    EXTRA_COMMANDS: Set[str] = {
        "+", # flip stock
        "help"
    }


    @property
    def accepted_chars(self) -> List[str]:
        extra_cmd_chars: List[str] = list()
        for cmd in self.EXTRA_COMMANDS:
            for char in cmd:
                extra_cmd_chars.append(char)
        
        return (
            list(self.KEYMAP.values()) +
            list(self.SPECIALS.values()) +
            extra_cmd_chars
        )

    @property
    def GAME_LOGIC(self) -> bool:
        logic: str = os.environ.get("GAME_LOGIC", "True").capitalize()
        return True if logic == "True" else False


config = Config()