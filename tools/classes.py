from enum import Enum


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
