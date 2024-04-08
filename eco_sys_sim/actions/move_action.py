from . import Action


class MoveAction(Action):
    # current room
    @property
    def current_room(self):
        return self._current_room

    # target room
    @property
    def target_room(self):
        return self._target_room

    def __init__(self, animal, cost, current_room, target_room):
        self._animal = animal
        self._energy_cost = cost
        self._current_room = current_room
        self._target_room = target_room

    def action(self):
        self.target_room.add_animal(self.animal)
        self.current_room.remove_animal(self.animal)
