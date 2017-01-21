l = [4, 5, 6, 7, 8, 9]

# print list
for i in l:
    print(i)

print("------------------------------------------")

# print using indexing
for i in range(len(l)):
    print(l[i])

print("------------------------------------------")

# print list in reversed order
for i in range(len(l)):
    print(l[len(l) - i - 1])

print("------------------------------------------")

# print every second item
for i in range(len(l)//2):
    print(l[i*2])

print("------------------------------------------")

# print square
k = 10
for i in range(k):
    for j in range(k):
        print("*", end="")
    print()

print("------------------------------------------")

# print skewed square
k = 10
for i in range(k):
    # print spaces
    for j in range(i):
        print(" ", end="")
    # print stars
    for j in range(k):
        print("*", end="")
    # print new-line
    print()

print("------------------------------------------")

# print circle
import math
import time
import sys

r = 6
for x in range(2*r + 1):
    for y in range(2*r + 1):
        if abs(r - math.sqrt((x - r)**2 + (y - r)**2)) <= 0.5:
            time.sleep(0.03)
            print("*", end="")
        else:
            time.sleep(0.03)
            print(".", end="")
        sys.stdout.flush()
    print()
