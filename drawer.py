import numpy as np
import matplotlib.pyplot as plt
import os
import networkx as nx


def condition(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if self.is_save == True:
            plt.savefig(self.save_path)
        if self.is_show == True:
            plt.show()

    return wrapper


class Drawer:
    def __init__(self, title='', is_save=False, is_show=True, save_path='./'):
        self.title = title
        self.is_show = is_show
        self.save_path = save_path
        self.is_save = is_save
        self.is_show = is_show

    @condition
    def draw_matrix(self, matrix):
        fig, ax = plt.subplots()
        im = ax.imshow(matrix, cmap=plt.get_cmap('hot'), interpolation='nearest',
                           vmin=0, vmax=1)
        fig.colorbar(im)
        plt.title(self.title)

    @condition
    def draw_graph(self, model):
        nx.draw(model, with_labels=True)
        plt.draw()

    @condition
    def draw_3D(self, data, xlabel='x', ylabel='y', zlabel='z'):
        ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
        #  将数据点分成三部分画，在颜色上有区分度
        pass
        # high
        #
        # middle
        #
        # low
        #
        # ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
        # ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
        # ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
        #
        # ax.set_zlabel(zlabel)  # 坐标轴
        # ax.set_ylabel(ylabel)
        # ax.set_xlabel(xlabel)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    drawer = Drawer(is_save=True, is_show=False, save_path='img/test.jpg')
    drawer.draw_matrix(matrix)