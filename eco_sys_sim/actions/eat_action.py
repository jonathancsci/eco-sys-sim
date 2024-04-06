from . import Action


class EatAction(Action):
    #current room
    @property
    def current_room(self):
        return self._current_room

    #target animal to eat
    @property
    def target(self):
        return self._target

    def __init__(self,animal,cost,target):
        self._animal = animal
        self._energy_cost = cost
        self._target = target

    def action(self):
        self.animal.energy += self.target.nutritional_value()
        self.current_room.remove_animal(self.target)