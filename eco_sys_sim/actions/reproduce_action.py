from .action import Action


class ReproduceAction(Action):
    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    # offspring to be created
    @property
    def offpsring(self):
        return self._offpsring

    def __init__(self, animal, cost, current_grid, offspring):
        self._animal = animal
        self._energy_cost = cost
        self._current_grid = current_grid
        self._animal = animal

    def action(self):
        self.current_grid.add_animal(self.offspring)
        # important note: ask Jonathan if python has garbage collection, if not then there needs to be a way to delete the baby if the animal dies before taking their turn
