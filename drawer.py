import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import os


def condition(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if self.is_save == True:
            plt.savefig(self.save_path)
        if self.is_show == True:
            plt.show()

    return wrapper


class Drawer:
    def __init__(self, is_save=False, is_show=True, save_path='./'):
        self.is_show = is_show
        self.save_path = save_path
        self.is_save = is_save
        self.is_show = is_show

    @condition
    def draw_matrix(self, matrix):
        plt.matshow(matrix)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    drawer = Drawer(is_save=True, is_show=False, save_path='img/test.jpg')
    drawer.draw_matrix(matrix)