import random
from .action import Action


class AttackAction(Action):
    # target animal to attack
    @property
    def target(self):
        return self._target

    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    def __init__(self, animal, cost, current_grid, target):
        self._animal = animal
        self._energy_cost = cost
        self._current_grid = current_grid
        self._target = target

    def action(self):
        if self.target in self.current_grid.occupants:
            if random.random() > 0.5 - (0.1 * self.animal.size) + (
                0.1 * self.target.size
            ):
                self.target.alive = False
            else:
                self.target.age_up()
