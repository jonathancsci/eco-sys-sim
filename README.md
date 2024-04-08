# EcoSysSim

## UML
```mermaid
classDiagram
class Ecosystem {
    - _animals_list: list[str]
    - _fig: matplotlib.figure
    - _ax: matplotlib.axis
    - _plot: Plot
    - _environment: Environment

    + __init__(self) -> Ecosystem
    + run_simulation(self) -> None
    + step(self, max_iters) -> str
}
class Plot {
    - _ax: matplotlib.axis
    - _x_iters: list[int]
    - _y_populations: dict[str, deque[int]]
    - _plot_lines: dict[str, Line2D]

    + __init__(self, ax, animals_list) -> Display
    + update(self, curr_iter, animal_populations) -> None
}
class Environment {
    - _rows: int
    - _cols: int
    - _animals_list: list[str]
    - _observers: list[Plot]
    - _iter_counter: int
    - _obstacle_grid: list
    - _grid_map: dict[tuple, Grid]
    + iter_counter: @property

    + __init__(self, rows, cols, animals_list) -> Environment
    - _find_neighbors(self, grid_coords) -> list[tuple]
    - _create_obstacle_grid(self) -> list
    - _create_grid_map(self) -> dict[tuple, Grid]
    - _populate_grid_map(self) -> None
    + attach(self, new_observer) -> None
    - _notify_observers(self, animal_populations) -> None
    - count_animal_populations(self) -> dict[str, int]
    + step(self) -> None
    - _get_random_grid(self)
    - _get_grid(self, x, y)
}
class Grid {
    - _occupants: list[Animal]
    - _neighbors: list[Grid]
    - _grass_level: int
    + occupants: @property, @setter
    + neighbors: @property, @setter

    + __init__(self) -> Grid
    + step(self) -> None
    other methods() for animal behavior
}

class Animal {
    ...
}

class Bear {
    ...
}

class Deer {
    ...
}

class Fox {
    ...
}

class Rabbit {
    ...
}

class Wolf {
    ...
}

class Action {
    ...
}

class AttackAction {
    ...
}

class EatAction {
    ...
}

class GrazeAction {
    ...
}

class MoveAction {
    ...
}

class ReproduceAction {
    ...
}

Ecosystem *-- Plot
Ecosystem *-- Environment

Environment *-- Grid
Environment o-- Plot
Environment *-- Animal

Grid o-- Grid

Animal <|.. Action

Animal <|-- Bear
Animal <|-- Deer
Animal <|-- Fox
Animal <|-- Rabbit
Animal <|-- Wolf

Action <|-- AttackAction
Action <|-- EatAction
Action <|-- GrazeAction
Action <|-- MoveAction
Action <|-- ReproduceAction

```

## Set up the dev environment
1. Create a venv named 'venv'
```bash
python3 -m venv venv
```
2. Activate the venv
```bash
source venv/bin/activate
```
3. Install requirements.txt
```bash
pip install -r requirements.txt
```

## License
This software is licensed under the [`MIT-0`](https://github.com/aws/mit-0) license. The intent is to effectively place this work in the public domain.