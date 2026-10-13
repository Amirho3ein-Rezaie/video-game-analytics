from modules.loader import read_data_file
from modules.prepare import (
    cleaning_data,
    change_columns_type,
    save_prepared_dataset_file,
)
from tools.func import run_command, select_option, press_enter_to_continue
from tools.classes import DatasetSave


def main() -> None:

    while True:
        run_command("cls")  # clean the terminal

        file_name = input(
            "Enter the data file name that is in raw folder in data (exp: data.csv): "
        )
        if read_data_file(file_name) == 1:  # check load dataset successfuly
            press_enter_to_continue()
            continue

        cleaning_data()  # clean the data

        change_columns_type()  # change type and name

        # save file
        option = select_option(
            DatasetSave.AllOptions, "Options for saving dataset ... "
        )
        save_prepared_dataset_file(option)


if __name__ == "__main__":
    main()
