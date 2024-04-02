import numpy as np
import matplotlib.pyplot as plt
from .environment import Environment


def main():
    Z = np.random.rand(6, 10)
    x = np.arange(-0.5, 10, 1)
    y = np.arange(4.5, 11, 1)

    # fig, ax = plt.subplots()
    # ax.pcolormesh(x, y, Z)
    # plt.show()

    enviroment = Environment(rows=5, cols=10)
    print(enviroment._obstacle_grid)
    print(enviroment._find_neighbors((0,0)))
    print(enviroment._grid_map[(0, 0)].neighbors)
    for neighbor in enviroment._find_neighbors((0, 0)):
        print(enviroment._grid_map[neighbor])



if __name__ == "__main__":
    main()
