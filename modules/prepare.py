from data.data import data


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
