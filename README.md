# EcoSysSim

## UML
```mermaid
classDiagram
class Ecosystem {
    - _fig: matplotlib.figure
    - _ax: matplotlib.axis
    - _display: Display
    - _enviroment: Enviroment
    + enviroment: @property

    + __init__(self) -> Ecosystem
    + run_simulation(self) -> None
}
class Display {
    - _ax: matplotlib.axis
    - _x_array: np.ndarray
    - _y_array: np.ndarray
    + ax: @property
    + x_array: @property, @setter
    + y_array: @property, @setter

    __init__(self, ax) -> Display
    update(self) -> None
}
class Enviroment {
    - _rows: int
    - _cols: int
    - _obstacle_grid: list
    - _grid_map: dict[tuple, Grid]
    - _observers: list
    + rows: @property
    + cols: @property
    + obstacle_grid: @property
    + grid_map: @property
    + observers: @property, @setter

    + __init__(self, rows, cols) -> Enviroment
    - _find_neighbors(self, grid_coords) -> list[tuple]
    - _create_obstacle_grid(self) -> list
    - _create_grid_map(self) -> dict[tuple, Grid]
    - _populate_enviroment(self) -> None
    + step(self) -> None
    + count_animals(self) -> dict[str, int]
    + attach(self, observer) -> None
    - _notify_observers(self) -> None
}
class Grid {
    - _occupants: list[Animal]
    - _plant_food_level: int
    - _neighbors: list[Grid]
    + occupants: @property, @setter
    + plant_food_level: @property, @setter
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