from enum import Enum
from msvcrt import getwch
from subprocess import run
from tools.classes import DatasetSave, DatasetFields, Comparison
from pandas import DataFrame


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


def splitter(line: bool = True, length_line: int = 100) -> None:
    "split selecion by a new line or by a line"

    if line == False:
        print()
    else:
        print("-" * length_line)


def display_result(field: str, statistic: str, result: float) -> None:
    """Display a formatted statistical analysis result."""

    print("=== Analysis result ===")
    print(f"Field: {field}")
    print(f"Statistic: {statistic}")
    print(f"Result: {result * 1000000:,.0f} units")


def dataframe_as_table(dataframe: DataFrame, number_columns: list = []) -> None:
    "get a dataframe and show it in table"

    # get the max of length for columns
    columns = dataframe.columns

    length = []
    for column in columns:

        len_column = [len(str(column))]
        for index in range(len(dataframe[column])):
            len_column.append(len(str(dataframe[column][index])))

        length.append(max(len_column))

    # split head
    print()
    splitter(length_line=(sum(length) + len(columns) * 3))

    # show columns
    for len_c, column in zip(length, columns):
        print(f" {column:<{len_c}} " + "|", end="")

    # split columns and the data in the table
    print()
    splitter(length_line=(sum(length) + len(columns) * 3))

    # show the data in the table
    for record in dataframe.values:

        for column, len_d, data in zip(dataframe.columns, length, record):

            # make specific fields that are numberic split
            try:
                if column in number_columns:
                    data = int(data)
                    print(f" {data:<{len_d},} " + "|", end="")
                else:
                    print(f" {data:<{len_d}} " + "|", end="")
            except:
                print(f" {data:<{len_d}} " + "|", end="")

        print()

    # split footer
    splitter(length_line=(sum(length) + len(columns) * 3))
    print()


def field_select():
    "select selling fields"

    # select
    field = select_option(
        DatasetFields.StatsFields(), "select one of the field ... "
    ).value

    # split
    splitter()

    return field


def select_comparison() -> Comparison:
    "select one Comparison for sub analysis that Copare somethings"

    # select one Comparison
    comparison = select_option(Comparison, "select one of the Comparison options ... ")

    # split
    splitter()

    return comparison


def head_select() -> int:
    "gets the number of heads for limitation of dataframes"

    # get number
    number = 0
    while True:
        try:
            number = int(input("Enter the head of dataframe : "))
            break
        except:
            pass

    # split
    splitter()

    return number
