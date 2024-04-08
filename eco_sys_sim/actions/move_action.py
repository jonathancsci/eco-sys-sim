from .action import Action


class MoveAction(Action):
    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    # target grid
    @property
    def target_grid(self):
        return self._target_grid

    def __init__(self, animal, cost, current_grid, target_grid):
        self._animal = animal
        self._energy_cost = cost
        self._current_grid = current_grid
        self._target_grid = target_grid

    def action(self):
        self.target_grid.add_occupant(self.animal)
        self.current_grid.remove_occupant(self.animal)
