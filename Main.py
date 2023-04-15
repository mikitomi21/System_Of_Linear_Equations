from Matrix import Matrix
from Methods import jacobi, gauss
N = 988
N_TEST = 1000
THRESHOLD = pow(10, -9)
MAX_ITERATION=100

A = Matrix(N_TEST,N_TEST)
b = Matrix(N_TEST)
#x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
#(f"x={x}")
x = gauss(A, b, THRESHOLD, MAX_ITERATION)
print(f"x={x}")


