__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import scipy as sp
from scipy import linalg as la

# ---------------------------------------------------------------
# Constants
# ---------------------------------------------------------------

# for dumping factor 1, cannot be computed in algebraic way
NOT_INVERTIBLE = [
    [1, 2, 3],
    [2, 3],
    [0],
    [0, 2],
]

# for d.f. 1, results in zero page-ranks
SINK = [
    [1],
    [3],
    [0, 1],
    [],
]

# for d.f. 1, cannot be computed in the algebraic way, as the matrix I - d*M is singular
DISCONNECTED = [
    [1],
    [0],
    [3, 4],
    [2, 4],
    [2, 3],
]

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def get_algebraic_page_rank(transition_matrix, dumping_factor=0.85):
    """Computes the page ranks in an algebraic way"""
    n = transition_matrix.shape[0]
    m_a = transition_matrix
    d = dumping_factor

    ls = la.inv(sp.identity(n) - d*m_a)
    rs = sp.matrix([(1-d)/n]*n).reshape(n, 1)

    return sp.dot(ls, rs)


def get_iter_page_rank(transition_matrix, iterations=20, dumping_factor=0.85, epsilon=10e-5):
    """Computes the page ranks in an iterative way

    The computation terminates once:
    - specified number of iterations has been reached
    - the difference in the page ranks after one iteration is negligible"""
    n = transition_matrix.shape[0]
    m_a = transition_matrix
    d = dumping_factor

    print("Computing page-rank. number of pages = " + str(n) + ", dumping factor = " + str(d))
    page_ranks = sp.array([1/n]*n).reshape((n, 1))
    for i in range(iterations):
        print("\tIteration " + str(i) + ": " + str([float(pr) for pr in page_ranks]))
        new_page_ranks = (1 - d)/n + d*sp.dot(m_a, page_ranks)
        if all(abs(new_page_ranks[i] - page_ranks[i]) < epsilon for i in range(n)):
            print("Stopped due to negligible changes\n")
            return page_ranks
        page_ranks = new_page_ranks
    print("Stopped after reaching max. number of iterations\n")
    return page_ranks


def make_transition_matrix(links):
    """Takes in a list of (n) lists representing the linkage among pages

    Page indices range from 0..n -> a list with index k specifies what pages the k-th page links to

    Returns the transition matrix A where value A[i, j] is
     - 0 if i-th page is not linked to from j-th page
     - 1/s otherwise, where s is the number of links on j-th page
    """
    n = len(links)
    transition_matrix = sp.zeros((n, n))
    for i in range(n):
        for j in range(len(links[i])):
            transition_matrix[links[i][j]][i] = 1/len(links[i])

    return transition_matrix


def print_page_ranks(page_ranks):
    """Prints the list of page-ranks"""
    print("Page ranks:")
    for i in range(len(page_ranks)):
        print("\t" + str(i) + ": " + str(float(page_ranks[i])))
    print()

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    links = SINK
    transition_matrix = make_transition_matrix(links)
    print("Transition matrix: \n" + str(transition_matrix))
    print()

    df = 0.85
    page_ranks_iter = get_iter_page_rank(transition_matrix, dumping_factor=df)
    page_ranks_algebraic = get_algebraic_page_rank(transition_matrix, dumping_factor=df)
    print_page_ranks(page_ranks_iter)
    print_page_ranks(page_ranks_algebraic)

    df = 1
    page_ranks_iter = get_iter_page_rank(transition_matrix, dumping_factor=df)
    page_ranks_algebraic = get_algebraic_page_rank(transition_matrix, dumping_factor=df)
    print_page_ranks(page_ranks_iter)
    print_page_ranks(page_ranks_algebraic)

if __name__ == '__main__':
    main()
