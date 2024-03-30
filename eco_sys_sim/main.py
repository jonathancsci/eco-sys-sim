import numpy as np
import matplotlib.pyplot as plt

def main():
    Z = np.random.rand(6, 10)
    x = np.arange(-0.5, 10, 1)
    y = np.arange(4.5, 11, 1)

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, Z)
    plt.show()

if __name__ == '__main__':
    main()

