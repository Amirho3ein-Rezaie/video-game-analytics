from pandas import DataFrame


class Data:
    __data = DataFrame()
    file_type = None

    def set_data(self, new_data: DataFrame):
        self.__data = new_data

    def set_file_type(self, file_type: str):
        self.file_type = file_type

    def get_data(self) -> DataFrame:
        return self.__data


data = Data()
