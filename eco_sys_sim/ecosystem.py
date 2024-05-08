from .plot import Plot
from .environment import Environment
import matplotlib.pyplot as plt
from rich.progress import track
from .status import Status, MaxIterReached, UserTerminated


class Ecosystem:
    def __init__(
        self,
        rows: int = 5,
        cols: int = 10,
        probability_of_obstacles: float = 0.2,
        init_num_bears: int = 2,
        init_num_wolves: int = 3,
        init_num_foxes: int = 5,
        init_num_deer: int = 10,
        init_num_rabbits: int = 30,
    ):
        self._animals_list: list[str] = [
            "bear",
            "wolf",
            "fox",
            "deer",
            "rabbit",
            "carrion",
        ]

        self._ax = plt.subplots()[1]
        self._plot = Plot(ax=self._ax, animals_list=self._animals_list)

        self._environment = Environment(
            rows,
            cols,
            probability_of_obstacles,
            init_num_bears,
            init_num_wolves,
            init_num_foxes,
            init_num_deer,
            init_num_rabbits,
            self._animals_list,
        )
        self._environment.attach(self._plot)

    def run_simulation(self, num_iters: int = 0) -> tuple[Status, dict[str, int]]:
        status = None
        for _ in track(range(num_iters), description="Simulation status"):
            self.step()
            if not plt.get_fignums():
                status = UserTerminated()
                break
        plt.close("all")
        status = MaxIterReached() if not status else status
        final_populations = self._environment.count_animal_populations()
        return status, final_populations

    def step(self):
        self._environment.step()
