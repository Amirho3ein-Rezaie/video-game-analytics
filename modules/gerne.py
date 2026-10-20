from pandas import DataFrame
from .func_analysis import group_analysis
from tools.classes import DatasetFields


def gerne_analysis(sales_field, show_result: bool = True) -> DataFrame:
    "analysis the genre field"

    return group_analysis(
        DatasetFields.GroupByFields.Genre.value, sales_field, show_result
    )
