import numpy as np
import random as rand
from math import log, exp, sqrt
from scipy.stats import norm
from stratified_1 import strat_prop


def strat_opt(s0, k, r, s, R, m):
    # pilot simulations for estimating variance in each strata
    R_prim = 1000
    est_s = []
    for i in range(m):
        V = []
        u = np.random.uniform(0, 1, int(R_prim / m))
        V = np.concatenate((V, (i / m + 1 / m * u)))
        z = norm.ppf(V)
        mu = r - s ** 2 / 2
        y_strat = np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0))
        # estimated variance in one strata
        est_s.append(sqrt(1 / (int(R_prim / m) - 1) * sum(np.power(z - y_strat, 2))))
        # albo powinno byc: est_s.append(sqrt(1 / (int(R_prim / m) - 1) * sum(np.power(z - mean(z), 2))))
    R_j = np.ceil((1 / m) * np.array(est_s) / sum((1 / m) * np.array(est_s) ) * R)
    Y_est = []
    for i in range(m):
        V = []
        u = np.random.uniform(0, 1, int(R_j[i]))
        V = np.concatenate((V, (i / m + 1 / m * u)))
        z = norm.ppf(V)
        mu = r - s ** 2 / 2
        # estymator z kazdej warstwy
        Y_est.append(np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0)))
    return np.mean(Y_est)

print(strat_opt(100, 100, 0.05, 0.25, 10000, 10))
