from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from math import log, exp
from scipy.stats.distributions import chi2


def strat_prop2(s0, k, r, s, R, m, n):
    S = []
    for i in range(1, m):
        s_temp = []
        for j in range(1, m):
            s_temp.append(1 / n * min(i, j))
        S.append(s_temp)
    A = np.linalg.cholesky(S)
    Z = np.zeros((n, R))
    Y = []
    for i in range(m):
        xyz = []
        # punkty
        norma = 0
        for j in range(n):
            xyz.append(np.random.normal(0, 1, R))
            norma += xyz[j] ** 2
        norma = np.sqrt(norma)
        for j in range(n):
            xyz[j] = xyz[j] / norma
        # promien
        v = np.random.uniform(0, 1, R)
        v = v / m + i / m
        D2 = np.sqrt(chi2.ppf(v, df=n))
        for j in range(n):
            xyz[j] = xyz[j] * D2
            Z[j, :] = xyz[j]
        B = np.dot(A, Z)
        # wyliczamy estymatory
        est_s = []
        est_temp = np.zeros((1, R))
        for g in range(n):
            est_s.append([s0 * np.exp((r - s ** 2 / 2) * (g + 1) / n + s * B[g, :])])
            est_temp += s0 * np.exp((r - s ** 2 / 2) * (g + 1) / n + s * B[g, :])
        # estymacja w danej warstwie
        Y.append(np.mean(np.maximum(1 / n * est_temp - k, 0)))

    print(exp(-r) * np.mean(Y))

strat_prop2(100, 100, 0.05, 0.25, 1000, 4, 3)
