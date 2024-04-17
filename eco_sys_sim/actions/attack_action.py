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
        if self.target in self.current_grid.occupants and random.random() > 0.5:
            self.target.alive = False
