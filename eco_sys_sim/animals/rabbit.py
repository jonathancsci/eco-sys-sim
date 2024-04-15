from .animal import Animal
from .fox import Fox
from .deer import Deer
from .wolf import Wolf
from .bear import Bear


class Rabbit(Animal):
    def __init__(self):
        super().__init__(2)
        self.diet = Animal.eat_grass
        self.fears = [Fox, Deer, Wolf, Bear]
