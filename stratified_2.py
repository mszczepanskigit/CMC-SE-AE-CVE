import numpy as np
from math import exp, sqrt
from scipy.stats import norm


def strat_opt(s0, k, r, s, R, m, R_prim):
    """
       :param s0: S(0) - fixed
       :param k: K - fixed
       :param r: r - fixed
       :param s: sigma - fixed
       :param R: total number of replications
       :param m: number of strata
       :param R_prim: number of pilot replications
       :return: estimated value
    """
    np.random.seed(465726236011%(2**32-1))
    # pilot simulations for estimating variance in each strata
    est_s = []
    for i in range(m):
        V = []
        u = np.random.uniform(0, 1, int(R_prim / m))
        V = np.concatenate((V, (i / m + 1 / m * u)))
        z = norm.ppf(V)
        # estimated variance in one strata
        est_s.append(sqrt(np.var(z)))
    # number of actual replications for each strata
    R_j = np.round((1 / m) * np.array(est_s) / sum((1 / m) * np.array(est_s)) * R, 0)
    Y_est = []
    for i in range(m):
        V = []
        u = np.random.uniform(0, 1, int(R_j[i]))
        V = np.concatenate((V, (i / m + 1 / m * u)))
        z = norm.ppf(V)
        mu = r - s ** 2 / 2
        # estimator for each strata
        Y_est.append(np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0)))
    return exp(-r) * np.mean(Y_est)

