# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import scipy

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def read_matrix():
    """ Function to read in a matrix - line by line (each line being one row)

    :return: The scipy.matrix object representing the matrix
    """
    print("Hey! Give me rows of numbers!")
    print("(separate the numbers with spaces)")
    print("(finish with empty line)")

    rows = []  # this will be a list read-in matrix rows - each row being a list of numbers
    s = input()
    while s != "":  # until the user does not input an empty line
        list_of_strings = s.split(' ')
        list_of_integers = [int(i) for i in list_of_strings]
        rows.append(list_of_integers)

        # we check if the new row has the same number of columns as the very first one
        if len(list_of_integers) != len(rows[0]):
            raise Exception("Hey! That's not a matrix")

        # get another input from user
        s = input()

    # make a matrix out of the read-in data and return it as a result from the function
    m = scipy.matrix(rows)
    return m

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

# we use our function twice to read in two matrices
m_1 = read_matrix()
print("M1: \n" + str(m_1))
m_2 = read_matrix()
print("M2: \n" + str(m_2))

# we print their shapes (number of rows, number of columns)
print("Shape of M1: " + str(m_1.shape))
print("Shape of M2: " + str(m_2.shape))

# we check if the matrices have compatible shapes (can be multiplied)
if m_1.shape[1] != m_2.shape[0]:
    raise Exception("Incompatible matrices")

# we multiply them and print result
mult = m_1 * m_2
print("M1 x M = \n" + str(mult))