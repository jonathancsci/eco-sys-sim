import numpy as np
from eco_sys_sim.environment import Environment
from eco_sys_sim.grid import Grid


class TestEnvironment:
    @classmethod
    def setup_class(cls):
        cls.instance = Environment(rows=5, cols=10)

    def test_constructor(self):
        assert self.instance._rows == 5
        assert self.instance._cols == 10

    def test_obstacle_grid(self):
        obstacle_grid: np.ndarray = self.instance._obstacle_grid
        obstacle_grid_set = set(obstacle_grid.flatten())
        contains_only_ones_and_zeros = obstacle_grid_set == set([0, 1])
        assert contains_only_ones_and_zeros

    def test_find_neighbors(self):
        neighbors = self.instance._find_neighbors((0, 0))
        assert isinstance(neighbors, list)

    def test_create_grid_map(self):
        grid_map = self.instance._grid_map
        _, grid = next(iter(grid_map.items()))
        assert isinstance(grid, Grid)

        neighbors_list = grid.neighbors
        assert isinstance(neighbors_list, list)

        if neighbors_list:
            first_neighbor = neighbors_list[0]
            assert isinstance(first_neighbor, Grid)
        else:
            assert len(neighbors_list) == 0
