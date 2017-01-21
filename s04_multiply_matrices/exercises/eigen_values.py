__author__ = 'ferrard'

import numpy as np
import math

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def get_2x2_eigen(m):
    b = - m[0, 0] - m[1, 1]
    c = m[0, 0]*m[1, 1] - m[0, 1]*m[1, 0]

    eig1 = (-b + math.sqrt(b**2 - 4 * c)) / 2
    eig2 = (-b - math.sqrt(b**2 - 4 * c)) / 2
    return eig1, eig2


def get_eigen(m):
    return np.linalg.eig(m)

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    print("Inpute first row of the 2x2 matrix: ")
    first = input()
    print("Inpute second row of the 2x2 matrix: ")
    second = input()

    first_numbers = [int(i) for i in first.split(' ')]
    second_numbers = [int(i) for i in second.split(' ')]

    m = np.array([first_numbers, second_numbers])
    eigen_values = get_2x2_eigen(m)
    print("First eigenvalue: " + str(eigen_values[0]))
    print("Second eigenvalue: " + str(eigen_values[1]))

    print(np.linalg.eig(m))

if __name__ == "__main__":
    main()