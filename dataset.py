import pandas as pd
from utils import divider_factory

class Dataset:
    def __init__(self):
        pass

    def load(self, reader, filepath):
        self.dataframe = reader.read(filepath)

    def discretize_data(self, divide_list_dic):
        columns = self.dataframe.columns
        divide_list_name = list(map(lambda item: (columns[item[0]], item[1]), divide_list_dic.items()))
        print(divide_list_name)
        for (column, divide_list) in divide_list_name:
            self.dataframe[column] = self.dataframe[column].map(divider_factory(divide_list))

class NewDataset(Dataset):

    def __init__(self):
        pass

if __name__ == '__main__':
    pass
