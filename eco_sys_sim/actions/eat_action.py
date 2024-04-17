from .action import Action


class EatAction(Action):
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
            self.animal.energy += self.target.nutritional_value()*3
            self.current_grid.remove_occupant(self.target)

#wolves share, they eat less but can still eat meat that another animal has eaten
class PackEatAction(Action):

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
        self.animal.energy += self.target.nutritional_value()*2
        self.current_grid.remove_occupant(self.target)