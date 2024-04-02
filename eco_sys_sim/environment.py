import numpy as np
import random
from .grid import Grid


class Environment:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols

        self._obstacle_grid = self._create_obstacle_grid()
        #  self._grid_map = self._create_grid_map()

    # TODO: Remove unnecessary getters
    # @property
    # def rows(self):
    #     return self._rows

    # @property
    # def cols(self):
    #     return self._cols

    # @property
    # def obstacle_grid(self):
    #     return self._obstacle_grid

    # @property
    # def grid_map(self):
    #     return self._grid_map

    def _find_neighbors(self, grid_coords: tuple):
        neighbors = []
        j, i = grid_coords
        potential_neighbors = [
            (j, i - 1),
            (j + 1, i - 1),
            (j + 1, i),
            (j + 1, i + 1),
            (j, i + 1),
            (j - 1, i + 1),
            (j - 1, i),
            (j - 1, i - 1),
        ]
        for y, x in potential_neighbors:
            if (
                0 <= y < self._rows
                and 0 <= x < self._cols
                and not self._obstacle_grid[y, x]
            ):
                neighbors.append((y, x))
        return neighbors

    def _create_obstacle_grid(self):
        # TODO: Switch to numpy arrays
        obstacles = np.zeros((self._rows, self._cols), dtype=int)
        for y in range(self._rows):
            for x in range(self._cols):
                if random.randint(0, 4) == 1:
                    obstacles[y, x] = 1
        return obstacles

    def _create_grid_map(self):
        grid_map = dict()
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.obstacle_grid[i][j]:
                    grid_map[(i, j)] = Grid()
        # TODO: Connect Grids
        return grid_map
