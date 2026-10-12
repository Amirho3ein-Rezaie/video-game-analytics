from modules.loader import read_data_file
from tools.func import run_command
from data.data import read_data


def main() -> None:
    run_command("cls")  # clean the terminal

    file_name = input(
        "Enter the data file name that is in raw folder in data (exp: data.csv): "
    )
    read_data_file(file_name)

    print(read_data.get_data())


if __name__ == "__main__":
    main()
