from . import Action


class ReproduceAction(Action):
    #current room
    @property
    def current_room(self):
        return self._current_room

    def __init__(self,animal,cost,current_room,offspring):
        self._animal = animal
        self._energy_cost = cost
        self._current_room = current_room
        self._animal = animal

    def action(self):
        graze = self.current_room.grass_level/2
        self.animal.energy += graze
        self.current_room.grass_level -= graze