__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import time
import matplotlib.pyplot as plt
import numpy as np
import random

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
# Interface - Sum of squares to
# ---------------------------------------------------------------


def sum_sq_builtin(n):
    """Sums squares of numbers up to n using built-in function - O(n)"""
    print(sum(i*i for i in range(n)))


def sum_sq_explicit(n):
    """Sums squares of numbers up to n explicitely - O(n)"""
    total = 0
    for i in range(n):
        total += i*i
    print(total)


def sum_sq_analytic(n):
    """Sums squares of numbers up to n, analytically -  O(1)"""
    print(n*(n + 1)*(2*n + 1)//6)

# ---------------------------------------------------------------
# Sorting
# ---------------------------------------------------------------

MAX_SORT_NUMBER = 1000


def check_is_sorted(l):
    n = len(l)
    print(str(n) + " - Sorted OK" if all(l[i] <= l[i + 1] for i in range(n - 1)) else "Sorted NOK")


def sort_quadratic(n):
    """Sort n random numbers - using inefficient quadratic sort - O(n^2)"""
    l = list(np.random.random_integers(0, MAX_SORT_NUMBER, n))
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    check_is_sorted(l)


def sort_inbuilt(n):
    """Sorts n random numbers - using efficient inbuilt function - O(n log n)"""
    l = list(np.random.random_integers(0, MAX_SORT_NUMBER, n))
    l.sort()
    check_is_sorted(l)


def sort_counting(n):
    """Sorts n random numbers bounded in a small range - using efficient linear sort - O(n)"""
    l = list(np.random.random_integers(0, MAX_SORT_NUMBER, n))
    counts = [0]*(MAX_SORT_NUMBER + 1)
    for i in l:
        counts[i] += 1
    counter = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            l[counter] = i
            counter += 1
    check_is_sorted(l)


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


def fib_n(n):
    """Efficient way to compute Fibonacci's numbers. Complexity = O(n)"""
    fibs = [0, 1]  # we don't need to store all along the way, but the memory is still as good as in the naive alg
    for i in range(2, n + 1):
        fibs.append(fibs[-2] + fibs[-1])
    print(fibs[-1])
    return fibs[-1]


def fib_n_closed(n):
    """Closed-form computation Fibonacci's numbers. Complexity = O(n)

    WRONG! Problems with precision!
    """
    fi = (1 + np.sqrt(5))/2
    res = int(np.round((fi**n - (-fi)**(-n))/np.sqrt(5)))
    print(res)
    return res

# ---------------------------------------------------------------
# Primality tests
# ---------------------------------------------------------------


def check_hundred_primes_naive(n):
    """Checks 100 random numbers with n digits - if they are prime, using the naive alg. O(2^(sqrt(n))"""
    for i in range(100):
        number = random.randint(10**n, 10**(n + 1))
        primality_test_naive(number)


def check_hundred_primes_miller_rabin(n):
    """Checks 100 random numbers with n digits - if they are prime, using Miller-Rabin test. O(n)"""
    for i in range(100):
        number = random.randint(10**n, 10**(n + 1))
        primality_test_miller_rabin(number)


def primality_test_naive(n):
    """Does primality test for n in a naive way. Complexity O(sqrt(n))"""
    print("Checking " + str(n))
    if n % 2 == 0:
        n += 1
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            print(str(n) + " is composite")
            return False

    print(str(n) + " is prime")
    return True


def modular_exp(a, b, n):
    """Computes a^b mod n. Complexity O(log(b))"""
    res = 1
    q = a
    while b > 0:
        if b % 2 == 1:
            res = q*res % n
        q = q*q % n
        b //= 2

    return res


def primality_test_miller_rabin(n):
    """Miller-Rabin primality test. Complexity O(log(n))"""
    print("Checking " + str(n))
    if n % 2 == 0:
        n += 1

    # write m as t*2^s
    s = 0
    x = 2
    while (n - 1) % x == 0:
        s += 1
        x *= 2
    s -= 1
    x //= 2
    t = (n - 1)//x

    # do k iterations, looking for witnesses
    k = 10
    for i in range(k):
        b = random.randint(2, n - 2)
        l = modular_exp(b, t, n)
        if l in [1, n - 1]:
            continue
        for j in range(1, s):
            l = l*l % n
            if l == n - 1:
                break
        if l != n - 1:  # found witness
            print(str(n) + " is composite")
            return False

    print(str(n) + " is prime with probability > " + str(1 - (1/4)**k))
    return True

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    print(modular_exp(111, 98, 197))
    exit()

    time_them(20, 1000000, sum_builtin, sum_explicit, sum_analytic)
    time_them(20, 100000, sum_sq_builtin, sum_sq_explicit, sum_sq_analytic)
    time_them(25, 50, fib_n, fib_n_naive)
    time_them(25, 500, fib_n, fib_n_closed)
    time_them(10, 10000, sort_counting, sort_inbuilt, sort_quadratic)
    time_them(10, 1000000, sort_counting, sort_inbuilt)
    time_them(30, 80, check_hundred_primes_naive, check_hundred_primes_miller_rabin)

if __name__ == '__main__':
    main()
