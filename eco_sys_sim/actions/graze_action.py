from .action import Action


class ReproduceAction(Action):
    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    def __init__(self, animal, cost, current_grid, offspring):
        self._animal = animal
        self._energy_cost = cost
        self._current_grid = current_grid
        self._animal = animal

    def action(self):
        graze = self.current_grid.grass_level / 2
        self.animal.energy += graze
        self.current_grid.grass_level -= graze
