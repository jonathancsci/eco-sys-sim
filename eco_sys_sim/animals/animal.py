from ..actions.move_action import MoveAction
from ..actions.action import Action
from eco_sys_sim.grid import Grid
import random


class Animal:
    # energy that is spent on acitons and must be regaained through food
    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, energy):
        self._energy = energy

    # size provides a higher chance of winning combat and is the baseline for energy gained from eating the animal, it may also factor into energy cost as well
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    # boolean value for whether an animal is alive
    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive

    # storage for current preferences
    @property
    def preferences(self):
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        self._preferences = preferences

    # full list of methods
    def __init__(self, size=3):
        self._alive = True
        self._preferences = {}
        self._size = size
        self._energy = size * 1.5

    def step(self, grid: Grid):
        self.init_scores()
        for rm in self.preferences.keys():
            self.score_grid(rm)
        target = max(self.preferences, key=self.preferences.get)
        return MoveAction(self, self.size * 0.1, grid, target)

    def init_scores(self, grid: Grid):
        self.preferences = dict.fromkeys(grid.neighbors, self.dice_roll())
        self.preferences.update({grid: self.size+self.dice_roll()})

    def score_grid(self, grid: Grid):
        raise NotImplementedError

    def add_grid_score(self, value, grid):
        if grid in self.preferences.keys():
            self.preferences[grid] += value

    def nutritional_value(self):
        return 2 * self.size + self.energy

    def can_mate(self):
        return self.energy >= 2 * self.size

    def is_full(self):
        return self.energy >= 3 * self.size

    def dice_roll(self):
        return random.randint(1, 7)
