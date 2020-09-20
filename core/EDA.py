"""
Extensive Data Exploration
"""
import stumpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
from core.constants import Constant


def plot_neighbour(data, idx, neighbour_idx, rect_w):
    fig, axs = plt.subplots(len(idx), sharex=True, gridspec_kw={'hspace': 0})
    plt.suptitle('Motif (Pattern) Discovery', fontsize='30')

    for i in range(len(idx)):
        axs[i].plot(data[idx[i]: idx[i] + rect_w], color='C1')
        axs[i].plot(data[neighbour_idx[i]: neighbour_idx[i] + rect_w], color="C2")
        axs[i].set_ylabel(f'{i}', fontsize='20')


def matrix_profile(data, m, k):
    out = stumpy.stump(data, m)
    dists = out[:, 0]
    # sort dists in ascending order and get indices of n smallest items
    idx = np.argsort(dists)[:k]
    idx = sorted(idx)
    # data at close idx like 345 and 346 would look almost the same so we have to remove them
    correct_idx = [idx[0]]
    for i in range(1, len(idx)):
        if idx[i] - idx[i-1] < m:
            continue
        else:
            correct_idx.append(idx[i])

    # get nearest neighbour of those item in the matrix profile
    neighbour_idx = out[correct_idx, 1]
    plot_neighbour(data, correct_idx, neighbour_idx, m)
    plt.show()


def main(data):
    print(data.head())
    plt.plot(data["Open"][0:1000])
    plt.show()


if __name__ == '__main__':
    csv_data = pd.read_csv(Constant.EUR_USD_H1, usecols=["Open", "Close", "High", "Low", ])
    # main(csv_data)
    matrix_profile(csv_data['Open'][0:1000].to_numpy(), m=24, k=10)