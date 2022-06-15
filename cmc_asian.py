from imports import *


def cmc_asian(s0, k, r, s, R, n):
    def S(t):
        return s0 * np.exp((r - s ** 2 / 2) * t + s * np.random.normal(0, t, 1))

    A = np.zeros(shape=(1, R))
    for j in range(R):
        Asum = 0
        for i in range(1, n + 1):
            Asum += S(i / n) / n
        A[0, j] = Asum
    return exp(-r) * (np.mean(np.maximum(A - k, 0)))
