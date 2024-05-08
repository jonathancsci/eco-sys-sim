from .animal import Animal
from ..actions.eat_action import EatAction
from ..actions.eat_action import PackEatAction
from ..actions.reproduce_action import ReproduceAction
from ..actions.reproduce_action import RabbitReproduceAction
from ..grid import Grid


class Rabbit(Animal):
    def __init__(self, age=-1):
        super().__init__(2, 0.05)
        self._diet = Animal.eat_grass
        self._fears = [Fox, Deer, Wolf, Bear]
        self._age = age

    def check_for_mate(self, grid: Grid, current_plan):
        if not current_plan is None:
            return current_plan
        if self.can_mate():
            for o in grid.occupants:
                if type(o) == type(self) and o != self:
                    return ReproduceAction(self, self.size * 0.5, o, grid, type(self))

    def can_mate(self):
        return self.energy >= 1.5 * self.size

    def is_full(self):
        return self.energy >= 3 * self.size


class Fox(Animal):
    def __init__(self, age=-1):
        super().__init__(3, 0.03)
        self._diet = Fox.eat_meat
        self._attacks = [Rabbit]
        self._fears = [Wolf, Bear]
        self._age = age

    def eat_meat(self, grid: Grid):
        for o in grid.occupants:
            if not o.alive:
                return EatAction(self, o, grid)
        return None


class Deer(Animal):
    def __init__(self, age=-1):
        super().__init__(5, 0.02)
        self._diet = Animal.eat_grass
        self._fears = [Wolf, Bear]
        self._fights_back = True
        self._herds = True
        self._age = age

    def is_full(self):
        return self.energy >= 4 * self.size


class Wolf(Animal):
    def __init__(self, age=-1):
        super().__init__(6, 0.02)
        self._diet = Wolf.eat_meat
        self._attacks = [Rabbit, Fox, Deer]
        self._fears = [Bear]
        self._herds = True
        self._fights_back = True
        self._age = age

    def eat_meat(self, grid: Grid):
        for o in grid.occupants:
            if (not o.alive) and (o.age <= 1.2) and not isinstance(self, type(o)):
                return PackEatAction(self, o, grid)
        return None

    def is_full(self):
        return self.energy >= 5 * self.size


class Bear(Animal):
    def __init__(self, age=-1):
        super().__init__(12, 0.01)
        self._diet = Animal.eat_meat
        self._attacks = [Deer, Wolf]
        self._age = age

    def init_scores(self, grid):
        self.preferences = dict.fromkeys(grid.neighbors, self.energy + self.dice_roll())
        self.preferences.update({grid: self.size + self.dice_roll()})

    def can_mate(self):
        return self.energy >= 3 * self.size

    def is_full(self):
        return self.energy >= 5 * self.size
