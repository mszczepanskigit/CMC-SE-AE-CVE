from imports import *


def cmc_european(s0, k, r, s, R):
    z = np.random.normal(0, 1, R)
    mu = r - s ** 2 / 2
    return exp(-r)*(np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0)))
