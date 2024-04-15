from .plot import Plot
from .environment import Environment
import matplotlib.pyplot as plt
from rich.progress import track
import time
from .status import Status, MaxIterReached, UserTerminated


class Ecosystem:
    def __init__(
            self,
            rows: int = 5,
            cols: int = 10,
            probability_of_obstacles: float = 0.2,
            ):
        self._animals_list: list[str] = ["bear", "wolf", "fox", "deer", "rabbit"]

        self._ax = plt.subplots()[1]
        self._plot = Plot(ax=self._ax, animals_list=self._animals_list)

        self._environment = Environment(
            rows=rows,
            cols=cols, 
            probability_of_obstacles=probability_of_obstacles,
            animals_list=self._animals_list,
        )
        self._environment.attach(self._plot)

    def run_simulation(self, num_iters: int = 0) -> tuple[Status, dict[str, int]]:
        # for _ in track(range(num_iters), description="Simulation status"):
        #     time.sleep(0.1)
        # return MaxIterReached
        status = None
        for _ in track(range(num_iters), description="Simulation status"):
            self.step()
            if not plt.get_fignums():
                status = UserTerminated()
                break
        status = MaxIterReached() if not status else status
        final_populations = self._environment.count_animal_populations()
        return status, final_populations

    def step(self):
        self._environment.step()
