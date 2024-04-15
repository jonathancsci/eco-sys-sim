from ..actions.move_action import MoveAction
from ..actions.attack_action import AttackAction
from ..actions.reproduce_action import ReproduceAction
from ..actions.graze_action import GrazeAction
from ..actions.eat_action import EatAction
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
        if(target != grid):
            return MoveAction(self, self.size * 0.1, grid, target)
        foe = check_for_fight(grid)
        if(foe):
            return AttackAction(self, foe, foe.size*.5-self.size*.1)
        mate = check_for_mate(grid)
        if(mate):
            return ReproduceAction(self,self.size,mate,grid,type(self))
        food = check_for_food(grid)
        if(food):
            if(type(food)==Animal):
                return EatAction(self,food,grid)
            else:
                return GrazeAction(self,grid)
        

    def init_scores(self, grid: Grid):
        self.preferences = dict.fromkeys(grid.neighbors, self.dice_roll())
        self.preferences.update({grid: self.size+self.dice_roll()})

    def score_grid(self, grid: Grid):
        raise NotImplementedError
    
    def check_for_fight(self, grid: Grid):
        raise NotImplementedError
    
    def check_for_mate(self, grid: Grid):
        raise NotImplementedError

    def check_for_food(self, grid: Grid):
        raise NotImplementedError

    def check_for_meat(self, grid: Grid):
        for o in grid.occupants:
            if not o.alive:
                return o
        return None
    
    def check_for_grass(self, grid: Grid):
        if(grid.grass_level >= self.size):
            return grid.grass_level
        return None

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
