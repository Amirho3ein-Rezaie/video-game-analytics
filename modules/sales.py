from numpy import sum
from pandas import DataFrame
from data.data import data
from tools.func import dataframe_as_table, display_result


def top_salling(show_result: bool = True) -> DataFrame:
    "find the top salesing games in the dataset."

    dataframe = data.get_data()

    # get the top saleing games
    dataframe = dataframe.sort_values(by="Global_Sales", ascending=False).head(10)[
        ["Name", "Platform", "Year", "Genre", "Publisher", "Global_Sales"]
    ]

    if show_result:
        dataframe_copy = dataframe.copy()

        # change the value of global saleing
        dataframe_copy["Global_Sales"] = (
            dataframe_copy["Global_Sales"] * 1_000_000
        ).astype("int64")

        dataframe_as_table(dataframe_copy, ["Global_Sales"])

    return dataframe


def total_selling(field, show_result: bool = True) -> int:
    "calculate the total global saleing."

    dataframe = data.get_data()

    total = sum(dataframe[field])

    if show_result:
        display_result(dataframe[field].name, "total Selling", total)

    return total
