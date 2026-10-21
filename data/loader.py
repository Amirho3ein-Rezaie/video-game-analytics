from pandas import read_csv, read_excel, read_json
from pathlib import Path
from data.data import data

# properties
RAW_DATA_DIR = "data/raw/"
PREPARED_DATA_DIR = "data/prepared/"


# functions
def read_data_file(name_data_file: str, prepared: bool = False) -> int:
    "read data file in xlsx, csv and json formats"

    # make path
    if not prepared:
        path_data_file = RAW_DATA_DIR + name_data_file
    elif prepared:
        path_data_file = PREPARED_DATA_DIR + name_data_file

    file = Path(path_data_file)

    if file.exists():  # check existance of path
        suffixes_funcs = {"csv": read_csv, "json": read_json, "xlsx": read_excel}

        suffix_data_file = file.suffix.split(".")[1]

        try:
            # read file
            read_data = suffixes_funcs[suffix_data_file](path_data_file)

            data.set_data(read_data)  # save file in the special class
            data.set_filename(name_data_file)  # save dataset file type

            return 0

        except ValueError as e:
            print(e)
            return 1

    else:
        print(f"{file} Not found ... !")
        return 1
