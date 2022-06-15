import numpy as np
import random as rand
from math import log, exp
from scipy.stats import norm


def ant(s0, k, r, s, R):
    z = np.random.normal(0, 1, int(R))
    z[np.arange(1, R + 1, 2)] = -z[np.arange(0, R, 2)]
    mu = r - s ** 2 / 2
    return np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0))


print(ant(100, 100, 0.05, 0.25, 10000))


def ant2(s0, k, r, s, R):
    u = np.random.uniform(0, 1, int(R))
    u[np.arange(1, R + 1, 2)] = 1 - u[np.arange(0, R, 2)]
    z = norm.ppf(u)
    mu = r - s ** 2 / 2
    return np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0))


print(ant2(100, 100, 0.05, 0.25, 10000))
