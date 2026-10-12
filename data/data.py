from pandas import DataFrame


class Data:
    __data = DataFrame()

    def set_data(self, new_data: DataFrame):
        self.__data = new_data

    def get_data(self) -> DataFrame:
        return self.__data


read_data = Data()
