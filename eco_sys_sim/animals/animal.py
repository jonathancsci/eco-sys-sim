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

    # the animal's age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    # the rate an animal ages at
    @property
    def age_coeff(self):
        return self._age_coeff

    # size provides a higher chance of winning combat and is the baseline for energy gained from eating the animal, it may also factor into energy cost as well
    @property
    def size(self):
        return self._size

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
    def __init__(self, size, age_coeff):
        self._alive = True
        self._preferences = {}
        self._size = size
        self._age = -2
        self._age_coeff = age_coeff
        self._energy = size * 2
        self._fights_back = False
        self._herds = False
        self._diet = Animal.eat_grass
        self._fears = []
        self._attacks = []

    def step(self, grid: Grid):
        if(self.alive):
            action = self.check_for_move(grid)
            action = self.check_for_self_defense(grid,action)
            action = self.check_for_mate(grid,action)
            action = self.check_for_food(grid,action)
            action = self.check_for_hunt(grid,action)
            if(not action is None):
                return action
        #if you aren't alive or have nothing to do, do nothing
        return RestAction(self,grid)

    def init_scores(self, grid: Grid):
        self.preferences = dict.fromkeys(grid.neighbors, self.energy/2+self.dice_roll())
        self.preferences.update({grid: self.dice_roll()})

    def check_for_move(self, grid):
        self.init_scores(grid)
        for rm in self.preferences.keys():
            self.score_grid(rm)
        if(self.preferences[grid] < 0):
            self.age_up() #being near a predator is stressful
        target = max(self.preferences, key=self.preferences.get)
        if(target != grid):
            return MoveAction(self, self.size * 0.05, grid, target)
        else:
            return None

    def score_grid(self, grid):
        for o in grid.occupants:
            #animals prefer to move away from their predators
            if type(o) in self.fears:
                self.add_grid_score(-50, grid)
                #animals that fight back will prefer to stay if the predator is on top of them though
                if(self in grid.occupants and self.fights_back and random.random() > .75):
                    self.add_grid_score(70, grid)
                #animals will avoid rooms that their predators can approach them from (everything is viewed as a predator if skittish)
                if(self in o.attacks):
                    for rm in grid.neighbors:
                        self.add_grid_score(-30, grid)
            #carnivores prefer to move towards their prey when they are hungry
            elif ((type(o) in self.attacks) and (not self.is_full())):
                self.add_grid_score(o.nutritional_value(), grid)
            #herding animals and animals that can mate prefer to move towards eachother
            elif ((type(o) == type(self)) and (not o == self)):
                if((self.herds) and (o not in grid.occupants)):
                    self.add_grid_score(.25)
                if(self.can_mate()):
                    self.add_grid_score(self.energy/2, grid)
        #herbivores prefer taller grass
        if(self.diet == Animal.eat_grass and grid.grass_level >= self.size/2 and not self.is_full()):
            self.add_grid_score(grid.grass_level, grid)
    
    def check_for_self_defense(self, grid: Grid, current_plan):
        if(not current_plan is None):
            return current_plan
        if self.fights_back:
            for o in grid.occupants:
                if(o.alive and (type(o) in self.fears)):
                    return AttackAction(self, o.size*.3-self.size*.1, grid, o)
        return None
    
    def check_for_hunt(self, grid: Grid, current_plan):
        if(not current_plan is None):
            return current_plan
        if not self.is_full():
            for o in grid.occupants:
                if(o.alive and (type(o) in self.attacks)):
                    return AttackAction(self, o.size*.2-self.size*.1, grid, o)
        return None

    def check_for_food(self, grid: Grid, current_plan):
        if(not current_plan is None):
            return current_plan
        return self.diet(self, grid)
  
    def check_for_mate(self, grid: Grid, current_plan):
        if(not current_plan is None):
            return current_plan
        if self.can_mate():
            for o in grid.occupants:
                if(type(o) == type(self) and o != self):
                    return ReproduceAction(self,self.size*1.5,o,grid,type(self))
        return None

    def eat_meat(self, grid: Grid):
        for o in grid.occupants:
            if not o.alive and o.age <= 1.2 and not isinstance(self, type(o)):
                return EatAction(self,o,grid)
        return None
    
    def eat_grass(self, grid: Grid):
        if(not self.is_full() and grid.grass_level >= self.size/2):
            return GrazeAction(self,grid)
        return None

    def add_grid_score(self, value: int, grid):
        if grid in self.preferences.keys():
            self.preferences[grid] += value

    def nutritional_value(self):
        return 2 * self.size + self.energy

    def can_mate(self):
        return self.energy >= 2 * self.size

    def is_full(self):
        return self.energy >= 3 * self.size

    def age_up(self):
        if(self.alive):
            self._age += self._age_coeff
        else:
            if(self._age < 1):
                self._age = 1
            else:
                self._age += .25

    def dice_roll(self):
        return random.randint(1, 7)
