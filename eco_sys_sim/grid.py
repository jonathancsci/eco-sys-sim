class Grid:
    def __init__(self):
        self._occupants: list = list()
        self._neighbors: list[Grid] = list()
        self._grass_level: int = 12

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
        self._grass_level = grass_level

    def step(self):
        # TODO
        pass
