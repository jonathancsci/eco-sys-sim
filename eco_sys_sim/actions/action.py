import random


class Action:
    # acting animal
    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, animal):
        self._animal = animal

    # the energy cost of taking an action
    @property
    def energy_cost(self):
        return self._energy_cost

    @energy_cost.setter
    def energy_cost(self, energy_cost):
        self._energy_cost = energy_cost

    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    def execute(self):
        if self.animal.alive:
            self.animal.energy = self.animal.energy - self.energy_cost
            self.action()
        if self.animal.energy <= 0 or random.random() < self.animal.age:
            self.animal.alive = False
        self.animal.age_up()
        if self.animal.age > 3:
            self.current_grid.remove_occupant(self.animal)

    def action(self):
        raise NotImplementedError
