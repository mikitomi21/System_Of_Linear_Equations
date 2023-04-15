from Matrix import Matrix
from Methods import jacobi, gauss
import time
N = 988
THRESHOLD = pow(10, -9)
MAX_ITERATION=100

A = Matrix(N,N)
b = Matrix(N)

#Jacobi method
start = time.time()
x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
end = time.time()
print(f"Jacobi time:{end-start}")

#Gauss method
start = time.time()
x = gauss(A, b, THRESHOLD, MAX_ITERATION)
end = time.time()
print(f"Gauss time:{end-start}")

'''Matrix.a1 = 3
Matrix.a2 = -1
Matrix.a3 = -1
A = Matrix(N,N)
b = Matrix(N)
x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
x = gauss(A, b, THRESHOLD, MAX_ITERATION)
'''

