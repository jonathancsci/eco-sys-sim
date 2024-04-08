from .plot import Plot
from .environment import Environment
import matplotlib.pyplot as plt


class Ecosystem:
    def __init__(self, rows: int = 5, cols: int = 10):
        self._animals_list: list[str] = ["bear", "wolf", "fox", "deer", "rabbit"]

        self._fig, self._ax = plt.subplots()
        self._plot = Plot(ax=self._ax, animals_list=self._animals_list)

        self._environment = Environment(
            rows=rows, cols=cols, animals_list=self._animals_list
        )
        self._environment.attach(self._plot)

    def run_simulation(self, max_iters: int = 0) -> str:
        for _ in range(max_iters):
            self.step()
            if not plt.get_fignums():
                return "window_closed"
        return "max_iters_reached"

    def step(self):
        self._environment.step()
