# __author__ = 'ferrard'

n = 100

# --------------------------------------------------
# region
# linear - O(n)
# endregion

total = 0
for i in range(n):
    total += 1
print(total)

# --------------------------------------------------
# region
# quadratic O(n^2)
# endregion

for i in range(n):
    for j in range(n):
        print(str(i) + " " + str(j) + ", ", end="")
    print()

# --------------------------------------------------
# region
# number of handshakes - still quadratic O(n^2)
# endregion

for i in range(n):
    for j in range(i, n):
        print(str(i) + " " + str(j) + ", ", end="")
    print()

# --------------------------------------------------
# region
# complexity may be inside called functions - O(n^2)
# endregion

s = "Hello EveryOne!"
for i in range(n):
    s += 'a'
    s.swapcase()
print(s)

# --------------------------------------------------
# region
# the complexity may be caused by recursion - O(n)
# endregion


def factorial(k):
    if k == 0:
        return 1
    return k * factorial(k - 1)
factorial(n)

# --------------------------------------------------
# region
# computes integer part of log(n). Complexity is also O(log n)
# endregion


def f1(k):
    result = 0
    x = 2
    while x <= k:
        x *= 2
        result += 1
    return result
print(f1(n))

# --------------------------------------------------
# region
# computes integer part of sqrt(n). Complexity is also O(sqrt n)
# endregion


def f2(k):
    x = 1
    while x*x <= k:
        x += 1
    return x - 1
print(f2(n))


# --------------------------------------------------
# region
# 2^n - extremely stupid impl. with time O(2^n). We can do it in O(n), even O(log n)
# endregion


def stupid_function(k):
    if k == 0:
        return 1
    return stupid_function(k - 1) + stupid_function(k - 1)
print(stupid_function(n))

# --------------------------------------------------
# region
# constant term does not matter - O(n)
# endregion

total = 0
for i in range(n):
    total += 1
    total /= 1.5
    total -= 47
    total = abs(total)
    print("What the hell is this computing?")
print(total)

# --------------------------------------------------
# region
# considering worst case is enough - O(n)
# endregion

if n == 1000047:
    print("That's too much")
else:
    for i in range(n):
        print("*")