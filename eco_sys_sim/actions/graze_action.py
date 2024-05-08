from .action import Action


class GrazeAction(Action):
    def __init__(self, animal, current_grid):
        self._animal = animal
        self._energy_cost = 0
        self._current_grid = current_grid

    def action(self):
        graze = min(self.animal.size * 0.5, self.current_grid.grass_level * 0.5)
        self.animal.energy += graze * 2
        self.current_grid.grass_level -= graze
