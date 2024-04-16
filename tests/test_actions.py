from eco_sys_sim.grid import Grid
from eco_sys_sim.animals.concrete_animals import Rabbit
from eco_sys_sim.animals.concrete_animals import Fox
from eco_sys_sim.animals.animal import Animal
from eco_sys_sim.actions.action import Action
from eco_sys_sim.actions.attack_action import AttackAction
from eco_sys_sim.actions.eat_action import EatAction
from eco_sys_sim.actions.graze_action import GrazeAction
from eco_sys_sim.actions.move_action import MoveAction
from eco_sys_sim.actions.reproduce_action import ReproduceAction
from eco_sys_sim.actions.rest_action import RestAction


class TestActions:
    def test_move(self):
        grid1 = Grid()
        grid2 = Grid()
        rabbit = Rabbit()
        grid1.add_occupant(rabbit)
        action = MoveAction(rabbit, 0.2, grid1, grid2)
        action.execute()
        assert rabbit in grid2.occupants
        assert not rabbit in grid1.occupants
        assert rabbit.energy == 2.8

    def test_attack(self):
        fox = Fox()
        rabbit = Rabbit()
        action = AttackAction(fox, 1, rabbit)
        while(rabbit.alive):
            action.execute()
            fox.energy = 20
        assert not rabbit.alive

    def test_eat(self):
        grid = Grid()
        fox = Fox()
        rabbit = Rabbit()
        grid.add_occupant(fox)
        grid.add_occupant(rabbit)
        rabbit.alive = False
        action = EatAction(fox, rabbit, grid)
        action.execute()
        assert fox in grid.occupants
        assert not rabbit in grid.occupants
        assert fox.energy == 11.5

    def test_graze(self):
        grid = Grid()
        rabbit = Rabbit()
        grid.add_occupant(rabbit)
        action = GrazeAction(rabbit, grid)
        action.execute()
        assert rabbit.energy == 5
        assert grid.grass_level == 10

    def test_reproduce(self):
        grid = Grid()
        rabbit1 = Rabbit()
        rabbit2 = Rabbit()
        grid.add_occupant(rabbit1)
        rabbit1.energy = 6
        grid.add_occupant(rabbit2)
        action = ReproduceAction(rabbit1, 4, rabbit2, grid, Rabbit)
        action.execute()
        assert len(grid.occupants) > 2
        assert rabbit1.energy == 2

    def test_rest(self):
        rabbit = Rabbit()
        action = RestAction(rabbit)
        action.execute()
        action.execute()
        action.execute()
        assert rabbit.energy == 3

    def test_starvation(self):
        fox = Fox()
        rabbit = Rabbit()
        fox.energy = .1
        action = AttackAction(fox, 1, rabbit)
        action.execute()
        assert not fox.alive