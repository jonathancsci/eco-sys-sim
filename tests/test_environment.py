import random
import numpy as np
import matplotlib.pyplot as plt
from eco_sys_sim.environment import Environment
from eco_sys_sim.grid import Grid
from eco_sys_sim.plot import Plot


class TestEnvironment:
    @classmethod
    def setup_class(cls):
        cls.environment = Environment()
        cls.plot = Plot()
        cls.animals_list: list[str] = ["bear", "wolf", "fox", "deer", "rabbit"]

    def test_constructor(self):
        assert self.environment._rows == 5
        assert self.environment._cols == 10

    def test_obstacle_grid(self):
        obstacle_grid: np.ndarray = self.environment._obstacle_grid
        obstacle_grid_set = set(obstacle_grid.flatten())
        contains_only_ones_and_zeros = obstacle_grid_set == set([0, 1])
        assert contains_only_ones_and_zeros

    def test_find_neighbors(self):
        neighbors = self.environment._find_neighbors((0, 0))
        assert isinstance(neighbors, list)

    def test_create_grid_map(self):
        grid_map = self.environment._grid_map
        _, grid = next(iter(grid_map.items()))
        assert isinstance(grid, Grid)

        neighbors_list = grid.neighbors
        assert isinstance(neighbors_list, list)

        if neighbors_list:
            first_neighbor = neighbors_list[0]
            assert isinstance(first_neighbor, Grid)
        else:
            assert len(neighbors_list) == 0

    def test_observer(self):
        dummy_data = {animal: random.randint(0, 9) for animal in self.animals_list}
        self.environment.attach(self.plot)
        self.environment._notify_observers(dummy_data)
        plt.close('all')
