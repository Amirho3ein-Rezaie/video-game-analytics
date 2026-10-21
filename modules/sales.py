from numpy import sum, mean
from pandas import DataFrame
from data.data import data
from tools.func import dataframe_as_table, display_result
from tools.classes import Comparison, DatasetFields


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


def Compare_avrg_sales(
    Comparison: Comparison, sale_field, head: int = 10, show_result: bool = True
) -> DataFrame:
    "the records that their sales are above the average sales"

    dataframe = data.get_data()

    # select fields
    dataframe = dataframe[
        ["Name", "Platform", "Year", "Genre", "Publisher", sale_field]
    ]

    # Copare
    result = DataFrame()

    if Comparison == Comparison.BIGGER:
        result = dataframe[dataframe[sale_field] > mean(dataframe[sale_field])]

    elif Comparison == Comparison.LESS:
        result = dataframe[dataframe[sale_field] < mean(dataframe[sale_field])]

    elif Comparison == Comparison.EQUAL:
        result = dataframe[dataframe[sale_field] == mean(dataframe[sale_field])]

    # correct the format of sale field
    result = result.copy()
    result[sale_field] = result[sale_field] * 1_000_000

    # show the dataframe
    if show_result:
        print("=== The result analysis ===")
        print(
            f"The average of {sale_field} : {mean(dataframe[sale_field]) * 1_000_000:,.0f}"
        )
        dataframe_as_table(result.head(head), [sale_field])

    return result


def regional_sales_comparison(show_result: bool = True) -> DataFrame:
    "calculate the some analysis about the sale fields (total selling)"

    dataframe = data.get_data()

    # get the sale fields
    sale_fields = list(DatasetFields.StatsFields())

    # save the value of elements of the enum fields
    for index in range(len(sale_fields)):
        sale_fields[index] = sale_fields[index].value

    # cal the total
    total_selling_fields = []
    for field in sale_fields:
        total_selling_fields.append(sum(dataframe[field]))

    # make result dataframe
    result_dict = {}

    # add the fields to the dataset
    result_dict["Field name"] = sale_fields
    result_dict["Total selling (copy)"] = total_selling_fields

    # make dataframe
    result_dataframe = DataFrame(result_dict)

    # change the format of some fields
    result_dataframe["Total selling (copy)"] = (
        result_dataframe["Total selling (copy)"] * 1_000_000
    )

    # show the dataframe
    if show_result:
        dataframe_as_table(result_dataframe, ["Total selling (copy)"])

    return result_dataframe
