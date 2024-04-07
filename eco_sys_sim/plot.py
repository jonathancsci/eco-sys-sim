from matplotlib.axes import Axes
from collections import deque

class Plot:
    def __init__(self, ax: Axes, animals_list: list[str]):
        self._ax: Axes = ax
        self._x_iters: deque[int] = deque()
        self._y_populations: dict[str, deque[int]] = {
            animal: deque() for animal in animals_list
        }

    def update(self, curr_iter: int, animal_populations: dict[str, int]):
        pass
