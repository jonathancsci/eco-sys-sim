from .action import Action


class GrazeAction(Action):
    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    def __init__(self, animal, current_grid):
        self._animal = animal
        self._energy_cost = 0
        self._current_grid = current_grid

    def action(self):
        graze = self.current_grid.grass_level / 2
        self.animal.energy += graze
        self.current_grid.grass_level -= graze
