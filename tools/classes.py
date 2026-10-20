from enum import Enum
from data.data import data


class DatasetSave:
    "one class that have type dataset files and actions"

    class FormatsSave(Enum):
        "The formats that can save in them"

        csv = ".csv"
        json = ".json"
        xlsx = ".xlsx"

    class ActionsSave(Enum):
        "the action or method for save"

        all = "all"
        own = "own"

    class AllOptions(Enum):
        "one Enum that have all options"

        csv = ".csv"
        json = ".json"
        xlsx = ".xlsx"
        all = "all"
        own = "own"


class DatasetFields:
    "the fields of the dataset as enum"

    @staticmethod
    def StatsFields() -> Enum:
        "fields that can calculate the stats on them as Enum"

        dataset = data.get_data()

        columns = list(dataset.columns[5:])

        return Enum("StatsFields", {column: column for column in columns})

    class GroupByFields(Enum):
        "The fields that we group the dataset by them"

        Platform = "Platform"
        Year = "Year"
        Genre = "Genre"


class Comparison(Enum):
    "an Enum that defines the colltion"

    BIGGER = "BIGGER"
    LESS = "LESS"
    EQUAL = "EQUAL"
