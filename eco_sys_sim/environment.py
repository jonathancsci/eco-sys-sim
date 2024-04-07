import numpy as np
import random
from .grid import Grid


class Environment:
    def __init__(self, rows: int = 5, cols: int = 10, animals_list: list[str] = ['bear', 'wolf', 'fox', 'deer', 'rabbit']):
        self._rows: int = rows
        self._cols: int = cols
        self._animals_list = animals_list
        self._observers = list()

        self._obstacle_grid: np.ndarray = self._create_obstacle_grid()
        self._grid_map: dict[tuple, Grid] = self._create_grid_map()

    def _find_neighbors(self, grid_coords: tuple) -> list[tuple]:
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

    def _create_obstacle_grid(self) -> np.ndarray:
        obstacles = np.zeros((self._rows, self._cols), dtype=int)
        for y in range(self._rows):
            for x in range(self._cols):
                if random.randint(0, 4) == 1:
                    obstacles[y, x] = 1
        return obstacles

    def _create_grid_map(self) -> dict[tuple, Grid]:
        # Setup dictionary of Grids
        grid_map = dict()
        for y in range(self._rows):
            for x in range(self._cols):
                if not self._obstacle_grid[y, x]:
                    grid_map[(y, x)] = Grid()

        # Connect Grids
        for curr_coords, curr_grid in grid_map.items():
            curr_coords: tuple; curr_grid: Grid
            
            neighbor_coords = self._find_neighbors(curr_coords)
            neighbors_list: list[Grid] = []

            for neighbor_coord in neighbor_coords:
                neighbors_list.append(grid_map[neighbor_coord])

            curr_grid.neighbors = neighbors_list

        return grid_map

    def _populate_grid_map(self) -> None:
        # TODO
        pass

    def attach(self):
        pass

    def _notify_observers(self):
        pass

    def step(self):
        # TODO
        pass
