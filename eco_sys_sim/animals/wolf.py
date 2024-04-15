from .animal import Animal
from .deer import Deer
from .fox import Fox
from .bear import Bear


class Wolf(Animal):
    def __init__(self):
        super().__init__(5)
        self.diet = Animal.eat_meat
        self.attacks = [Fox, Deer]
        self.fears = [Bear]
        self.herds = True
        self.fights_back = True
