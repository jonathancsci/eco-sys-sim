import random
import matplotlib.pyplot as plt
from eco_sys_sim.plot import Plot


class TestPlot:
    @classmethod
    def setup_class(cls):
        cls.plot = Plot()
        cls.animals_list: list[str] = ["bear", "wolf", "fox", "deer", "rabbit"]

    def test_update(self):
        dummy_data = {animal: random.randint(0, 9) for animal in self.animals_list}
        self.plot.update(0, dummy_data)
        plt.close('all')
