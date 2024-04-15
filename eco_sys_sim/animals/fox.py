from .animal import Animal
from .rabbit import Rabbit


class Fox(Animal):
    def __init__(self):
        super().__init__(3,Animal.eat_meat)

    def score_grid(self, grid):
        for o in grid.occupants:
            if type(o) == Rabbit:
                self.add_grid_score(o.nutritional_value, grid)
            elif self.can_mate() and type(o) == Fox:
                self.add_grid_score(10)

    def check_for_fight(self, grid):
        if(not self.is_full):
            for o in grid.occupants:
                if type(o) == Rabbit:
                    return o