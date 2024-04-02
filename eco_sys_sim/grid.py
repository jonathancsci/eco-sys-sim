class Grid:
    def __init__(self):
        self._neighbors = list()

    @property
    def neighbors(self):
        return self._neighbors
    
    @neighbors.setter
    def neighbors(self, neighbors_list):
        self._neighbors = neighbors_list