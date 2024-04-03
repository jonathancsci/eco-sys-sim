from .plot import Plot
from .environment import Environment
import matplotlib.pyplot as plt

class Ecosystem:
    def __init__(self):
        self._fig, self._ax = plt.subplots()
        self._plot = Plot(self._ax)
        self._environment = Environment(rows=5, cols=10)
