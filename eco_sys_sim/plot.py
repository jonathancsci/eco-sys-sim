import numpy as np
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        _, self._ax = plt.subplots()
        self._ax: Axes
        self._x_list = list()
        self._y_lists = list()

    def update(self):
        pass
