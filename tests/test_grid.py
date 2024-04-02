from eco_sys_sim.grid import Grid

class TestGrid:
    @classmethod
    def setup_class(cls):
        cls.instance = Grid()

    def test_constructor(self):
        assert isinstance(self.instance._occupants, list)
        assert isinstance(self.instance._neighbors, list)
        assert self.instance._grass_level == 50
