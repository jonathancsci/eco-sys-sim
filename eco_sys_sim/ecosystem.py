from .plot import Plot
from .environment import Environment
import matplotlib.pyplot as plt

class Ecosystem:
    def __init__(self):
        self._animals_list: list[str] = ['bear', 'wolf', 'fox', 'deer', 'rabbit']
        self._fig, self._ax = plt.subplots()
        self._plot = Plot(ax=self._ax, animals_list=self._animals_list)
        self._environment = Environment(rows=5, cols=10, animals_list=self._animals_list)
