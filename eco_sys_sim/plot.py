import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from collections import deque

class Plot:
    def __init__(self, ax: Axes, animals_list: list[str]):
        self._ax: Axes = ax
        self._x_iters: deque[int] = deque(maxlen=50)
        self._y_populations: dict[str, deque[int]] = {
            animal: deque(maxlen=50) for animal in animals_list
        }
        self._plot_lines: dict[str, Line2D] = {animal: ax.plot(self._x_iters, population, label=animal)[0] for animal, population in self._y_populations.items()}
        self._ax.legend(loc='upper left')

    def update(self, curr_iter: int, animal_populations: dict[str, int]):
        self._x_iters.append(curr_iter)
        for animal, curr_population in animal_populations:
            self._y_populations[animal].append(curr_population)
            self._plot_lines[animal].set_data(self._x_iters, self._y_populations[animal])

        self._ax.relim()
        self._ax.autoscale_view()
        plt.draw()
        plt.pause(0.1)
