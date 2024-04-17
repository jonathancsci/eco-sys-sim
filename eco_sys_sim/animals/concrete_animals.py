from .animal import Animal


class Rabbit(Animal):
    def __init__(self):
        super().__init__(1,.075)
        self._diet = Animal.eat_grass
        self._fears = [Fox, Deer, Wolf, Bear]

class Fox(Animal):
    def __init__(self):
        super().__init__(4,.05)
        self._diet = Animal.eat_meat
        self._attacks = [Rabbit]
        self._fears = [Wolf, Bear]

class Deer(Animal):
    def __init__(self):
        super().__init__(6,.05)
        self._diet = Animal.eat_grass
        self._fears = [Wolf, Bear]
        self._fights_back = True
        self._herds = True

class Wolf(Animal):
    def __init__(self):
        super().__init__(7,.025)
        self._diet = Animal.eat_meat
        self._attacks = [Rabbit, Fox, Deer]
        self._fears = [Bear]
        self._herds = True
        self._fights_back = True

class Bear(Animal):
    def __init__(self):
        super().__init__(20,.025)
        self._diet = Animal.eat_meat
        self._attacks = [Deer, Wolf]