import numpy as np
from math import exp, sqrt
from scipy.stats.distributions import chi2


def strat_opt2(s0, k, r, s, R, m, n, R_prim):
    S = []
    for i in range(1, n + 1):
        s_temp = []
        for j in range(1, n + 1):
            s_temp.append(1 / n * min(i, j))
        S.append(s_temp)
    A = np.linalg.cholesky(S)
    B_variance = []
    # pilot replications in order to estimate variance in each strata
    for i in range(m):
        Z = np.zeros((n, int(R_prim / m)))
        xyz = []
        norma = 0
        for j in range(n):
            xyz.append(np.random.normal(0, 1, int(R_prim / m)))
            norma += xyz[j] ** 2
        norma = np.sqrt(norma)
        for j in range(n):
            xyz[j] = xyz[j] / norma
        v = np.random.uniform(0, 1, int(R_prim / m))
        v = v / m + i / m
        D2 = np.sqrt(chi2.ppf(v, df=n))
        for j in range(n):
            xyz[j] = xyz[j] * D2
            Z[j, :] = xyz[j]
        B = np.dot(A, Z)
        B_variance.append(sqrt(np.var(B)))
    B_variance = np.array(B_variance)
    # number of actual replications for each strata
    R_j = np.floor((1 / m * B_variance) / sum(1 / m * B_variance) * R)
    if np.sum(R_j) != R:
        R_j[-1] = R_j[-1] + (R - np.sum(R_j))
    Y = []
    for i in range(m):
        Z = np.zeros((n, int(R_j[i])))
        xyz = []
        norma = 0
        for j in range(n):
            xyz.append(np.random.normal(0, 1, int(R_j[i])))
            norma += xyz[j] ** 2
        norma = np.sqrt(norma)
        for j in range(n):
            xyz[j] = xyz[j] / norma
        v = np.random.uniform(0, 1, int(R_j[i]))
        v = v / m + i / m
        D2 = np.sqrt(chi2.ppf(v, df=n))
        for j in range(n):
            xyz[j] = xyz[j] * D2
            Z[j, :] = xyz[j]
        B = np.dot(A, Z)
        est_s = []
        est_temp = np.zeros((1, int(R_j[i])))
        for g in range(n):
            est_s.append([s0 * np.exp((r - s ** 2 / 2) * (g + 1) / n + s * B[g, :])])
            est_temp += s0 * np.exp((r - s ** 2 / 2) * (g + 1) / n + s * B[g, :])
            # estimator for each strata
        Y.append(np.mean(np.maximum(1 / n * est_temp - k, 0)))

    print(exp(-r) * np.mean(Y))

# np.random.seed(1)
# strat_opt2(100, 100, 0.05, 0.25, 1000, 4, 3, 100)
# np.random.seed(465726236011 % (2 ** 32 - 1))
# strat_opt2(100, 100, 0.05, 0.25, 10000, 4, 2, 100)
# strat_opt2(100, 100, 0.05, 0.25, 10000, 4, 3, 100)
# strat_opt2(100, 100, 0.05, 0.25, 10000, 4, 17, 100)
# strat_opt2(100, 100, 0.05, 0.25, 10000, 10, 2, 100)
# strat_opt2(100, 100, 0.05, 0.25, 10000, 10, 3, 100)
# strat_opt2(100, 100, 0.05, 0.25, 10000, 10, 17, 100)
#
# strat_opt2(100, 100, 0.05, 0.25, 1000000, 4, 2, 1000)
# strat_opt2(100, 100, 0.05, 0.25, 1000000, 4, 3, 1000)
# strat_opt2(100, 100, 0.05, 0.25, 1000000, 4, 17, 1000)
# strat_opt2(100, 100, 0.05, 0.25, 1000000, 10, 2, 1000)
# strat_opt2(100, 100, 0.05, 0.25, 1000000, 10, 3, 1000)
# strat_opt2(100, 100, 0.05, 0.25, 1000000, 10, 17, 1000)
