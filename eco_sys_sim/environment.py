import numpy as np
import random
from .animals.animal import Animal
from .animals.concrete_animals import Rabbit
from .animals.concrete_animals import Fox
from .animals.concrete_animals import Deer
from .animals.concrete_animals import Wolf
from .animals.concrete_animals import Bear
from .grid import Grid
from .plot import Plot


class Environment:
    def __init__(
        self,
        rows: int = 5,
        cols: int = 10,
        probability_of_obstacles: int = 0.2,
        init_num_bears: int = 2,
        init_num_wolves: int = 3,
        init_num_foxes: int = 5,
        init_num_deer: int = 10,
        init_num_rabbits: int = 30,
        animals_list: list[str] = ["bear", "wolf", "fox", "deer", "rabbit", "carrion"],
    ):
        self._rows: int = rows
        self._cols: int = cols
        self._animals_list: list[str] = animals_list
        self._observers: list[Plot] = list()
        self._iter_counter: int = 0
        self._probability_of_obstacles = probability_of_obstacles
        self._init_num_bears = init_num_bears
        self._init_num_wolves = init_num_wolves
        self._init_num_foxes = init_num_foxes
        self._init_num_deer = init_num_deer
        self._init_num_rabbits = init_num_rabbits

        self._obstacle_grid: np.ndarray = self._create_obstacle_grid()
        self._grid_map: dict[tuple, Grid] = self._create_grid_map()
        self._populate_grid_map()

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
        return np.random.choice(
            [0, 1],
            size=(self._rows, self._cols),
            replace=True,
            p=[1 - self._probability_of_obstacles, self._probability_of_obstacles],
        )

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
        for _ in range(self._init_num_bears):
            self._get_random_grid().add_occupant(Bear((random.random() * 2) - 2))
        for _ in range(self._init_num_wolves):
            self._get_random_grid().add_occupant(Wolf((random.random() * 2) - 2))
        for _ in range(self._init_num_foxes):
            self._get_random_grid().add_occupant(Fox((random.random() * 2) - 2))
        for _ in range(self._init_num_deer):
            self._get_random_grid().add_occupant(Deer((random.random() * 2) - 2))
        for _ in range(self._init_num_rabbits):
            self._get_random_grid().add_occupant(Rabbit((random.random() * 2) - 2))

    def attach(self, new_observer: Plot):
        self._observers.append(new_observer)

    def _notify_observers(self, animal_populations: dict[str, int]):
        for observer in self._observers:
            observer.update(self._iter_counter, animal_populations)

    def count_animal_populations(self) -> dict[str, int]:
        population_counter: dict[str, int] = {
            animal: 0 for animal in self._animals_list
        }
        for grid in self._grid_map.values():
            for occupant in grid.occupants:
                if occupant.alive:
                    match occupant:
                        case Bear():
                            population_counter["bear"] += 1
                        case Wolf():
                            population_counter["wolf"] += 1
                        case Fox():
                            population_counter["fox"] += 1
                        case Deer():
                            population_counter["deer"] += 1
                        case Rabbit():
                            population_counter["rabbit"] += 1
                        case _:
                            raise ValueError("Unknown animal type")
                else:
                    population_counter["carrion"] += 1
        return population_counter

    def step(self):
        populations = self.count_animal_populations()
        self._notify_observers(populations)

        actions = []
        for grid in self._grid_map.values():
            actions += grid.step()
        for action in actions:
            action.execute()

        self._iter_counter += 1

    def _get_random_grid(self):
        return random.choice(list(self._grid_map.values()))
