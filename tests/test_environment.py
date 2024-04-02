import numpy as np
from eco_sys_sim.environment import Environment


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
        # print(neighbors)
        assert isinstance(neighbors, list)

    
