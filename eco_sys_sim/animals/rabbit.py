from .animal import Animal

class Rabbit(Animal):
    def __init__(self):
        self.size = 2

    def score_room(self, room):
        for o in room.occupants:
            if(type(o) != Rabbit):
                self.add_room_score(-100,room)
                for rm in room.neighbors:
                    self.add_room_score(-30,room)
            elif(self.can_mate()):
                self.add_room_score(10)
        self.add_room_score(room.grass_level,room)
        self.add_room_score(self.dice_roll,room)