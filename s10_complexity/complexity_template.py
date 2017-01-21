__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import time
import matplotlib.pyplot as plt
import scipy as sp

# ---------------------------------------------------------------
# Interface - Timing function
# ---------------------------------------------------------------


def time_them(k, m, *functions):
    """Times the functions (accepting one argument - n) on k values of n up to m

    Stops the timing once the function's execution takes:
    - more then 2 sec
    - more then 1 sec longer then on previous value of n
    """
    n_values = list(range(1, m))
    if m > k:
        n_values = list(range(1, m, m//k))
    results = []
    for i in range(len(functions)):
        results_for_f = []
        for n in n_values:
            before = time.time()
            functions[i](n)
            after = time.time()
            results_for_f.append(after - before)
            if results_for_f[-1] > 2 or (len(results_for_f) > 1 and results_for_f[-1] - results_for_f[-2] > 1):
                break
        results.append(results_for_f)

    for i in range(len(functions)):
        plt.plot(n_values[:len(results[i])], results[i], label=functions[i].__name__)
    plt.legend()
    plt.show()

# ---------------------------------------------------------------
# Interface - try out
# ---------------------------------------------------------------


def n_sqrt_n(n):
    res = 0
    for i in range(n*int(sp.sqrt(n))):
        res += 1
    return res


def n_squared(n):
    res = 0
    for i in range(n*n):
        res += 1
    return res

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    time_them(20, 1000, n_sqrt_n, n_squared)

if __name__ == '__main__':
    main()
