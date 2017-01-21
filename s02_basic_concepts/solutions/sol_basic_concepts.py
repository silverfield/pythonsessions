__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import math
import time
import sys

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def never_stop():
    """Will never stop"""
    while True:
        pass


def slow_down():
    """Will take up all the memory and then continue taking space on the harddisk, the swapping resulting in
    slowing down the system
    """
    l = []
    while True:
        l.append(47)


def circle(r):
    """Prints a circle with radius r"""
    for y in range(r*2 + 1):
        for x in range(r*2 + 1):
            time.sleep(0.1)
            sys.stdout.flush()
            dist = math.sqrt((x - r)**2 + (y - r)**2)
            diff = abs(dist - r)
            print("*" if diff <= 0.5 else " ", end="")
        print()


def square(a):
    """Prints a square with side length a"""
    for i in range(a):
        for j in range(a):
            print("*", end="")
            sys.stdout.flush()
            time.sleep(0.05)
        print()


def heart(r):
    """Prints a heart with size parametrized by r (must be an even number)"""
    if r % 2 != 0:
        print("r must be even")
        return

    for y in range(r*2 + 1 - r//2):
        for x in range(r*2 + 1):
            # top two half-circles
            if y <= r//2:
                # first half circle
                if x <= r:
                    dist = math.sqrt((x - r//2)**2 + (y - r//2)**2)
                    diff = abs(dist - r//2)
                    print("*" if diff <= 0.5 else " ", end="")
                # second half circle
                else:
                    dist = math.sqrt((x - (r//2 + r))**2 + (y - r//2)**2)
                    diff = abs(dist - r//2)
                    print("*" if diff <= 0.5 else " ", end="")
            else:
                print("*" if (x == (y - r//2) or x == (r*2 + r//2 - y)) else " ", end="")
        print()


def skewed(a):
    """Prints a skewed square with side length a"""
    for i in range(a):
        # conscise: print(' '*i, end="")
        for j in range(i):
            print(' ')
        for j in range(a):
            print("*", end="")
        print()

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

if __name__ == "__main__":
    # square(10)
    # circle(6)
    # skewed(20)
    heart(10)