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

# variables
NEEDED_FIELD_SELECT = [1]  # save the number of analysis that needs select field
GO_BACK_OPTION = 0


# functions
def load_prepared_data() -> bool:
    "load data from a prepared dataset"

    file_name = input(
        "Enter the data file name that is in prepared folder in data (exp: data.csv): "
    )

    # check load dataset successfuly
    if read_data_file(file_name, prepared=True) == 0:
        return True
    else:
        print("Reading the prepared dataset file Failed ... ")
        return False


def load_raw_data() -> bool:
    "load the data from a raw dataset"

    file_name = input(
        "Enter the data file name that is in raw folder in data (exp: data.csv): "
    )

    # check load dataset successfuly
    if read_data_file(file_name) == 0:
        return True
    else:
        return False


def prepare_data() -> None:
    cleaning_data()  # clean the data

    change_columns_type()  # change type and name

    # save file
    option = select_option(DatasetSave.AllOptions, "Options for saving dataset ... ")
    save_prepared_dataset_file(option)


def select_analysis() -> int:
    "select analysis before select sub_analysis"

    analysis = ["stats"]  # list of analysis
    return select_item(analysis, 1, "select of analysis option ... ")


def select_sub_analysis(analysis: int) -> dict:
    "select sub analysis"

    # select field if need
    field = ""
    if analysis in NEEDED_FIELD_SELECT:
        # select one field to calculate on it
        field = select_option(
            DatasetFields.StatsFields(), "select one of the field ... "
        ).value
        splitter()

    # make list of sub analysis
    sub_analysis = [["mean", "median", "std", "min", "max", "quartiles", "all"]]

    # add suffix and prepare the list of sub analysis
    selected_list = []
    if analysis in NEEDED_FIELD_SELECT:
        added_suffix = [
            item + " " + f"({field})" for item in sub_analysis[analysis - 1]
        ]
        selected_list = ["Go back"] + added_suffix
    else:
        selected_list = ["Go back"] + sub_analysis[analysis - 1]

    # select one of them
    result = select_item(
        selected_list, GO_BACK_OPTION, "select one of sub analysis option ... "
    )
    return {"result": result, "field": field}


def preform(analysis: int, sub_analysis: int, field) -> None:
    "preform the analysis function"

    funcs = [
        [
            lambda: stats.describe_field(field, "mean"),
            lambda: stats.describe_field(field, "50%"),
            lambda: stats.describe_field(field, "std"),
            lambda: stats.describe_field(field, "min"),
            lambda: stats.describe_field(field, "max"),
            lambda: stats.quartiles(field),
            lambda: stats.all(field),
        ]
    ]

    splitter()

    funcs[analysis - 1][sub_analysis - 1]()

    splitter()


def main() -> None:

    loaded_data = False

    while True:
        run_command("cls")  # clean the terminal

        if loaded_data == False:

            if not ask_yes_no("Do you have prepared dataset file ?"):
                loaded_data = load_raw_data()

                if loaded_data:
                    prepare_data()
            else:
                loaded_data = load_prepared_data()

            if not loaded_data:
                press_enter_to_continue()
                continue

        # select one analysis
        splitter()
        selected_analysis = select_analysis()

        splitter()

        # select one sub analysis and one field if need
        result_select_sub_analysis = select_sub_analysis(selected_analysis)
        selected_sub_analysis = result_select_sub_analysis["result"]
        selected_field = result_select_sub_analysis["field"]

        # go back if selected go back option in sub analysis
        if selected_sub_analysis == GO_BACK_OPTION:
            continue

        # run the function and start to analysis
        preform(selected_analysis, selected_sub_analysis, selected_field)

        press_enter_to_continue()


if __name__ == "__main__":
    main()
