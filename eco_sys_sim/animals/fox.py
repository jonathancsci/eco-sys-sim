from .animal import Animal
from .rabbit import Rabbit
from .wolf import Wolf
from .bear import Bear


class Fox(Animal):
    def __init__(self):
        super().__init__(3)
        self.diet = Animal.eat_meat
        self.attacks = [Rabbit]
        self.fears = [Wolf, Bear]