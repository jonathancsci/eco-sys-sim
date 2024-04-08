from .animal import Animal


class Rabbit(Animal):
    def __init__(self):
        super().__init__(2)

    def score_grid(self, grid):
        for o in grid.occupants:
            if type(o) != Rabbit:
                self.add_grid_score(-100, grid)
                for rm in grid.neighbors:
                    self.add_grid_score(-30, grid)
            elif self.can_mate():
                self.add_grid_score(10)
        self.add_grid_score(grid.grass_level, grid)
        self.add_grid_score(self.dice_roll, grid)
