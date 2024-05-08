from eco_sys_sim.animals.concrete_animals import Rabbit
from eco_sys_sim.animals.concrete_animals import Fox
from eco_sys_sim.animals.concrete_animals import Bear
from eco_sys_sim.animals.concrete_animals import Deer
from eco_sys_sim.animals.concrete_animals import Wolf
from eco_sys_sim.animals.animal import Animal
from eco_sys_sim.grid import Grid


class TestAnimals:
    def simple_choice_area(self):
        area = [Grid()]
        for i in range(1, 3):
            area.append(Grid())
            area[i].neighbors.append(area[i - 1])
            area[i - 1].neighbors.append(area[i])
        return area

    def test_size(self):
        rabbit = Rabbit()
        fox = Fox()
        assert rabbit.size == 2
        assert fox.size == 3

    def test_nutritional_value(self):
        rabbit = Rabbit()
        fox = Fox()
        wolf = Wolf()
        deer = Deer()
        bear = Bear()
        rabbit.energy = 3
        assert rabbit.nutritional_value() == 5
        assert fox.nutritional_value() == 6
        assert wolf.nutritional_value() == 12
        assert deer.nutritional_value() == 10
        assert bear.nutritional_value() == 24

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

    def test_fighting(self):
        area = self.simple_choice_area()
        deer = Deer()
        wolf = Wolf()
        area[1].add_occupant(deer)
        area[1].add_occupant(wolf)
        action = wolf.step(area[1])
        action.execute()
        assert wolf in area[1].occupants
        while deer.alive:
            action.execute()
            wolf.energy = 20
        assert not deer.alive

    def test_fleeing(self):
        area = self.simple_choice_area()
        rabbit = Rabbit()
        fox = Fox()
        bear = Bear()
        area[0].add_occupant(rabbit)
        area[0].add_occupant(fox)
        area[0].add_occupant(bear)
        action1 = fox.step(area[0])
        action2 = rabbit.step(area[0])
        action1.execute()
        action2.execute()
        assert fox in area[1].occupants
        assert rabbit in area[1].occupants
        action = rabbit.step(area[1])
        action.execute()
        assert rabbit in area[2].occupants

    def test_feeding(self):
        # setup
        area = self.simple_choice_area()
        area[1].grass_level = 0
        area[2].grass_level = 0
        area[0].grass_level = 20
        deer = Deer()
        area[1].add_occupant(deer)
        # deer approaches grass
        action = deer.step(area[1])
        action.execute()
        assert deer in area[0].occupants
        # deer grazes
        action = deer.step(area[0])
        action.execute()
        assert deer.energy == 9.75
        # bear approaches deer
        bear = Bear()
        area[1].add_occupant(bear)
        action = bear.step(area[1])
        action.execute()
        assert bear in area[0].occupants
        # bear kills deer
        action = bear.step(area[0])
        while deer.alive:
            action.execute()
            bear.energy = 20
        # bear eats deer
        bearergy = bear.energy
        action = bear.step(area[0])
        action.execute()
        assert not deer in area[0].occupants
        assert bear.energy == bearergy + deer.nutritional_value()

    def test_mating(self):
        # setup
        area = self.simple_choice_area()
        fox1 = Fox()
        fox2 = Fox()
        area[1].add_occupant(fox1)
        area[0].add_occupant(fox2)
        fox1.energy = 30
        fox2.energy = 30
        # fox approaches mate
        action = fox1.step(area[1])
        action.execute()
        assert fox1 in area[0].occupants
        # fox mates
        action = fox1.step(area[0])
        action.execute()
        assert len(area[0].occupants) == 3
        # fox is tired
        fox1.energy = 2
        action = fox1.step(area[0])
        action.execute()
        assert len(area[0].occupants) + len(area[1].occupants) == 3
