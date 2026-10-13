from enum import Enum
from msvcrt import getwch
from subprocess import run


def run_command(command: str) -> int:
    "run one command in terminal"
    try:
        run(command, shell=True)
        return 0
    except:
        return 1


def select_option(options: Enum):
    "Select one of the options in one enum"

    # show the enum options
    for index, option in enumerate(options, start=1):
        print(f"({index}) {option.name}")

    list_options = list(options)

    # select one of them
    selected_option = ""
    print("Enter number of one option : ", flush=True, end="")

    while True:
        try:
            option = int(getwch())
        except ValueError:
            pass

        if option in list(range(1, len(options) + 1)):
            print(option)
            selected_option = list_options[option - 1]
            break

    return selected_option
