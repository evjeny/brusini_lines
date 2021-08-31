import itertools
import numpy as np


def get_curve(
    alpha, beta, gamma, d_alpha, d_beta, d_gamma,
    begin: float = -40, end: float = 10, n_points: int = 100,
    n_coef_steps: int = 10
):
    xs = np.linspace(begin, end, n_points)

    m_y = lambda md: (alpha * md + beta * md ** 2 + gamma) if md < 0 else gamma
    ys = np.array([m_y(x) for x in xs])
    ys_min = np.array(ys)
    ys_max = np.array(ys)

    for ai, bi, gi in itertools.product(
        np.linspace(alpha - d_alpha, alpha + d_alpha, n_coef_steps),
        np.linspace(beta - d_beta, beta + d_beta, n_coef_steps),
        np.linspace(gamma - d_gamma, gamma + d_gamma, n_coef_steps)
    ):
        c_y = lambda md: (ai * md + bi * md ** 2 + gi) if md < 0 else gi
        ys_cur = np.array([c_y(x) for x in xs])

        ys_min = np.minimum(ys_min, ys_cur)
        ys_max = np.maximum(ys_max, ys_cur)

    return xs, ys, ys_min, ys_max


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
    
    curve_data = dict()

    for i in range(len(coefs)):
        xs, ys, ys_min, ys_max = get_curve(*coefs[i], *deltas[i])
        curve_data[f"{i}_xs"] = xs
        curve_data[f"{i}_ys"] = ys
        curve_data[f"{i}_ys_min"] = ys_min
        curve_data[f"{i}_ys_max"] = ys_max
    np.savez_compressed("brusini_curves.npz", **curve_data)


if __name__ == "__main__":
    main()
