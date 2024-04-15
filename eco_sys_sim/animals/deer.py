from .animal import Animal
from .wolf import Wolf
from .bear import Bear


class Deer(Animal):
    def __init__(self):
        super().__init__(6,Animal.eat_grass)
        self.diet = Animal.eat_meat
        self.fears = [Wolf, Bear]
        self.fights_back = True
        self.herds = True
