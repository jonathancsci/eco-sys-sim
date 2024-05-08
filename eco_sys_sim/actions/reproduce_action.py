from .action import Action


class ReproduceAction(Action):
    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    # offspring to be created
    @property
    def mate(self):
        return self._mate

    # offspring to be created
    @property
    def offspring(self):
        return self._offspring

    def __init__(self, animal, cost, mate, current_grid, offspring):
        self._animal = animal
        self._energy_cost = cost
        self._current_grid = current_grid
        self._mate = mate
        self._offspring = offspring

    def action(self):
        if self.mate.alive and self.mate in self.current_grid.occupants:
            self.current_grid.add_occupant(self.offspring())


class RabbitReproduceAction(ReproduceAction):
    def action(self):
        if self.mate.alive and self.mate in self.current_grid.occupants:
            self.current_grid.add_occupant(self.offspring())
            self.current_grid.add_occupant(self.offspring())
