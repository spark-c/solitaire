import json
import os
from typing import List
from src.userinterface import UserInterface


err_log_prefix: str = "errlog"

def make_log(trace:Exception, ui:UserInterface) -> None:
    print("An error has occurred! Traceback:\n")
    print(trace)
    
    dump: str = json.dumps(ui, default=lambda obj: obj.encode(), indent=4)

    next_number: int = get_next_number()
    with open(f"err_logs/{err_log_prefix}{next_number}.json", "w") as f:
        f.write(dump)

    print(
        f"An error log has been saved at 'err_log/{err_log_prefix}{next_number}.json'."
    )


def get_next_number() -> int:
    files: List[str] = os.listdir("err_logs")
    return len(files) + 1
