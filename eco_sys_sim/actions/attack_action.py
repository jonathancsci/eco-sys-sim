import random
from .action import Action


class AttackAction(Action):
    # target animal to attack
    @property
    def target(self):
        return self._target

    def __init__(self, animal, cost, target):
        self._animal = animal
        self._energy_cost = cost
        self._target = target

    def action(self):
        if random.random() > 0.5:
            self.target.alive = False
