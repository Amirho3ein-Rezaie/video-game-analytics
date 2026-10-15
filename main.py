from modules.loader import read_data_file
from modules.prepare import (
    cleaning_data,
    change_columns_type,
    save_prepared_dataset_file,
)
from modules import stats
from tools.func import (
    run_command,
    select_option,
    press_enter_to_continue,
    ask_yes_no,
    select_item,
    splitter,
)
from tools.classes import DatasetSave, DatasetFields


def select_analysis() -> int:
    "select analysis before select sub_analysis"

    analysis = ["stats"]  # list of analysis
    return select_item(analysis, 1, "select of analysis option ... ")


def select_sub_analysis(analysis: int, field: DatasetFields.StatsFields):
    "select sub analysis"

    # make list of sub analysis
    sub_analysis = [["mean", "median", "std", "min", "max", "quartiles"]]

    added_suffix = [item + " " + f"({field})" for item in sub_analysis[analysis - 1]]
    selected_list = ["Go back"] + added_suffix

    # select one of them
    return select_item(selected_list, 0, "select of sub analysis option ... ")


def preform(analysis: int, sub_analysis: int, field: DatasetFields.StatsFields) -> None:
    "preform the analysis function"

    funcs = [
        [
            lambda field: stats.describe_field(field, "mean"),
            lambda field: stats.describe_field(field, "50%"),
            lambda field: stats.describe_field(field, "std"),
            lambda field: stats.describe_field(field, "min"),
            lambda field: stats.describe_field(field, "max"),
            lambda field: stats.quartiles(field),
        ]
    ]

    splitter()

    funcs[analysis - 1][sub_analysis - 1](field)

    splitter()


def main() -> None:

    loaded_data = False

    while True:
        run_command("cls")  # clean the terminal

        if loaded_data == False:
            prepared_dataset_flag = ask_yes_no("Do you have prepared dataset file ?")

            if not prepared_dataset_flag:
                file_name = input(
                    "Enter the data file name that is in raw folder in data (exp: data.csv): "
                )

                # check load dataset successfuly
                if read_data_file(file_name) == 1:
                    press_enter_to_continue()
                    continue

                loaded_data = True

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
                    loaded_data = True
                    run_command("cls")
                else:
                    print("Reading the prepared dataset file Failed ... ")
                    press_enter_to_continue()
                    continue

        # select one analysis
        splitter()
        selected_analysis = select_analysis()

        # select one field to calculate on it
        splitter()
        selected_field = select_option(
            DatasetFields.StatsFields(), "select one of the field ... "
        ).value

        splitter()

        # select one sub analysis to do on the field
        selected_sub_analysis = select_sub_analysis(selected_analysis, selected_field)

        # go back if selected go back option in sub analysis
        if selected_sub_analysis == 0:
            continue

        # run the function and start to analysis
        preform(selected_analysis, selected_sub_analysis, selected_field)

        press_enter_to_continue()


if __name__ == "__main__":
    main()
