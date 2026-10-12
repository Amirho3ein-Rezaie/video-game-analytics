from pandas import read_csv, read_excel, read_json
from pathlib import Path
from data.data import data

# properties
RAW_DATA_DIR = "data/raw/"


# functions
def read_data_file(name_data_file: str) -> int:
    "read data file in xlsx, csv and json formats"

    # make path
    path_data_file = RAW_DATA_DIR + name_data_file

    file = Path(path_data_file)

    try:  # check existence of path
        suffixes_funcs = {"csv": read_csv, "json": read_json, "xlsx": read_excel}

        suffix_data_file = file.suffix.split(".")[1]

        try:
            # read file
            read_data = suffixes_funcs[suffix_data_file](path_data_file)

            data.set_data(read_data)  # save file in the special class
            data.set_file_type(suffix_data_file)  # save dataset file type

            return 0

        except ValueError as e:
            print(e)
            return 1

    except FileNotFoundError as e:
        print(e)
        return 1
