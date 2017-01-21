__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import scipy as sp
from numpy import random as random

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def find_distance_naive(mat):
    """Given the matrix (n x m) of numbers, finds the (shortest) distance from bottom-left to top-right corner

    Method used is recursion that checks all possible paths

    Time = O((m + n) choose n)
    """
    def __find_dist_naive_to(a, b):
        if a == 0 and b == 0:
            return mat[a][b]
        if a == 0:
            bottom = float("inf")
        else:
            bottom = __find_dist_naive_to(a - 1, b)
        if b == 0:
            left = float("inf")
        else:
            left = __find_dist_naive_to(a, b - 1)
        return mat[a][b] + min(left, bottom)

    return __find_dist_naive_to(mat.shape[0] - 1, mat.shape[1] - 1)


def find_distance(mat):
    """Given the matrix (n x m) of numbers, finds the (shortest) distance from bottom-left to top-right corner

    Uses dynamic programming for optimal time complexity
    Time = O(n*m)
    """
    n, m = mat.shape
    dists = sp.zeros(mat.shape)

    # init
    dists[0][0] = mat[0][0]
    for i in range(1, n):
        dists[i][0] = mat[i][0] + dists[i - 1][0]
    for j in range(1, m):
        dists[0][j] = mat[0][j] + dists[0][j - 1]

    # dynamic programming
    for i in range(1, n):
        for j in range(1, m):
            dists[i][j] = min(dists[i - 1][j], dists[i][j - 1]) + mat[i][j]

    return int(dists[n - 1][m - 1])


def find_min_path(mat):
    """Extends the previous approach to find the shortest path also

    Time = O(n*m)
    """
    n, m = mat.shape
    dists = sp.zeros(mat.shape)
    came_from = sp.zeros(mat.shape).tolist()

    # init
    dists[0][0] = mat[0][0]
    came_from[0][0] = None
    for i in range(1, n):
        dists[i][0] = mat[i][0] + dists[i - 1][0]
        came_from[i][0] = (i - 1, 0)
    for j in range(1, m):
        dists[0][j] = mat[0][j] + dists[0][j - 1]
        came_from[0][j] = (0, j - 1)

    # dynamic programming
    for i in range(1, n):
        for j in range(1, m):
            dists[i][j] = mat[i][j]
            if dists[i - 1][j] < dists[i][j - 1]:
                dists[i][j] += dists[i - 1][j]
                came_from[i][j] = (i - 1, j)
            else:
                dists[i][j] += dists[i][j - 1]
                came_from[i][j] = (i, j - 1)

    # reconstruct path
    current = (n - 1, m - 1)
    p = []
    while current is not None:
        p.append(current)
        current = came_from[current[0]][current[1]]
    p.reverse()

    return int(dists[n - 1][m - 1]), p


def exist_path_with_dist(mat, d):
    """Finds out, if there is a path through the grid with length d, and if so, returns it

    Time = O(n*m*d)
    """
    n, m = mat.shape
    came_from = sp.zeros((n, m, d + 1)).tolist()  # can we get to (x,y) using up distance z? If so, from where?

    # dynamic programming
    if mat[0][0] <= d:
        came_from[0][0][mat[0][0]] = None
    for k in range(d + 1):
        for i in range(0, n):
            for j in range(0, m):
                if i == j == 0:
                    continue
                e = mat[i][j]
                if k < e:
                    continue
                if i > 0 and came_from[i - 1][j][k - e] != 0:
                    came_from[i][j][k] = (i - 1, j)
                if j > 0 and came_from[i][j - 1][k - e] != 0:
                    came_from[i][j][k] = (i, j - 1)

    # we couldn't get to the top right corner using up distance d
    if came_from[n - 1][m - 1][d] == 0:
        return None

    # reconstruct the path
    current = (n - 1, m - 1)
    q = d
    p = []
    while current is not None:
        p.append(current)
        value = mat[current[0]][current[1]]
        current = came_from[current[0]][current[1]][q]
        q -= value
    p.reverse()
    return p


def print_matrix(mat, path=None):
    """Prints the matrix, also with the path through is (if specified)"""
    path_set = set(path) if path is not None else None
    dims = mat.shape
    for i in range(dims[0] - 1, -1, -1):
        for j in range(dims[1]):
            s = str(mat[i][j])
            if path_set is not None and (i, j) in path_set:
                s = "*" + s
            print(s.rjust(4), end="")
        print()


# ---------------------------------------------------------------
# Constants
# ---------------------------------------------------------------

DEF_DIM = 4

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main(argv):
    # if there's just one argument, it's the file name containing the matrix
    if len(argv) == 1:
        with open(argv[0], 'r') as f:
            lines = []
            for line in f.readlines():
                lines.append([int(i) for i in line.split(' ')])
            lines.reverse()
            mat = sp.array(lines)
    # otherwise we make a random grid
    else:
        dims = (DEF_DIM, DEF_DIM)
        if len(argv) == 2:
            dims = int(argv[0]), int(argv[1])
        random.seed()
        mat = random.random_integers(1, 10, size=dims)

    # try out all the methods
    print("Looking at path from bottom left corner to top right corner")

    print_matrix(mat)

    print("Min distance: " + str(find_distance(mat)))

    print("Min distance naive: " + str(find_distance_naive(mat)))

    d, path = find_min_path(mat)
    print("Min distance and path: " + str(d) + ": " + str(path))
    print_matrix(mat, path)

    for i in range(sum(mat.ravel())):
        path = exist_path_with_dist(mat, i)
        print("Exists distance " + str(i) + ": " + ("no" if path is None else str(path)))
        print_matrix(mat, path)

if __name__ == '__main__':
    import sys
    # main(sys.argv[1:])
    # main(['matrix.txt'])
    main(['original.txt'])