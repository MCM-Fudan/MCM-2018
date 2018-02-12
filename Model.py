import numpy as np
import pandas as pd
import config
from drawer import Drawer
from pgmpy.models import BayesianModel, MarkovModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from dataset import Dataset
from mpl_toolkits.mplot3d import Axes3D
import pdb
import matplotlib.pyplot as plt
from pgmpy.factors.discrete import DiscreteFactor
import networkx as nx
class MarkovNetwork:
    def __init__(self, dataset, graph_structure_index):
        self.dataset = dataset
        self.columns = dataset.dataframe.columns
        self.graph_structure_index = graph_structure_index

    def build_graph(self):
        mm = MarkovModel()
        mm.add_nodes_from(self.dataset.dataframe.columns)
        graph_structure_name = list(map(lambda tuple:
            (self.columns[tuple[0]], self.columns[tuple[1]]), self.graph_structure_index))
        mm.add_edges_from(graph_structure_name)
        self.model = mm.to_bayesian_model()

    def fit_model(self):
        self.model.fit(self.dataset.dataframe[0:-3], estimator=MaximumLikelihoodEstimator)

    def draw_graph(self):
        pass

    def evaluate_result(self):
        for cpd in self.model.get_cpds():
            print("CPD of {variable}:".format(variable=cpd.variable))
            print(cpd)
            accept_node = cpd.variables[0]

            ##3D-dimension
            if len(cpd.values.shape) > 3:
                pass
                # Drawer.draw_3D(cpd.values, x_label=cpd.variables[1],
                #                y_label=cpd.variables[2], z_label=cpd.variables[3])
            ##2D Dimension
            elif len(cpd.values.shape) == 2:
                title = cpd.variables[1] + '----->' + accept_node
                Drawer(title=title, is_show=False, is_save=False,
                       save_path='img/' + title + '.jpg').draw_matrix(cpd.values)

class BayesNetwork:
    def __init__(self, dataset, graph_structure_index):
        self.dataset = dataset
        self.columns = dataset.dataframe.columns
        self.graph_structure_index = graph_structure_index

    def build_graph(self):
        graph_structure_name = list(map(lambda tuple:
            (self.columns[tuple[0]], self.columns[tuple[1]]), self.graph_structure_index))
        self.model = BayesianModel(graph_structure_name)

    def draw_graph(self):
        Drawer.draw_graph(self.model)


    def fit_model(self, prior=False, prior_data = []):
        if prior:
            pseudo_counts = {
                {'D': [300, 700], 'I': [500, 500], 'G': [800, 200], 'L': [500, 500], 'S': [400, 600]}
            }
            raise NotImplementedError
        else:
            self.model.fit(self.dataset.dataframe[0:-3], estimator=MaximumLikelihoodEstimator)

    def inference(self, name):
        from pgmpy.inference import VariableElimination
        self.infer = VariableElimination(self.model)
        q = self.infer.query(variables=[name])
        print (q[name])

    def evaluate_result(self):
        for cpd in self.model.get_cpds():
            print("CPD of {variable}:".format(variable=cpd.variable))
            print(cpd)
            accept_node = cpd.variables[0]

            ##3D-dimension
            if len(cpd.values.shape) > 3:
                pass
                # Drawer.draw_3D(cpd.values, x_label=cpd.variables[1],
                #                y_label=cpd.variables[2], z_label=cpd.variables[3])
            ##2D Dimension
            elif len(cpd.values.shape) == 2:
                title = cpd.variables[1] + '----->' + accept_node
                Drawer(title=title, is_show=False, is_save=False,
                       save_path='img/' + title + '.jpg').draw_matrix(cpd.values)


if __name__ == '__main__':
    pass

