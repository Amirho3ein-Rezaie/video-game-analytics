from modules.loader import read_data_file
from modules.prepare import (
    cleaning_data,
    change_columns_type,
    save_prepared_dataset_file,
)
from tools.func import run_command, select_option, press_enter_to_continue, ask_yes_no
from tools.classes import DatasetSave


def main() -> None:

    while True:
        run_command("cls")  # clean the terminal

        prepared_dataset_flag = ask_yes_no("Do you have prepared dataset file ?")

        if not prepared_dataset_flag:
            file_name = input(
                "Enter the data file name that is in raw folder in data (exp: data.csv): "
            )

            # check load dataset successfuly
            if read_data_file(file_name) == 1:
                press_enter_to_continue()
                continue

            cleaning_data()  # clean the data

            change_columns_type()  # change type and name

            # save file
            option = select_option(
                DatasetSave.AllOptions, "Options for saving dataset ... "
            )
            save_prepared_dataset_file(option)

        elif prepared_dataset_flag:
            file_name = input(
                "Enter the data file name that is in prepared folder in data (exp: data.csv): "
            )

            # check load dataset successfuly
            if read_data_file(file_name, prepared=True) == 0:
                print("Reading the prepared dataset file Successfuly Done ... ")
                press_enter_to_continue()
                run_command("cls")
            else:
                print("Reading the prepared dataset file Failed ... ")
                press_enter_to_continue()


if __name__ == "__main__":
    main()
