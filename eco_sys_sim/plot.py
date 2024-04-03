import numpy as np
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


class Plot:
    def __init__(self, ax: Axes):
        self._ax: Axes = ax
        self._x_list = list()
        self._y_lists = list()

    def update(self):
        pass
