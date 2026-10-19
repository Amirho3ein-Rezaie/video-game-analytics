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
        "read the dataset and returns the fields that can calculate the stats on them as Enum"

        dataset = data.get_data()

        columns = list(dataset.columns[5:])

        return Enum("StatsFields", {column: column for column in columns})


class Collation(Enum):
    "an Enum that defines the colltion"

    BIGGER = "BIGGER"
    LESS = "LESS"
    EQUAL = "EQUAL"
