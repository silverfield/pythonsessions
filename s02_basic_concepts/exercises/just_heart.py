__author__ = 'ferrard'

import math

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

s = input("Zadaj cislo: ")
heart(int(s) * 2)
