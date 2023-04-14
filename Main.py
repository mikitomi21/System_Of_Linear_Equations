from Matrix import Matrix
from Methods import jacobi
N = 988
N_TEST = 6

A = Matrix(N_TEST,N_TEST)
b = Matrix(N_TEST)
jacobi(A, b)


