from .animal import Animal
from .deer import Deer
from .wolf import Wolf


class Bear(Animal):
    def __init__(self):
        super().__init__(10)
        self.diet = Animal.eat_meat
        self.attacks = [Deer, Wolf]
