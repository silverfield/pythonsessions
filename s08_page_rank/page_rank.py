import scipy as sp

SINK = [
    [1],
    [3],
    [0, 1],
    []
]

DISCONNECTED = [
    [1],
    [0],
    [3, 4],
    [2, 4],
    [2, 3]
]

def iterative_pr(d, M, epsilon, max_it):
    n = M.shape[0]
    prs = (1/n)*sp.ones((n, 1))
    for i in range(max_it):
        print("Iter. " + str(i) + " prs: " + str(prs))
        new_prs = (1 - d)/n + d*sp.dot(M, prs)
        if all(abs(new_prs[k] - prs[k]) < epsilon for k in range(n)):
            print("Finished - cause of little change")
            return new_prs
        prs = new_prs

    print("Finished - max. iter. reached")
    return prs

def algebraic_pr(d, M):
    n = M.shape[0]

def make_tranistion_matrix(link_graph):
    n = len(link_graph)
    M = sp.zeros((n, n))
    for j in range(n):
        for i in link_graph[j]:
            M[i][j] = 1/len(link_graph[j])

    return M

M = make_tranistion_matrix(SINK)
print(M)
page_ranks = iterative_pr(0.85, M, 0.01, 20)
print(page_ranks)