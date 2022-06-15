from imports import *


def ant_european(s0, k, r, s, R):
    z = np.random.normal(0, 1, int(R))
    z[np.arange(1, R + 1, 2)] = -z[np.arange(0, R, 2)]
    mu = r - s ** 2 / 2
    return exp(-r) * np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0))
