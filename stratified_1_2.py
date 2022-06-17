import numpy as np
from math import exp
from scipy.stats.distributions import chi2


def strat_prop2(s0, k, r, s, R, m, n):
    """
    :param s0: S(0) - fixed
    :param k: K - fixed
    :param r: r - fixed
    :param s: sigma - fixed
    :param R: total number of replications
    :param m: number of strata
    :param n: dimension
    :return: estimated value
    """
    np.random.seed(465726236011 % (2 ** 32 - 1))
    S = []
    for i in range(1, n + 1):
        s_temp = []
        for j in range(1, n + 1):
            s_temp.append(1 / n * min(i, j))
        S.append(s_temp)
    A = np.linalg.cholesky(S)
    Y = []
    for i in range(m):
        Z = np.zeros((n, int(R / m)))
        xyz = []
        norma = 0
        for j in range(n):
            xyz.append(np.random.normal(0, 1, int(R / m)))
            norma += xyz[j] ** 2
        norma = np.sqrt(norma)
        for j in range(n):
            xyz[j] = xyz[j] / norma
        v = np.random.uniform(0, 1, int(R / m))
        v = v / m + i / m
        D2 = np.sqrt(chi2.ppf(v, df=n))
        for j in range(n):
            xyz[j] = xyz[j] * D2
            Z[j, :] = xyz[j]
        B = np.dot(A, Z)
        est_s = []
        est_temp = np.zeros((1, int(R / m)))
        for g in range(n):
            est_s.append([s0 * np.exp((r - s ** 2 / 2) * (g + 1) / n + s * B[g, :])])
            est_temp += s0 * np.exp((r - s ** 2 / 2) * (g + 1) / n + s * B[g, :])
        # estimator for each strata
        Y.append(np.mean(np.maximum(1 / n * est_temp - k, 0)))

    return (exp(-r) * np.mean(Y))
