from .animal import Animal


class Rabbit(Animal):
    def __init__(self):
        super().__init__(2)
        self._diet = Animal.eat_grass
        self._fears = [Fox, Deer, Wolf, Bear]

class Fox(Animal):
    def __init__(self):
        super().__init__(3)
        self._diet = Animal.eat_meat
        self._attacks = [Rabbit]
        self._fears = [Wolf, Bear]

class Deer(Animal):
    def __init__(self):
        super().__init__(6)
        self._diet = Animal.eat_grass
        self._fears = [Wolf, Bear]
        self._fights_back = True
        self._herds = True

class Wolf(Animal):
    def __init__(self):
        super().__init__(5)
        self._diet = Animal.eat_meat
        self._attacks = [Fox, Deer]
        self._fears = [Bear]
        self._herds = True
        self._fights_back = True

class Bear(Animal):
    def __init__(self):
        super().__init__(10)
        self._diet = Animal.eat_meat
        self._attacks = [Deer, Wolf]