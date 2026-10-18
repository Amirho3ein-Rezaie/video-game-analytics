from modules.loader import read_data_file
from modules.prepare import (
    cleaning_data,
    change_columns_type,
    save_prepared_dataset_file,
)
from modules import stats, sales
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
def load_data(prepared: bool) -> bool:
    "load data from the dataset file"

    # get the dataset file name
    file_name = ""
    if prepared:
        file_name = input(
            "Enter the data file name that is in prepared folder in data (exp: data.csv): "
        )
    else:
        file_name = input(
            "Enter the data file name that is in raw folder in data (exp: data.csv): "
        )

    # load the data
    if file_name != "":
        if read_data_file(file_name, prepared) == 0:
            return True
        else:
            print("loading data from dataset file Failed ... ")
            return False
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

    analysis = ["stats", "sales"]  # list of analysis
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
    sub_analysis = [
        ["mean", "median", "std", "min", "max", "quartiles", "all"],
        [
            "Top-Selling Games",
            "Total Global Sales",
            "Games Above Average Sales",
            "Regional Sales Comparison",
        ],
    ]

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


# make function for select field in every sub_analysis


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
        ],
        [
            lambda: sales.top_salling(),
            lambda: sales.total_selling(),
            lambda: None,
        ],
    ]

    splitter()

    funcs[analysis - 1][sub_analysis - 1]()

    splitter()


def main() -> None:

    loaded_data = False

    while True:
        run_command("cls")  # clean the terminal

        if loaded_data == False:

            prepared_flag = ask_yes_no("Do you have prepared dataset file ?")
            loaded_data = load_data(prepared_flag)

            if loaded_data and not prepared_flag:
                prepare_data()

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
