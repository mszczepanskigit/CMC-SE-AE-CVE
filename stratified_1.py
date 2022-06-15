import numpy as np
import random as rand
from math import log, exp
from scipy.stats import norm


def strat_prop(s0, k, r, s, R, m):
    """
    :param s0: S(0) - fixed
    :param k: K - fixed
    :param r: r - fixed
    :param s: sigma - fixed
    :param R: total number of replications
    :param m: number of strata
    :return: estimated value
    """
    V = []
    for i in range(m):
        u = np.random.uniform(0, 1, int(R / m))
        V = np.concatenate((V, (i / m + 1 / m * u)))
    z = norm.ppf(V)
    mu = r - s ** 2 / 2
    return np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0))


print(strat_prop(100, 100, 0.05, 0.25, 10000, 10))
