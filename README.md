# EcoSysSim

## UML
```mermaid
classDiagram
class Ecosystem {
    - _fig: matplotlib.figure
    - _ax: matplotlib.axis
    - _plot: Plot
    - _environment: Environment

    + __init__(self) -> Ecosystem
    + run_simulation(self) -> None
}
class Plot {
    - _ax: matplotlib.axis
    - _x_list: list
    - _y_lists: list

    __init__(self, ax) -> Display
    update(self) -> None
}
class Environment {
    - _rows: int
    - _cols: int
    - _obstacle_grid: list
    - _grid_map: dict[tuple, Grid]
    - _observers: list

    + __init__(self, rows, cols) -> Environment
    - _find_neighbors(self, grid_coords) -> list[tuple]
    - _create_obstacle_grid(self) -> list
    - _create_grid_map(self) -> dict[tuple, Grid]
    - _populate_grid_map(self) -> None
    + attach(self, observer) -> None
    - _notify_observers(self) -> None
    + step(self) -> None
    + count_animals(self) -> dict[str, int]
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