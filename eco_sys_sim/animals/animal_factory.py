from .rabbit import Rabbit
from .animal import Animal
from .fox import Fox


class AnimalFactory:
    def createRabbit():
        return Rabbit()
