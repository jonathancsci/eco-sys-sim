from .animal import Animal

class Rabbit(Animal):
    def __init__(self):
        self.size = 2
        self.fears = [Fox]

    def score_room(self, room):
        return room.grass_level