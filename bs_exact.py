from imports import *


def bs_exact(s0, k, r, s):
    """
    Formula which allows to compute exact value of 'option' with discounted payoff at time 1.
    :param s0: S(0) - fixed
    :param k: K - fixed
    :param r: r - fixed
    :param s: sigma - fixed
    :return: exact value of Black-Scholes formula
    """
    d1 = 1/s * (log(s0/k)+r+s**2/2)
    d2 = d1 - s
    return s0 * norm.cdf(d1)-k*exp(-r)*norm.cdf(d2)
