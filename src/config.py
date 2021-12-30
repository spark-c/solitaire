from typing import Dict, Set

class Config:

    # Map board areas/stacks to selectors/keys
    KEYMAP: Dict[str, str] = {
            "waste": "w",
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

    EXTRA_COMMANDS: Set[str] = {
        "s", # flip stock
        "help"
    }