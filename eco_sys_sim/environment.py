import numpy as np
import random
from .animals.animal import Animal
from .animals.rabbit import Rabbit
from .grid import Grid
from .plot import Plot


class Environment:
    def __init__(
        self,
        rows: int = 5,
        cols: int = 10,
        animals_list: list[str] = ["bear", "wolf", "fox", "deer", "rabbit"],
    ):
        self._rows: int = rows
        self._cols: int = cols
        self._animals_list: list[str] = animals_list
        self._observers: list[Plot] = list()
        self._iter_counter: int = 0

        self._obstacle_grid: np.ndarray = self._create_obstacle_grid()
        self._grid_map: dict[tuple, Grid] = self._create_grid_map()

    @property
    def iter_counter(self):
        return self._iter_counter

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
            curr_coords: tuple
            curr_grid: Grid

            neighbor_coords: list[tuple] = self._find_neighbors(curr_coords)
            neighbors_list: list[Grid] = []

            for neighbor_coord in neighbor_coords:
                neighbors_list.append(grid_map[neighbor_coord])

            curr_grid.neighbors = neighbors_list

        return grid_map

    def _populate_grid_map(self) -> None:
        # TODO: replace with actual flexible creature population, possibly via builder pattern
        for i in range(0, 4):
            self.get_random_grid().add_occupant(Rabbit())
        pass

    def add_animal_at(self, animal, x, y):
        self.get_grid(x,y).add_occupant(animal)

    def attach(self, new_observer: Plot):
        self._observers.append(new_observer)

    def _notify_observers(self, animal_populations: dict[str, int]):
        for observer in self._observers:
            observer.update(self._iter_counter, animal_populations)

    def _count_animal_populations(self) -> dict[str, int]:
        population_counter: dict[str, int] = {
            animal: 0 for animal in self._animals_list
        }
        for grid in self._grid_map.values():
            for occupant in grid.occupants:
                match occupant:
                    # case Bear:
                    #     population_counter['bear'] += 1
                    # case Wolf:
                    #     population_counter['wolf'] += 1
                    # case Fox:
                    #     population_counter['fox'] += 1
                    # case Deer:
                    #     population_counter['deer'] += 1
                    # case Rabbit:
                    #     population_counter['rabbit'] += 1
                    case _:
                        raise ValueError("Unknown animal type")

        return population_counter

    def step(self):
        actions = []
        for g in self._grid_map:
            actions.append(g.step())
        for a in actions:
            a.execute()
        pass

    def get_random_grid(self):
        x = random.randint(0, self._rows)
        y = random.randint(0, self._cols)
        return self.get_grid(x, y)

    def get_grid(self, x, y):
        return self._grid_map[(x, y)]

    def animal_at(self, animal, x, y):
        return animal in self._grid_map[(x, y)].occupants