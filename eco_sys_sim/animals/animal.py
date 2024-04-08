from eco_sys_sim.actions.move_action import MoveAction
from eco_sys_sim.grid import Grid
from .rabbit import Rabbit
from .fox import Fox
import random

class Animal:
    #energy that is spent on acitons and must be regaained through food
    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, energy):
        self._energy = energy

    #size provides a higher chance of winning combat and is the baseline for energy gained from eating the animal, it may also factor into energy cost as well
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    #boolean value for whether an animal is alive
    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive

    #storage for current preferences
    @property
    def preferences(self):
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        self._preferences = preferences

    #full list of methods
    def step(self, room: Grid):
        self.preferences = dict.fromkeys(room.neighbors,0)
        self.preferences.update({room:0})
        for rm in self.preferences.keys():
            self.score_room(rm)
        target = max(self.preferences,key=self.preferences.get)
        return MoveAction(self,self.size*.1,room,target)

    def score_room(self, room: Grid):
        raise NotImplementedError
    
    def add_room_score(self,value,room):
        if room in self.preferences.keys():
            self.preferences[room] += value
                    
    def nutritional_value(self, room: Grid):
        return 2*self.size+self.energy
    
    def can_mate(self):
        return self.energy > 2*self.size
        
    def is_full(self):
        return self.energy > 3*self.size
    
    def dice_roll():
        return random.randint(1,7)
    