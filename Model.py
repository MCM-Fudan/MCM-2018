import numpy as np
import pandas as pd

from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
import pdb

class Bayes:
    def __init__(self, dataframe, graph_structure):
        self.dataframe = dataframe
        self.graph_structure = graph_structure


    def build_graph(self):
        self.model = BayesianModel(graph_structure)

    def fit_model(self, prior_type=False, prior_data = []):

        if prior_type:
            pseudo_counts = {
                {'D': [300, 700], 'I': [500, 500], 'G': [800, 200], 'L': [500, 500], 'S': [400, 600]}
            }
            raise NotImplementedError
        else:
            self.model.fit(self.dataframe, estimator=MaximumLikelihoodEstimator)

    def evaluate_result(self):
        for cpd in self.model.get_cpds():
            print("CPD of {variable}:".format(variable=cpd.variable))
            print(cpd)
            print()
            pdb.set_trace()

class NotDivideError(Exception):
    pass


def divider_factory(divide_list):
    '''
    This function is floor-preferenced.
    :param divide_list: the intervals
    :return: the generated divider
    '''

    divide_list.append(10000)
    divide_list.insert(0, 0)
    def divider(data):
        for index in range(len(divide_list[0:-1])):
            if data > divide_list[index] and data <= divide_list[index+1]:
                ret = divide_list[index]
                return ret

        raise NotDivideError

    return divider



if __name__ == '__main__':

    xl_file = pd.read_excel('./data/fsi-2017.xlsx', sheetname='2017')
    all_columns = xl_file.columns

    selected_index = [3, 4, 5, 6]

    graph_structure = [
        (all_columns[6], all_columns[5]),
        (all_columns[6], all_columns[4]),
        (all_columns[4], all_columns[3]),
        (all_columns[5], all_columns[3])
    ]
    selected_columns = np.array(all_columns[selected_index])
    dataframe = pd.read_excel('./data/fsi-2017.xlsx', sheetname='2017', usecols=selected_columns)

    divide_list_dic = {
        all_columns[3]: [10, 30, 50, 70, 90],
        all_columns[4]: [2, 8],
        all_columns[5]: [2, 8],
        all_columns[6]: [2, 8],
    }


    for (column, divide_list) in divide_list_dic.items():
        dataframe[column] = dataframe[column].map(divider_factory(divide_list))


    bay = Bayes(dataframe=dataframe, graph_structure=graph_structure)
    bay.build_graph()
    bay.fit_model()
    bay.evaluate_result()