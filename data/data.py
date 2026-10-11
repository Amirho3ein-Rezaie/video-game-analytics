from pandas import DataFrame


class Data:
    data = DataFrame()

    def set_data(self, loaded_data: DataFrame):
        self.data = loaded_data

    def get_data(self) -> DataFrame:
        return self.data


read_data = Data()
