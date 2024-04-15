from .animal import Animal


class Wolf(Animal):
    def __init__(self):
        super().__init__(5,Animal.eat_meat)
