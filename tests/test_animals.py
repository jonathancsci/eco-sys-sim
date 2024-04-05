from eco_sys_sim.animals.rabbit import Rabbit
from eco_sys_sim.animals.fox import Fox
from eco_sys_sim.animals.animal import Animal

class TestAnimals:
    def test_size(self):
        rabbit = Rabbit()
        fox = Fox()
        assert rabbit.size == 2
        assert fox.size == 3

    def test_nutritional_value(self):
        rabbit = Rabbit()
        fox = Fox()
        rabbit.energy = 3
        assert rabbit.nutritional_value() == 7
        assert fox.nutritional_value() == 6
    
    def test_can_mate(self):
        rabbit = Rabbit()
        fox = Fox()
        rabbit.energy = 4
        fox.energy = 4
        assert rabbit.can_mate()
        assert not fox.can_mate()

    def test_is_full(self):
        rabbit = Rabbit()
        fox = Fox()
        rabbit.energy = 6
        fox.energy = 6
        assert rabbit.is_full()
        assert not fox.is_full()
