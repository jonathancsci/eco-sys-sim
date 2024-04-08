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
        action = MoveAction(rabbit,.2,environment.get_grid(0,0),environment.get_grid(1,0))
        action.execute()
        assert environment.animal_at(rabbit,1,0)
        assert not environment.animal_at(rabbit,0,0)
        assert rabbit.energy == 2.8
    
    def test_attack(self):
        raise NotImplementedError
    
    def test_eat(self):
        raise NotImplementedError
    
    def test_graze(self):
        raise NotImplementedError
    
    def test_reproduce(self):
        raise NotImplementedError
