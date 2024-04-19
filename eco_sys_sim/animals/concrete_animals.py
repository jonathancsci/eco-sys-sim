from .animal import Animal
from ..actions.eat_action import EatAction
from ..actions.eat_action import PackEatAction


class Rabbit(Animal):
    def __init__(self, age=-1):
        super().__init__(2,.04)
        self._diet = Animal.eat_grass
        self._fears = [Fox, Deer, Wolf, Bear]
        self._age = age

    def can_mate(self):
        return self.energy >= 2 * self.size
    
class Fox(Animal):
    def __init__(self, age=-1):
        super().__init__(5,.02)
        self._diet = Animal.eat_meat
        self._attacks = [Rabbit]
        self._fears = [Wolf, Bear]
        self._age = age

    def eat_meat(self, grid):
        for o in grid.occupants:
            if not o.alive:
                return EatAction(self,o,grid)
        return None

class Deer(Animal):
    def __init__(self, age=-1):
        super().__init__(8,.02)
        self._diet = Animal.eat_grass
        self._fears = [Wolf, Bear]
        #self._fights_back = True
        self._herds = True
        self._age = age

class Wolf(Animal):
    def __init__(self, age=-1):
        super().__init__(9,.015)
        self._diet = Animal.eat_meat
        self._attacks = [Rabbit, Fox, Deer]
        self._fears = [Bear]
        self._herds = True
        self._fights_back = True
        self._age = age

    def eat_meat(self, grid):
        for o in grid.occupants:
            if not o.alive:
                return PackEatAction(self,o,grid)
        return None

class Bear(Animal):
    def __init__(self, age=-1):
        super().__init__(18,.01)
        self._diet = Animal.eat_meat
        self._attacks = [Deer, Wolf]
        self._age = age

    def init_scores(self, grid):
        self.preferences = dict.fromkeys(grid.neighbors, self.energy/2+self.dice_roll())
        self.preferences.update({grid: (self.size*2)+self.dice_roll()})

    def can_mate(self):
        return self.energy >= 4 * self.size

    def is_full(self):
        return self.energy >= 6 * self.size