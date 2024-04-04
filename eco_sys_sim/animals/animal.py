from eco_sys_sim.actions import *
from .animal import *
from eco_sys_sim.grid import Grid

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

    #list of predators the animal fears
    @property
    def fears(self):
        return self._fears

    @fears.setter
    def fears(self, fears):
        self._fears = fears

    #list of food sources the animal approaches
    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, likes):
        self._likes = likes

    #full list of methods
    def __init__(self):
        self.fears = []
        self.likes = []

    def turn(self, room: Grid):
        room_blacklist = self.check_for_fears(room)
        room_preference = self.check_for_food(room)
        raise NotImplementedError
                             
    def nutritional_value(self, room: Grid):
        return 2*self.size+self.energy
    
    def can_mate(self):
        return self.energy > 2*self.size
        
    def is_full(self):
        return self.energy > 3*self.size
    
    def check_for_fears(self, room: Grid):
        blacklist = []
        for rm in room.neighbors:
            for o in rm.occupants:
                if o in self.fears:
                    blacklist.append(rm.neighbors)
        return blacklist
    
    def check_for_food(self, room: Grid):
        target_room = room
        high_score = self.score_room(room)
        for rm in room.neighbors:
            score = self.score_room(rm)
            if(score > high_score):
                target_room = rm
                high_score = score

    def score_room(self, room: Grid):
        raise NotImplementedError
    
    def look_for_grass(self, room:Grid):
        return room.grass_level

    def look_for_prey(self, room:Grid):
        score = 0
        for o in room.occupants:
            if(o in self.likes):
                score += o.nutritional_value
        return score