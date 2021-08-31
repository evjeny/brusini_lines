import matplotlib.pyplot as plt
import numpy as np


def display(
    ax, xs, ys, ys_min, ys_max
):
    ax.plot(xs, ys, c="k")
    ax.fill_between(xs, ys_min, ys_max, color="r", alpha=0.3)


def main():
    # alpha, beta, gamma
    coefs = [
        [-0.225, -0.541, 1.934],
        [-0.029, -0.276, 2.965],
        [-0.080, -0.184, 4.775],
        [-0.129, -0.100, 8.084],
        [-0.280, -0.074, 13.147],
        [-0.283, -0.067, 24.372]
    ]

    # d_alpha, d_beta, d_gamma
    deltas = [
        [0.142, 0.071, 0.041],
        [0.219, 0.062, 0.141],
        [0.199, 0.040, 0.181],
        [0.118, 0.012, 0.191],
        [0.108, 0.007, 0.256],
        [0.114, 0.005, 0.444]
    ]

    fig, ax = plt.subplots(1, figsize=(10, 10))
    
    ax.set_xlim((5, -30))
    ax.set_ylim((0, 20))
    ax.invert_yaxis()
    
    curve_data = np.load("brusini_curves.npz")

    for i in range(len(coefs)):
        xs = curve_data[f"{i}_xs"]
        ys = curve_data[f"{i}_ys"]
        ys_min = curve_data[f"{i}_ys_min"]
        ys_max = curve_data[f"{i}_ys_max"]
        display(ax, xs, ys, ys_min, ys_max)
    plt.show()


if __name__ == "__main__":
    main()
