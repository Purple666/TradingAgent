import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2020)


def create_random_walk(size=100, start=None):
    x = np.random.choice([-1,1], size=size, replace=True) # Sample with replacement from (-1, 1)
    if start is not None:
        return np.cumsum(np.hstack((start, x)))
    return np.cumsum(x) # Return the cumulative sum of the elements


def draw_output():
    x_input = np.arange(50)
    x_pred = np.arange(49, 100)
    y_input = create_random_walk(size=50)
    y_pred1 = create_random_walk(size=50, start=y_input[-1])
    y_pred2 = create_random_walk(size=50, start=y_input[-1])
    y_pred3 = create_random_walk(size=50, start=y_input[-1])

    plt.plot(x_input, y_input)
    plt.plot(x_pred, y_pred1)
    plt.plot(x_pred, y_pred2)
    plt.plot(x_pred, y_pred3)

    plt.show()


if __name__ == '__main__':
    draw_output()