class Grid:
    def __init__(self):
        self._occupants: list = list()
        self._neighbors: list[Grid] = list()
        self._grass_level: int = 50

    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors_list):
        self._neighbors = neighbors_list
