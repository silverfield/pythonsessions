# ------------------------------------------
# Computes n! for given n


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorials------------------------------------")
print(factorial(5))  # should print 120
print(factorial(4))  # should print 24

# ------------------------------------------
# Computes n-th Fibonacci's number, if 0-th and 1st are both equal to 1


def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print("Fibonacci------------------------------------")
print(fib(4))  # should print 5
print(fib(5))  # should print 8

# ------------------------------------------
# Recursive formula for some Dynamical-Systems-like sequence. k could be a "death rate" and q could be
# "number of born people per period"


def a(n, k, q):
    if n == 0:
        return 4
    result = k*a(n - 1, k, q) + q

    # this prints values while working towards a(n)
    print("\ta(" + str(n) + ", " + str(k) + ", " + str(q) + ") = " + str(result))

    return result

print("DS formula------------------------------------")
print(a(3, 0.7, 10))
print(a(50, 0.9, 4))  # notice how this converges to "fixed point"