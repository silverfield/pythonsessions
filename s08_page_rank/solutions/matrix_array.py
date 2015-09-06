import scipy as sp

# matrix A, stored as array
array_A = sp.array([
    [1, 2],
    [0, 3]
])

# matrix B, stored as array
array_B = sp.array([
    [-1, 0],
    [-2, 1]
])

# vector V, stored as array
array_V = sp.array([
    [1],
    [2]
])

# the same matrix A, stored as matrix
matrix_A = sp.matrix([
    [1, 2],
    [0, 3]
])

# the same matrix B, stored as matrix
matrix_B = sp.matrix([
    [-1, 0],
    [-2, 1]
])

# the same vector V, stored as matrix
matrix_V = sp.matrix([
    [1],
    [2]
])

# matrix addition - same for types array and matrix
print("array A + B is: ")
print(array_A + array_B)
print("matrix A + B is: ")
print(matrix_A + matrix_B)
print()
# OUTPUT:
# array A + B is:
# [[ 0  2]
#  [-2  4]]
# matrix A + B is:
# [[ 0  2]
#  [-2  4]]

# matrix multiplication - DIFFERENT for types array and matrix
print("array A * B is: ")
print(array_A * array_B)
print("sp.dot(array A, B) is: ")
print(sp.dot(array_A, array_B))
print("matrix A * B is: ")
print(matrix_A * matrix_B)
print()
# OUTPUT:
# array A * B is:
# [[-1  0]
#  [ 0  3]]
# sp.dot(array A, B) is:
# [[-5  2]
#  [-6  3]]
# matrix A * B is:
# [[-5  2]
#  [-6  3]]

# similarly for vectors-matrix multiplication - DIFFERENT for types array and matrix
print("array A * V is: ")
print(array_A * array_V)
print("sp.dot(A, V) is: ")
print(sp.dot(array_A, array_V))
print("matrix A * B is: ")
print(matrix_A * matrix_V)
print()
# OUTPUT:
# array A * V is:
# [[1 2]
#  [0 6]]
# sp.dot(array A, V) is:
# [[5]
#  [6]]
# matrix A * B is:
# [[5]
#  [6]]
