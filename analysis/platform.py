from pandas import DataFrame
from tools.func_analysis import group_analysis
from tools.classes import DatasetFields


def platform_analysis(sales_field, show_result: bool = True) -> DataFrame:
    "analysis the genre field"

    return group_analysis(
        DatasetFields.GroupByFields.Platform.value, sales_field, show_result
    )
