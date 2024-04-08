from eco_sys_sim.environment import Environment
from eco_sys_sim.animals.rabbit import Rabbit
from eco_sys_sim.animals.fox import Fox
from eco_sys_sim.animals.animal import Animal
from eco_sys_sim.actions.action import Action
from eco_sys_sim.actions.attack_action import AttackAction
from eco_sys_sim.actions.eat_action import EatAction
from eco_sys_sim.actions.graze_action import GrazeAction
from eco_sys_sim.actions.move_action import MoveAction
from eco_sys_sim.actions.reproduce_action import ReproduceAction


class TestAnimals:
    def test_move(self):
        environment = Environment(rows=2, cols=1)
        rabbit = Rabbit()
        environment.add_animal_at(rabbit,0,0)
        print(environment._grid_map.keys())
        action = MoveAction(rabbit,.2,environment.get_grid(0,0),environment.get_grid(1,0))
        action.execute()
        assert environment.animal_at(rabbit,1,0)
        assert not environment.animal_at(rabbit,0,0)
        assert rabbit.energy == 2.8
    
    def test_attack(self):
        fox = Fox()
        rabbit = Rabbit()
        action = AttackAction(fox,1,rabbit)
        action.execute()
        action.execute()
        action.execute()
        action.execute()
        action.execute()
        action.execute()
        action.execute()
        action.execute()
        action.execute()
        action.execute()
        assert not rabbit.alive
    
    def test_eat(self):
        environment = Environment(rows=1, cols=1)
        fox = Fox()
        rabbit = Rabbit()
        environment.add_animal_at(fox,0,0)
        environment.add_animal_at(rabbit,0,0)
        rabbit.alive = False
        print(environment._grid_map.keys())
        action = EatAction(fox,rabbit,environment.get_grid(0,0))
        action.execute()
        assert environment.animal_at(fox,0,0)
        assert not environment.animal_at(rabbit,0,0)
        assert fox.energy == 11.5
    
    def test_graze(self):
        environment = Environment(rows=1, cols=1)
        rabbit = Rabbit()
        environment.add_animal_at(rabbit,0,0)
        action = GrazeAction(rabbit,environment.get_grid(0,0))
        action.execute()
        assert rabbit.energy == 9
        assert environment.get_grid(0,0).grass_level == 6
    
    def test_reproduce(self):
        environment = Environment(rows=2, cols=1)
        rabbit1 = Rabbit()
        rabbit2 = Rabbit()
        print(environment._grid_map.keys())
        environment.add_animal_at(rabbit1,0,0)
        rabbit1.energy = 6
        environment.add_animal_at(rabbit2,0,0)
        action = ReproduceAction(rabbit1,4,rabbit2,environment.get_grid(0,0),Rabbit)
        action.execute()
        assert len(environment.get_grid(0,0).occupants) > 2
        assert rabbit1.energy == 2
