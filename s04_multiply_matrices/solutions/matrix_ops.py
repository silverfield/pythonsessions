__author__ = 'ferrard'

import scipy as sp
import scipy.linalg as la

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    # define matrices
    m_a = sp.matrix(
        '1 5 8;'
        '0 -1 4'
    )
    print(type(m_a))

    m_b = sp.matrix(
        '1 4;'
        '-2 0;'
        '-3 1'
    )

    m_c = sp.matrix(
        '1 2 4;'
        '3 8 14;'
        '2 6 13'
    )

    m_d = sp.matrix(
        '0 1 -1;'
        '5 7 9;'
        '-3 0 0'
    )

    # print them
    print("Matrix A is: \n" + str(m_a))
    print("Matrix B is: \n" + str(m_b))
    print("Matrix C is: \n" + str(m_c))
    print()

    # their shape
    print("Shape of A is: " + str(m_a.shape))
    print("Shape of B is: " + str(m_b.shape))
    print("Shape of C is: " + str(m_c.shape))
    print()

    # add/multiply
    m_add = m_c + m_d
    print("C+D = \n" + str(m_add))

    m_mult = m_a * m_b
    print("A*B = \n" + str(m_mult))

    # inverse
    m_inv = la.inv(m_c)
    print("Inverse of C is: \n" + str(m_inv))

    # determinant
    det = la.det(m_c)
    print("Determinant of C: " + str(det))

    # eigen-decomposition
    eig_vals_vectors = la.eig(m_c)
    print("Eigenvalues of C: \n" + str(eig_vals_vectors[0]))
    print("Eigenvectors (unit) of C (vectors are in columns): \n" + str(eig_vals_vectors[1]))
    # let's verify
    u_1 = eig_vals_vectors[1][:, 0]
    u_1 = u_1.reshape(u_1.size, 1)
    print("C*u_1: \n" + str(m_c*u_1))
    print("lambda_1*u_1: \n" + str(eig_vals_vectors[0][0]*u_1))

    # LU-decomposition
    m_p, m_l, m_u = la.lu(m_c)
    print("LU decomposition of C:\n"
          "P: \n" + str(m_p) + "\n"
          "L: \n" + str(m_l) + "\n"
          "U: \n" + str(m_u) + "\n")

    # solve a system
    b = sp.array([1, 5, 6])
    print("b is: \n" + str(b))
    x = la.solve(m_c, b)
    print("Solution to Cx = b: " + str(x))

if __name__ == "__main__":
    main()