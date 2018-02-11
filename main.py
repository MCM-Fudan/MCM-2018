from dataset import Dataset
from model import Bayes
from reader import XLSLReader, CSVReader
from config import Config

dataset = Dataset()
dataset.load(XLSLReader, './data/聚类.xlsx')
dataset.discretize_data(Config.divide_list_dic)

bay = Bayes(dataset=dataset, graph_structure_index=Config.graph_structure)
bay.build_graph()
bay.fit_model()
bay.evaluate_result()



