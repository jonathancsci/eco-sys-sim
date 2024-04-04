from matplotlib.axes import Axes
from collections import deque

class Plot:
    def __init__(self, ax: Axes):
        self._ax: Axes = ax
        self._x_iters: deque = deque()
        self._y_populations: dict[deque] = dict()

    def update(self):
        pass
