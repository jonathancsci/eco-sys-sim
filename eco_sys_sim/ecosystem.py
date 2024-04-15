from .plot import Plot
from .environment import Environment
import matplotlib.pyplot as plt
from rich.progress import track
import time
from .status import Status, MaxIterReached, UserTerminated


class Ecosystem:
    def __init__(self, rows: int = 5, cols: int = 10):
        self._animals_list: list[str] = ["bear", "wolf", "fox", "deer", "rabbit"]

        self._plot = Plot(animals_list=self._animals_list)

        self._environment = Environment(
            rows=rows, cols=cols, animals_list=self._animals_list
        )
        self._environment.attach(self._plot)

    def run_simulation(self, max_iters: int = 0) -> Status:
        # for _ in track(range(max_iters), description="Simulation status"):
        #     time.sleep(0.1)
        # return MaxIterReached
        for _ in track(range(max_iters), description="Simulation status"):
            self.step()
            if not plt.get_fignums():
                return UserTerminated
        return MaxIterReached

    def step(self):
        self._environment.step()
