from imports import *


def bs_exact(s0, k, r, s):
    d1 = 1/s * (log(s0/k)+r+s**2/2)
    d2 = d1 - s
    return s0 * norm.cdf(d1)-k*exp(-r)*norm.cdf(d2)
