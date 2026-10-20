from pandas import DataFrame
from tools.classes import DatasetFields
from tools.func import dataframe_as_table
from data.data import data


def group_analysis(
    group_by_field: DatasetFields.GroupByFields, sales_field, show_result: bool = True
) -> DataFrame:
    "analysis the dataset with group by fields"

    dataframe = data.get_data()

    # get the analysis
    dataframe = dataframe.groupby(group_by_field, as_index=False).agg(
        total_sales=(sales_field, "sum"),
        avg_sales=(sales_field, "mean"),
        count=(sales_field, "count"),
    )

    # show the result
    if show_result:
        dataframe[["total_sales", "avg_sales", "count"]] = (
            dataframe[["total_sales", "avg_sales", "count"]] * 1_000_000
        ).astype(int)

        dataframe_as_table(dataframe, ["total_sales", "avg_sales", "count"])

    return dataframe
