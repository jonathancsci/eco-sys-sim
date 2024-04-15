from ..actions.move_action import MoveAction
from ..actions.attack_action import AttackAction
from ..actions.reproduce_action import ReproduceAction
from ..actions.graze_action import GrazeAction
from ..actions.eat_action import EatAction
from ..actions.rest_action import RestAction
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

    #storage for the diet function
    @property
    def diet(self):
        return self._diet

    #animals that a predator hunts
    @property
    def attacks(self):
        return self._attacks

    #animals to run away from
    @property
    def fears(self):
        return self._fears

    #whether an animal fights back when cornered
    @property
    def fights_back(self):
        return self._fights_back

    #whether an animal seeks others of its kind when not hoping to reproduce
    @property
    def herds(self):
        return self._herds

    # storage for current preferences
    @property
    def preferences(self):
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        self._preferences = preferences

    # full list of methods
    def __init__(self, size):
        self._alive = True
        self._preferences = {}
        self._size = size
        self._energy = size * 1.5
        self._fights_back = False
        self._herds = False
        self._diet = Animal.eat_grass
        self._fears = []
        self._attacks = []

    def step(self, grid: Grid):
        self.init_scores(grid)
        for rm in self.preferences.keys():
            self.score_grid(rm)
        target = max(self.preferences, key=self.preferences.get)
        if(target != grid):
            return MoveAction(self, self.size * 0.1, grid, target)
        foe = self.check_for_fight(grid)
        if(foe):
            return AttackAction(self, foe, foe.size*.5-self.size*.1)
        mate = self.check_for_mate(grid)
        if(mate):
            return ReproduceAction(self,self.size,mate,grid,type(self))
        food = self.check_for_food(grid)
        if(food):
            if(type(food)==Animal):
                return EatAction(self,food,grid)
            else:
                return GrazeAction(self,grid)
        return RestAction(self)  

    def init_scores(self, grid: Grid):
        self.preferences = dict.fromkeys(grid.neighbors, pow((self.size-self.energy),2)+self.dice_roll()*2)
        self.preferences.update({grid: (self.size*2)+self.dice_roll()*2})

    def score_grid(self, grid):
        for o in grid.occupants:
            #animals prefer to move away from their predators
            if type(o) in self.fears:
                self.add_grid_score(-100, grid)
                #animals that fight back will prefer to stay if the predator is on top of them though
                if(not(self in grid.occupants and self.fights_back)):
                    self.add_grid_score(150, grid)
                #animals will avoid rooms that their predators can approach them from (everything is viewed as a predator if skittish)
                if(self in o.attacks):
                    for rm in grid.neighbors:
                        self.add_grid_score(-50, grid)
            #carnivores prefer to move towards their prey when they are hungry
            elif ((type(o) in self.attacks) and (not self.is_full())):
                self.add_grid_score(o.nutritional_value, grid)
            #herding animals and animals that can mate prefer to move towards eachother
            elif ((self.herds or self.can_mate()) and (type(o) == type(self))):
                self.add_grid_score(5+self.energy)
        #herbivores prefer taller grass
        if(self.diet == Animal.eat_grass and not self.is_full()):
            self.add_grid_score(grid.grass_level, grid)
    
    def check_for_fight(self, grid: Grid):
        if self.fights_back:
            for o in grid.occupants:
                if(type(o) in self.fears):
                    return o
        if not self.is_full():
            for o in grid.occupants:
                if(type(o) in self.attacks):
                    return o
        return None

    def check_for_food(self, grid: Grid):
        return self.diet(self, grid)
  
    def check_for_mate(self, grid: Grid):
        if self.can_mate:
            for o in grid.occupants:
                if(type(o) == type(self) and o != self):
                    return o
        return None

    def eat_meat(self, grid: Grid):
        for o in grid.occupants:
            if not o.alive:
                return o
        return None
    
    def eat_grass(self, grid: Grid):
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
