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


def select_option(options: Enum, msg: str):
    "Select one of the options in one enum"

    print(msg)  # show msg before showing options

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


def press_enter_to_continue() -> None:
    "the func that check enter pressed"

    print("Press enter to continue ... ", end="", flush=True)

    while True:
        char = getwch()

        if repr(char) == repr("\r"):
            break


def ask_yes_no(message: str) -> bool:
    "Ask a yes/no question"

    print(f"{message} (y/n): ", end="", flush=True)

    while True:
        key = getwch().lower()

        if key in ["y", "n"]:
            print(key)
            return True if key == "y" else False


def select_number_between(start: int, end: int, msg: str) -> int:
    "returns the number that selected between start and end"

    while True:

        # show
        print(f"{msg} [{start},{end}] : ", flush=True, end="")

        # select
        try:
            number = int(getwch())

            if number in [n for n in range(start, end + 1)]:
                print(number)
                return number

        except ValueError:
            print("\n" + "Invalid number ... ")


def select_item(items: list, start: int = 0, msg: str = "options") -> int:
    "returns the index of item that selected"

    # show message
    print(msg)

    # show the list of options
    for number, item in enumerate(items, start=start):
        print(f"({number}) {item}")

    # select the option
    return select_number_between(start, start + len(items) - 1, "select option")


def splitter(line: bool = True) -> None:
    "split selecion by a new line or by a line"

    if line == False:
        print()
    else:
        print("-" * 100)
