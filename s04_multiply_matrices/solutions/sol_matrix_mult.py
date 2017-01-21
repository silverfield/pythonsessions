# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import scipy as sp

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def split(s, split_by_char):
    """Splits the string into substring, splitting by the split-by character

    e.g. "for-the-win" would be split into:
    - "for"
    - "the"
    - "win"
    if '-' was used as a split-by character

    :returns the list of items"""
    if len(split_by_char) != 1:
        raise Exception("The split-by argument must be a single character")

    items = []
    buffer = []
    for c in s:
        if c == split_by_char:
            items.append(''.join(buffer))
            buffer.clear()
            continue
        buffer.append(c)
    items.append(''.join(buffer))

    return items


def read_matrix():
    """Reads in a matrix from standard input - one row at a time - until an empty row is encountered

    :returns the matrix as a numpy.ndarray
    """
    print("Input matrix rows (terminate with empty row):")
    rows = []
    s = input()
    while s != "":
        row = [float(i) for i in split(s, ' ')]
        rows.append(row)
        s = input()

    m = len(rows[0])
    if any(len(row) != m for row in rows):
        raise Exception("Each row must have equal length!")

    mat = sp.matrix(rows)
    print("Read in this matrix:\n" + str(mat) + "\n")
    return mat


def multiply(m_a, m_b):
    """Multiplies the two matrices and returns the resulting matrix"""
    if m_a.shape[1] != m_b.shape[0]:
        raise Exception("The number of columns of matrix A must be the same as the number of rows of matrix B!")

    n = m_a.shape[0]
    m = m_a.shape[1]
    l = m_b.shape[1]

    m_c = sp.zeros((n, l))
    for i in range(n):  # each row of A...
        for j in range(l):  # ...multiplied with each column of B
            # the multiplication itself now
            entry_i_j = 0
            for k in range(m):
                entry_i_j += m_a[i, k]*m_b[k, j]
            m_c[i, j] = entry_i_j

            # concise way: entry_i_j = sum(m_a[i, k]*m_b[k, j] for k in range(m))

    return m_c

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    m_a = read_matrix()
    m_b = read_matrix()
    m_c = multiply(m_a, m_b)
    print("Multiplication is:\n" + str(m_c))

if __name__ == "__main__":
    main()