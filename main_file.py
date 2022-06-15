from imports import *

if __name__ == "__main__":
    np.random.seed(465726236011 % (2**32 - 1))  # 6C 6F 72 65 6B
    bs = bs_exact(s0=100, k=100, r=0.05, s=0.25)
    cmc_eu = cmc_european(s0=100, k=100, r=0.05, s=0.25, R=10000)
    cmc_as_2 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=10000, n=2)
    cmc_as_3 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=10000, n=3)
    cmc_as_17 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=10000, n=17)
    ant_eu = ant_european(s0=100, k=100, r=0.05, s=0.25, R=10000)
    # cv_eu = cv_european(s0=100, k=100, r=0.05, s=0.25, R=10000)

    cmc_eu_err = abs(bs - cmc_eu) / bs
    ant_err = abs(bs - ant_eu) / bs
    # cv_err = abs(bs - cv_eu) / bs

    print("Exact value: ", bs)

    print("CMC European value:", cmc_eu)
    print("CMC European relative error:", cmc_eu_err)

    print("CMC Asian with n=2 value:", cmc_as_2)
    print("CMC Asian with n=3 value:", cmc_as_3)
    print("CMC Asian with n=17 value:", cmc_as_17)

    print("Antithetic European value:", ant_eu)
    print("Antithetic European relative error:", ant_err)
