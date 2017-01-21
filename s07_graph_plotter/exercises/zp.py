__author__ = 'ferrard'

def get_ranks(p):
    ranks = [None]*p
    ranks[1] = 0
    for i in range(2, p):
        s = i
        ranks[i] =
        while s != 1:
            s *= i
