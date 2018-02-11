import numpy as np
import pandas as pd
import config
from drawer import Drawer
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from dataset import Dataset
import pdb

class Bayes:
    def __init__(self, dataset, graph_structure_index):
        self.dataset = dataset
        self.columns = dataset.dataframe.columns
        self.graph_structure_index = graph_structure_index

    def build_graph(self):
        graph_structure_name = list(map(lambda tuple:
            (self.columns[tuple[0]], self.columns[tuple[1]]), self.graph_structure_index))
        self.model = BayesianModel(graph_structure_name)

    def fit_model(self, prior=False, prior_data = []):
        if prior:
            pseudo_counts = {
                {'D': [300, 700], 'I': [500, 500], 'G': [800, 200], 'L': [500, 500], 'S': [400, 600]}
            }
            raise NotImplementedError
        else:
            self.model.fit(self.dataset.dataframe, estimator=MaximumLikelihoodEstimator)


    def evaluate_result(self):
        for cpd in self.model.get_cpds():
            print("CPD of {variable}:".format(variable=cpd.variable))
            print(cpd)
            print()
            pdb.set_trace()

if __name__ == '__main__':
    pass

