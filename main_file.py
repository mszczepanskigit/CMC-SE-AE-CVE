from imports import *

if __name__ == "__main__":
    # Exact Value
    bs = bs_exact(s0=100, k=100, r=0.05, s=0.25)

    print(u'\u2500' * 10)

    
    # CMC European
    cmc_eu_102 = cmc_european(s0=100, k=100, r=0.05, s=0.25, R=100)
    cmc_eu_104 = cmc_european(s0=100, k=100, r=0.05, s=0.25, R=10000)
    cmc_eu_106 = cmc_european(s0=100, k=100, r=0.05, s=0.25, R=1000000)

    cmc_eu_102_err = abs((cmc_eu_102 - bs) / bs)
    cmc_eu_104_err = abs((cmc_eu_104 - bs) / bs)
    cmc_eu_106_err = abs((cmc_eu_106 - bs) / bs)

    print("Exact value:", bs)
    print("CMC European value R=10^2:", cmc_eu_102)
    print("CMC European error R=10^2:", cmc_eu_102_err)
    print("CMC European value R=10^4:", cmc_eu_104)
    print("CMC European error R=10^4:", cmc_eu_104_err)
    print("CMC European value R=10^6:", cmc_eu_106)
    print("CMC European error R=10^6:", cmc_eu_106_err)

    print(u'\u2500' * 10)
    
    # CMC Asian
    cmc_as_102_2 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=100, n=2)
    cmc_as_104_2 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=10000, n=2)
    cmc_as_106_2 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=1000000, n=2)

    cmc_as_102_3 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=100, n=3)
    cmc_as_104_3 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=10000, n=3)
    cmc_as_106_3 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=1000000, n=3)

    cmc_as_102_17 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=100, n=17)
    cmc_as_104_17 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=10000, n=17)
    cmc_as_106_17 = cmc_asian(s0=100, k=100, r=0.05, s=0.25, R=1000000, n=17)

    print("CMC Asian value R=10^2 and n=2 :", cmc_as_102_2)
    print("CMC Asian value R=10^4 and n=2 :", cmc_as_104_2)
    print("CMC Asian value R=10^6 and n=2 :", cmc_as_106_2)

    print("CMC Asian value R=10^2 and n=3 :", cmc_as_102_3)
    print("CMC Asian value R=10^4 and n=3 :", cmc_as_104_3)
    print("CMC Asian value R=10^6 and n=3 :", cmc_as_106_3)

    print("CMC Asian value R=10^2 and n=17:", cmc_as_102_17)
    print("CMC Asian value R=10^4 and n=17:", cmc_as_104_17)
    print("CMC Asian value R=10^6 and n=17:", cmc_as_106_17)

    print(u'\u2500' * 10)
    
    # Stratified European (proportional allocation)
    
    print("Stratified European (proportional) value R=10^4, m=5:", strat_prop(100, 100, 0.05, 0.25, 10000, 5))
    print("Stratified European (proportional) value R=10^4, m=10:", strat_prop(100, 100, 0.05, 0.25, 10000, 10))
    print("Stratified European (proportional) value R=10^6, m=5:", strat_prop(100, 100, 0.05, 0.25, 1000000, 5))
    print("Stratified European (proportional) value R=10^6, m=10:", strat_prop(100, 100, 0.05, 0.25, 1000000, 10))
    print("Stratified European (proportional) value R=10^6, m=50:", strat_prop(100, 100, 0.05, 0.25, 1000000, 50))
    
    print(u'\u2500' * 10)
    
    # Stratified European (optimal allocation)
    
    print("Stratified European (optimal) value R=10^4, m=5, R'=100:", strat_opt(100, 100, 0.05, 0.25, 10000, 5, 100))
    print("Stratified European (optimal) value R=10^4, m=10, R'=100:", strat_opt(100, 100, 0.05, 0.25, 10000, 10, 100))
    print("Stratified European (optimal) value R=10^4, m=5, R'=1000:", strat_opt(100, 100, 0.05, 0.25, 10000, 5, 1000))
    print("Stratified European (optimal) value R=10^4, m=10, R'=1000:", strat_opt(100, 100, 0.05, 0.25, 10000, 10, 1000))
    print("Stratified European (optimal) value R=10^6, m=5, R'=100:", strat_opt(100, 100, 0.05, 0.25, 1000000, 5, 100))
    print("Stratified European (optimal) value R=10^6, m=10, R'=100:", strat_opt(100, 100, 0.05, 0.25, 1000000, 10, 100))
    print("Stratified European (optimal) value R=10^6, m=50, R'=100:", strat_opt(100, 100, 0.05, 0.25, 1000000, 50, 100))
    print("Stratified European (optimal) value R=10^6, m=5, R'=1000:", strat_opt(100, 100, 0.05, 0.25, 1000000, 5, 1000))
    print("Stratified European (optimal) value R=10^6, m=10, R'=1000:", strat_opt(100, 100, 0.05, 0.25, 1000000, 10, 1000))
    print("Stratified European (optimal) value R=10^6, m=50, R'=1000:", strat_opt(100, 100, 0.05, 0.25, 1000000, 50, 1000))
    
    print(u'\u2500' * 10)
    
    # Stratified Asian (proportional allocation)
    
    print("Stratified Asian (proportional) value R=10^4, m=4, n=2:", strat_prop2(100, 100, 0.05, 0.25, 10000, 4, 2))
    print("Stratified Asian (proportional) value R=10^4, m=4, n=3:", strat_prop2(100, 100, 0.05, 0.25, 10000, 4, 3))
    print("Stratified Asian (proportional) value R=10^4, m=4, n=17:", strat_prop2(100, 100, 0.05, 0.25, 10000, 4, 17))
    print("Stratified Asian (proportional) value R=10^4, m=10, n=17:", strat_prop2(100, 100, 0.05, 0.25, 10000, 10, 2))
    print("Stratified Asian (proportional) value R=10^4, m=10, n=3:", strat_prop2(100, 100, 0.05, 0.25, 10000, 10, 3))
    print("Stratified Asian (proportional) value R=10^4, m=10, n=17:", strat_prop2(100, 100, 0.05, 0.25, 10000, 10, 17))
    print("Stratified Asian (proportional) value R=10^6, m=4, n=2:", strat_prop2(100, 100, 0.05, 0.25, 1000000, 4, 2))
    print("Stratified Asian (proportional) value R=10^6, m=4, n=3:", strat_prop2(100, 100, 0.05, 0.25, 1000000, 4, 3))
    print("Stratified Asian (proportional) value R=10^6, m=4, n=17:", strat_prop2(100, 100, 0.05, 0.25, 1000000, 4, 17))
    print("Stratified Asian (proportional) value R=10^6, m=10, n=2:", strat_prop2(100, 100, 0.05, 0.25, 1000000, 10, 2))
    print("Stratified Asian (proportional) value R=10^6, m=10, n=3:", strat_prop2(100, 100, 0.05, 0.25, 1000000, 10, 3))
    print("Stratified Asian (proportional) value R=10^6, m=10, n=17:", strat_prop2(100, 100, 0.05, 0.25, 1000000, 10, 17))

    print(u'\u2500' * 10)
    
    # Stratified Asian (optimal allocation)
    
    print("Stratified Asian (optimal) value R=10^4, m=4, n=2, R'=100:", strat_opt2(100, 100, 0.05, 0.25, 10000, 4, 2, 100))
    print("Stratified Asian (optimal) value R=10^4, m=4, n=3, R'=100:", strat_opt2(100, 100, 0.05, 0.25, 10000, 4, 3, 100))
    print("Stratified Asian (optimal) value R=10^4, m=4, n=17, R'=100:", strat_opt2(100, 100, 0.05, 0.25, 10000, 4, 17, 100))
    print("Stratified Asian (optimal) value R=10^4, m=10, n=2, R'=100:", strat_opt2(100, 100, 0.05, 0.25, 10000, 10, 2, 100))
    print("Stratified Asian (optimal) value R=10^4, m=10, n=3, R'=100:", strat_opt2(100, 100, 0.05, 0.25, 10000, 10, 3, 100))
    print("Stratified Asian (optimal) value R=10^4, m=10, n=17, R'=100:", strat_opt2(100, 100, 0.05, 0.25, 10000, 10, 17, 100))
    print("Stratified Asian (optimal) value R=10^6, m=4, n=2, R'=1000:", strat_opt2(100, 100, 0.05, 0.25, 1000000, 4, 2, 1000))
    print("Stratified Asian (optimal) value R=10^6, m=4, n=3, R'=1000:", strat_opt2(100, 100, 0.05, 0.25, 1000000, 4, 3, 1000))
    print("Stratified Asian (optimal) value R=10^6, m=4, n=17, R'=1000:", strat_opt2(100, 100, 0.05, 0.25, 1000000, 4, 17, 1000))
    print("Stratified Asian (optimal) value R=10^6, m=10, n=2, R'=1000:", strat_opt2(100, 100, 0.05, 0.25, 1000000, 10, 2, 1000))
    print("Stratified Asian (optimal) value R=10^6, m=10, n=3, R'=1000:", strat_opt2(100, 100, 0.05, 0.25, 1000000, 10, 3, 1000))
    print("Stratified Asian (optimal) value R=10^6, m=10, n=17, R'=1000:", strat_opt2(100, 100, 0.05, 0.25, 1000000, 10, 17, 1000))
    
    print(u'\u2500' * 10)

    # Antithetic European
    ant_eu_102 = ant_european(s0=100, k=100, r=0.05, s=0.25, R=100)
    ant_eu_104 = ant_european(s0=100, k=100, r=0.05, s=0.25, R=10000)
    ant_eu_106 = ant_european(s0=100, k=100, r=0.05, s=0.25, R=1000000)

    ant_eu_102_err = abs((ant_eu_102 - bs) / bs)
    ant_eu_104_err = abs((ant_eu_104 - bs) / bs)
    ant_eu_106_err = abs((ant_eu_106 - bs) / bs)

    print("Exact value:", bs)
    print("Antithetic European value R=10^2:", ant_eu_102)
    print("Antithetic European error R=10^2:", ant_eu_102_err)
    print("Antithetic European value R=10^4:", ant_eu_104)
    print("Antithetic European error R=10^4:", ant_eu_104_err)
    print("Antithetic European value R=10^6:", ant_eu_106)
    print("Antithetic European error R=10^6:", ant_eu_106_err)

    print(u'\u2500' * 10)

    # Control Variate European
    cv_eu_102 = cv_european(s0=100, k=100, r=0.05, s=0.25, R=100)
    cv_eu_104 = cv_european(s0=100, k=100, r=0.05, s=0.25, R=10000)
    cv_eu_106 = cv_european(s0=100, k=100, r=0.05, s=0.25, R=1000000)

    cv_eu_102_err = abs((cv_eu_102 - bs) / bs)
    cv_eu_104_err = abs((cv_eu_104 - bs) / bs)
    cv_eu_106_err = abs((cv_eu_106 - bs) / bs)

    print("Exact value:", bs)
    print("Control Variate European value R=10^2:", cv_eu_102)
    print("Control Variate European error R=10^2:", cv_eu_102_err)
    print("Control Variate European value R=10^4:", cv_eu_104)
    print("Control Variate European error R=10^4:", cv_eu_104_err)
    print("Control Variate European value R=10^6:", cv_eu_106)
    print("Control Variate European error R=10^6:", cv_eu_106_err)

    print(u'\u2500' * 10)
       
    
