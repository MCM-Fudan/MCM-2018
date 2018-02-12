from dataset import Dataset
from model import BayesNetwork, MarkovNetwork
from reader import XLSLReader, CSVReader
from config import Config
def test_bnn():
    dataset = Dataset()
    dataset.load(XLSLReader, './data/聚类.xlsx')
    dataset.discretize_data(Config.divide_list_dic)
    bay = BayesNetwork(dataset=dataset, graph_structure_index=Config.graph_structure)
    bay.build_graph()
    bay.fit_model()
    bay.evaluate_result()
    bay.inference('fragility')

def test_markov():
    dataset = Dataset()
    dataset.load(XLSLReader, './data/聚类.xlsx')
    dataset.discretize_data(Config.divide_list_dic)
    bay = MarkovNetwork(dataset=dataset, graph_structure_index=Config.graph_structure)
    bay.build_graph()
    bay.fit_model()
    bay.evaluate_result()
    bay.inference('fragility')


if __name__ == '__main__':
    test_markov()