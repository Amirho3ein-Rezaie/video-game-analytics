from data.data import data
from pathlib import Path

PREPARED_DATA_DIR = "data/prepared/"


def cleaning_data() -> int:
    "get data from Data class and clean the raw_data"

    dataframe = data.get_data()

    # droping the rank column
    dataframe.drop(columns=["Rank"], inplace=True)

    # droping the name and year column
    dataframe.dropna(subset=["Name", "Year"], inplace=True)

    # fill the Na columns
    dataframe.fillna(
        {
            "Platform": "Unknown",
            "Genre": "Unknown",
            "Publisher": "Unknown",
        },
        inplace=True,
    )

    # drop records that have no value for sale columns
    dataframe.dropna(
        subset=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"],
        inplace=True,
    )

    # rest index after droping records
    dataframe.reset_index(drop=True, inplace=True)

    data.set_data(dataframe)  # save data

    return 0


def change_columns_type() -> int:
    "Change the data types of the dataset columns."

    dataframe = data.get_data()  # get the data from Data class

    dataframe = dataframe.astype(
        {"Name": str, "Platform": str, "Year": int, "Genre": str, "Publisher": str}
    )

    data.set_data(dataframe)

    return 0


def save_prepared_dataset_file(save_all_types: bool = False) -> int:
    "save the cleaned and prepared dataset to one file"

    # get info of dataset
    filename = data.filename
    type = Path(filename).suffix

    dataframe = data.get_data()

    # manage the save functions
    save_functions = {
        ".csv": lambda path: dataframe.to_csv(path, index=False),
        ".json": lambda path: dataframe.to_json(
            path, force_ascii=False, orient="records"
        ),
        ".xlsx": lambda path: dataframe.to_excel(path, index=False),
    }

    # save in all types
    if save_all_types:
        path = PREPARED_DATA_DIR + filename.split(".")[0]

        for t in save_functions.keys():
            save_functions[t](path + t)

        return 0

    # save dataset to the own file type
    path = PREPARED_DATA_DIR + filename
    save_functions[type](path)

    return 0
