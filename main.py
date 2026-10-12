from modules.loader import read_data_file
from modules.prepare import cleaning_data, change_columns_type
from tools.func import run_command


def main() -> None:
    run_command("cls")  # clean the terminal

    file_name = input(
        "Enter the data file name that is in raw folder in data (exp: data.csv): "
    )
    read_data_file(file_name)

    cleaning_data()  # clean the data

    change_columns_type()  # change type and name


if __name__ == "__main__":
    main()
