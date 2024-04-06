from .animal import Animal
from .animal import Rabbit

class Fox(Animal):
    def __init__(self):
        self.size = 3
    
    def score_room(self, room):
        for o in room.occupants:
            if(type(o) == Rabbit):
                self.add_room_score(o.nutritional_value,room)
            elif(self.can_mate() and type(o) == Fox):
                self.add_room_score(10)
        self.add_room_score(self.dice_roll,room)