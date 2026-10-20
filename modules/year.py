from pandas import DataFrame
from tools.func_analysis import group_analysis
from tools.classes import DatasetFields


def year_analysis(sales_field, show_result: bool = True) -> DataFrame:
    "analysis the genre field"

    return group_analysis(
        DatasetFields.GroupByFields.Year.value, sales_field, show_result
    )
