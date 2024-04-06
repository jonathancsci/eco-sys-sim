class Action:
    #acting animal
    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, animal):
        self._animal = animal

    #the energy cost of taking an action
    @property
    def energy_cost(self):
        return self._energy_cost

    @energy_cost.setter
    def energy_cost(self, energy_cost):
        self._energy_cost = energy_cost
    
    def execute(self):
        if(self.animal.alive and self.animal.energy > energy_cost):
            self.animal.energy -= self.energy_cost
            self.action()
        
    def action(self):
        raise NotImplementedError