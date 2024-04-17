from .action import Action


class EatAction(Action):
    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    # target animal to eat
    @property
    def target(self):
        return self._target

    def __init__(self, animal, target, current_grid):
        self._animal = animal
        self._energy_cost = 0
        self._current_grid = current_grid
        self._target = target

    def action(self):
        if(self.target in self.current_grid.occupants):
            self.animal.energy += self.target.nutritional_value()
            self.current_grid.remove_occupant(self.target)
