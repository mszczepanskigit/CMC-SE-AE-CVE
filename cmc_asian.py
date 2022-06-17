from imports import *


def cmc_asian(s0, k, r, s, R, n):
    """
    Crude Monte Carlo estimator of asian option with discounted payoff at time 1.
    :param s0: S(0) - fixed
    :param k: K - fixed
    :param r: r - fixed
    :param s: sigma - fixed
    :param R: total number of replications
    :param n: dimension
    :return: estimated value
    """
    def S(t):
        """
        Auxiliary function
        """
        return s0 * np.exp((r - s ** 2 / 2) * t + s * np.random.normal(0, t, 1))

    seed = 465726236011 % (2 ** 32 - 1)  # 6C 6F 72 65 6B
    np.random.seed(seed)
    A = np.zeros(shape=(1, R))
    for j in range(R):
        Asum = 0
        for i in range(1, n + 1):
            Asum += S(i / n) / n
        A[0, j] = Asum
    return exp(-r) * (np.mean(np.maximum(A - k, 0)))
