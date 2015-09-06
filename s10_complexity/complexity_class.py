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
        print("Testing function " + functions[i].__name__)
        results_for_f = []
        for n in n_values:
            print("\tInput size " + str(n))
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
# Interface - Sum to
# ---------------------------------------------------------------


def sum_builtin(n):
    """Sums numbers up to n using built-in function - O(n)"""
    print(sum(range(n)))


def sum_explicit(n):
    """Sums numbers up to n explicitely - O(n)"""
    total = 0
    for i in range(n):
        total += i
    print(total)


def sum_analytic(n):
    """Sums numbers up to n, analytically -  O(1)"""
    print(n*(n + 1)//2)

# ---------------------------------------------------------------
# Fibonnachi numbers
# ---------------------------------------------------------------


def fib_n_naive(n):
    """Naive (recursive) way to compute Fibonacci's numbers. O(F(n))"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_n_naive(n - 1) + fib_n_naive(n - 2)


def fib_n_efficient(n):
    """Efficient way to compute Fibonacci's numbers. Complexity = O(n)"""
    a = 0
    b = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    print(b)
    return b


def fib_n_closed(n):
    """Closed-form computation Fibonacci's numbers. Complexity = O(n)

    WRONG! Problems with precision!
    """
    fi = (1 + sp.sqrt(5))/2
    res = int(round((fi**n - (-fi)**(-n))/sp.sqrt(5)))
    print(res)
    return res

# ---------------------------------------------------------------
# Sorting
# ---------------------------------------------------------------

BOUND = 1000
# BOUND = 1000000  # try this bound - the linear sort will much more slow down


def sort_selection(n):
    """Sort n random numbers - using inefficient quadratic sort - O(n^2)"""
    l = list(sp.random.random_integers(0, BOUND, n))
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp


def sort_inbuilt(n):
    """Sorts n random numbers - using efficient inbuilt function - O(n log n)"""
    l = list(sp.random.random_integers(0, BOUND, n))
    l.sort()


def sort_linear(n):
    """Sorts n random numbers bounded in a small range - using efficient linear sort, called Counting sort - O(n)"""
    l = list(sp.random.random_integers(0, BOUND, n))
    counts = [0]*(BOUND + 1)
    for i in l:
        counts[i] += 1
    counter = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            l[counter] = i
            counter += 1

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    # time_them(20, 1000, n_sqrt_n, n_squared)
    # time_them(20, 1000000, sum_builtin, sum_explicit, sum_analytic)
    # time_them(20, 100, fib_n_naive, fib_n_closed, fib_n_efficient)
    # time_them(20, 1000, fib_n_closed, fib_n_efficient)
    # time_them(20, 10000, sort_inbuilt, sort_linear, sort_selection)
    time_them(20, 1000000, sort_inbuilt, sort_linear)

if __name__ == '__main__':
    main()
