from .animal import Animal


class Rabbit(Animal):
    def __init__(self):
        super().__init__(2)
        self.diet = Animal.eat_grass
        self.fears = [Fox, Deer, Wolf, Bear]

class Fox(Animal):
    def __init__(self):
        super().__init__(3)
        self.diet = Animal.eat_meat
        self.attacks = [Rabbit]
        self.fears = [Wolf, Bear]

class Deer(Animal):
    def __init__(self):
        super().__init__(6,Animal.eat_grass)
        self.diet = Animal.eat_meat
        self.fears = [Wolf, Bear]
        self.fights_back = True
        self.herds = True

class Wolf(Animal):
    def __init__(self):
        super().__init__(5)
        self.diet = Animal.eat_meat
        self.attacks = [Fox, Deer]
        self.fears = [Bear]
        self.herds = True
        self.fights_back = True

class Bear(Animal):
    def __init__(self):
        super().__init__(10)
        self.diet = Animal.eat_meat
        self.attacks = [Deer, Wolf]