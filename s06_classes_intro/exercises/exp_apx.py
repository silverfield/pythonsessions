__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import cmath
import math
import numpy as np

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def exp_apx_naive(x, n):
    result = 0
    for i in range(n):
        result += x**i/math.factorial(i)
    return result


def exp_apx(x, n):
    result = 0
    for i in range(n):
        term = 1
        for j in range(1, i + 1):
            term *= (x/j)
        result += term
    return result


def test_exp(x, n):
    for i in range(1, n, 100):
        true_value = math.exp(x)
        try:
            apx_naive_value = exp_apx_naive(x, i)
        except Exception as e:
            apx_naive_value = str(e)
        try:
            apx_value = exp_apx(x, i)
        except Exception as e:
            apx_value = str(e)

        print("i = " + str(i))
        print("True value = " + str(true_value))
        print("Apx naive value = " + str(apx_naive_value))
        print("Apx value = " + str(apx_value))
        print()


def cos_apx_naive(x, n):
    result = 0
    sign = 1
    for i in range(n):
        result += sign*(x**(2*i))/math.factorial(2*i)
        sign *= -1
    return result


def cos_apx(x, n):
    result = 0
    sign = 1
    for i in range(n):
        term = 1
        for j in range(1, 2*i + 1):
            term *= (x/j)
        result += sign*term
        sign *= -1
    return result


def test_cos(x, n):
    for i in range(1, n, 10):
        true_value = cmath.cos(x)
        try:
            apx_naive_value = cos_apx_naive(x, i)
        except Exception as e:
            apx_naive_value = str(e)
        try:
            apx_value = cos_apx(x, i)
        except Exception as e:
            apx_value = str(e)

        print("i = " + str(i))
        print("True value = " + str(true_value))
        print("Apx naive value = " + str(apx_naive_value))
        print("Apx value = " + str(apx_value))
        print()

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    # test_exp(2, 1000)
    # print(cmath.cos(1 + 1j))
    # print(cmath.exp(1 + 1j))
    test_cos(2+2j, 1000)

if __name__ == '__main__':
    main()

