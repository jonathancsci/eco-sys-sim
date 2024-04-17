from .action import Action


class RestAction(Action):
    # current grid
    @property
    def current_grid(self):
        return self._current_grid

    def __init__(self, animal):
        self._animal = animal
        self._energy_cost = 0

    #skips spending energy and also skips aging
    def execute(self):
        return
