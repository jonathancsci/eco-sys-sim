import operator


class Grid:
    def __init__(self):
        self._occupants: list = list()
        self._neighbors: list[Grid] = list()
        self._grass_level: int = 8

    @property
    def occupants(self):
        return self._occupants

    @occupants.setter
    def occupants(self, occupants_list):
        self._occupants = occupants_list

    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors_list):
        self._neighbors = neighbors_list

    @property
    def grass_level(self):
        return self._grass_level

    @grass_level.setter
    def grass_level(self, grass_level):
        self._grass_level = max(grass_level,12)

    def add_occupant(self, occupant):
        self._occupants.append(occupant)

    def remove_occupant(self, occupant):
        if occupant in self._occupants:
            self._occupants.remove(occupant)

    def step(self):
        fertelizer_bonus = 0
        actions = []
        self.occupants.sort(key=operator.attrgetter('size'))
        for o in self.occupants:
            actions.append(o.step(self))
            if not o.alive:
                fertelizer_bonus = 1
        self.grass_level += 2+fertelizer_bonus
        return actions
