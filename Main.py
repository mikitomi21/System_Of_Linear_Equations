from Matrix import Matrix
from Methods import jacobi, gauss, factLU
import time

#N = 988
N=10
THRESHOLD = pow(10, -9)
MAX_ITERATION=1000

'''
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
'''

'''
Matrix.a1 = 3
Matrix.a2 = -1
Matrix.a3 = -1
A = Matrix(N,N)
b = Matrix(N)
x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
x = gauss(A, b, THRESHOLD, MAX_ITERATION)
'''


test = [[2,1,1,0],
        [4,3,3,1],
        [8,7,9,5],
        [6,7,9,8],]
A = Matrix(4,4,test)
b = Matrix(4)
x = factLU(A, b, THRESHOLD, MAX_ITERATION)

