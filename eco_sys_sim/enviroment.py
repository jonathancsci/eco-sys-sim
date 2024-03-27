import random


class Enviroment:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols

        self._obstacle_grid = self._create_obstacle_grid()
        self._grid_map = self._create_grid_map()

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def obstacle_grid(self):
        return self._obstacle_grid

    @property
    def grid_map(self):
        return self._grid_map

    def _find_neighbors(self, grid_coords: tuple):
        neighbors = []
        x, y = grid_coords
        potential_neighbors = [
            (x - 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x, y - 1),
            (x - 1, y - 1),
        ]
        for i, j in potential_neighbors:
            if (
                0 <= i < self.rows
                and 0 <= j < self.cols
                and not self.obstacle_grid[i][j]
            ):
                neighbors.append((i, j))
        return neighbors

    def _create_obstacle_grid(self):
        obstacles = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if random.randint(0, 4) == 1:
                    obstacles[i][j] = 1
        return obstacles

    def _create_grid_map(self):
        grid_map = dict()
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.obstacle_grid[i][j]:
                    grid_map[(i, j)] = {
                        # Grid class
                        "occupants": list(),
                        "grass_level": 50,
                        "neighbors": self._find_neighbors((i, j)),
                    }
        return grid_map

