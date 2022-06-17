import numpy as np
from math import exp
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
    return exp(-r) * np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0))

# np.random.seed(465726236011%(2**32-1))
# print(strat_prop(100, 100, 0.05, 0.25, 10000, 5))
# print(strat_prop(100, 100, 0.05, 0.25, 10000, 10))
# print(strat_prop(100, 100, 0.05, 0.25, 1000000, 5))
# print(strat_prop(100, 100, 0.05, 0.25, 1000000, 10))
# print(strat_prop(100, 100, 0.05, 0.25, 1000000, 50))

# print(12.432924551914493-12.335998930368717)
# print(12.309166576604726-12.335998930368717)
# print(12.325245252392454-12.335998930368717)
# print(12.330875153077235-12.335998930368717)
# print(12.337363600936357-12.335998930368717)
