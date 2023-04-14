from Matrix import Matrix
from Methods import jacobi, gauss
N = 988
N_TEST = 6
THRESHOLD = pow(10, -9)
MAX_ITERATION=1000

A = Matrix(N_TEST,N_TEST)
b = Matrix(N_TEST)
x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
print(x)
x = gauss(A, b)
print(x)


