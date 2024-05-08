from .action import Action


class RestAction(Action):
    def __init__(self, animal, grid):
        self._animal = animal
        self._current_grid = grid
        self._energy_cost = 0

    # skips spending energy and also skips aging
    def action(self):
        return
