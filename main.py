from modules.loader import read_data_file
from modules.prepare import (
    cleaning_data,
    change_columns_type,
    save_prepared_dataset_file,
)
from modules import stats, sales, gerne
from tools.func import (
    run_command,
    select_option,
    press_enter_to_continue,
    ask_yes_no,
    select_item,
    splitter,
    field_sales_select,
    head_select,
    select_comparison,
)
from tools.classes import DatasetSave

# variables
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

    analysis = [
        "Stats_analysis",
        "Sales_analysis",
        "Genre_analysis",
    ]  # list of analysis
    return select_item(analysis, 1, "select of analysis option ... ")


def select_sub_analysis(analysis: int) -> dict:
    "select sub analysis"

    # make list of sub analysis
    sub_analysis = [
        ["mean", "median", "std", "min", "max", "quartiles", "all"],
        [
            "Top-Selling Games",
            "Total Sales",
            "Copare Average Sales",
            "Regional Sales Comparison",
        ],
        [
            "Total Sales, Count, Mean sales by Genre",
        ],
    ]

    # select one of them
    result = select_item(
        ["Go back"] + sub_analysis[analysis - 1],
        GO_BACK_OPTION,
        "select one of sub analysis option ... ",
    )
    return result


def preform(analysis: int, sub_analysis: int) -> None:
    "preform the analysis function"

    # sub analysis options
    funcs = [
        [
            lambda: stats.describe_field(field_sales_select(), "mean"),
            lambda: stats.describe_field(field_sales_select(), "50%"),
            lambda: stats.describe_field(field_sales_select(), "std"),
            lambda: stats.describe_field(field_sales_select(), "min"),
            lambda: stats.describe_field(field_sales_select(), "max"),
            lambda: stats.quartiles(field_sales_select()),
            lambda: stats.all(field_sales_select()),
        ],
        [
            lambda: sales.top_salling(),
            lambda: sales.total_selling(field_sales_select()),
            lambda: sales.Copare_avrg_sales(
                select_comparison(), field_sales_select(), head_select()
            ),
            lambda: sales.regional_sales_comparison(),
        ],
        [
            lambda: gerne.gerne_analysis(sales_field=field_sales_select()),
        ],
    ]

    # run
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
        selected_sub_analysis = select_sub_analysis(selected_analysis)

        # go back if selected go back option in sub analysis
        if selected_sub_analysis == GO_BACK_OPTION:
            continue

        # run the function and start to analysis
        preform(selected_analysis, selected_sub_analysis)

        press_enter_to_continue()


if __name__ == "__main__":
    main()
