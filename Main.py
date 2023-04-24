import numpy as np

from Matrix import Matrix
from Methods import jacobi, gauss, factLU, factLUCho
import matplotlib.pyplot as plt
import time

N=988
THRESHOLD = pow(10, -9)
MAX_ITERATION=1000


# ------------------------Zadanie B------------------------

# A = Matrix(N,N)
# b = Matrix(N)

# #Jacobi method
# start = time.time()
# x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
# end = time.time()
# print(f"Jacobi time:{end-start}")

# #Gauss method
# start = time.time()
# x = gauss(A, b, THRESHOLD, MAX_ITERATION)
# end = time.time()
# print(f"Gauss time:{end-start}")



# ------------------------Zadanie C------------------------
# Matrix.a1 = 3
# Matrix.a2 = -1
# Matrix.a3 = -1
# A = Matrix(N,N)
# b = Matrix(N)
# x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
# x = gauss(A, b, THRESHOLD, MAX_ITERATION)

# ------------------------Zadanie D------------------------
# Matrix.a1 = 3
# Matrix.a2 = -1
# Matrix.a3 = -1
# A = Matrix(N, N)
# b = Matrix(N)
# x = factLU(A, b, THRESHOLD)



'''
test = [[2,1,1,0],
        [4,3,3,1],
        [8,7,9,5],
        [6,7,9,8],]
A = Matrix(4,4,test)
b = Matrix(4)
x = factLU(A, b, THRESHOLD, MAX_ITERATION)
print(x)
x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
print(x)
x = gauss(A, b, THRESHOLD, MAX_ITERATION)
print(x)
'''

# ------------------------Zadanie E------------------------
# sizes = np.array([100,500,1000,2000,3000])
# plots = np.zeros((3,5))
# print(plots)
# i = 0
# for N in sizes:
#
#         A = Matrix(N,N)
#         b = Matrix(N)
#         #Jacobi method
#         start = time.time()
#         x = jacobi(A, b, THRESHOLD, MAX_ITERATION)
#         end = time.time()
#         t = end-start
#         plots[0][i] = t
#
#         #print(f"Jacobi time:{t}")
#
#         #Gauss method
#         start = time.time()
#         x = gauss(A, b, THRESHOLD, MAX_ITERATION)
#         end = time.time()
#         t = end - start
#         plots[1][i] = t
#
#         #print(f"Gauss time:{t}")
#
#         # FactLU method
#         start = time.time()
#         x = factLUCho(A, b, THRESHOLD)
#         end = time.time()
#         t = end - start
#         plots[2][i] = t
#         #print(f"factLU time:{t}")
#
#         i+=1
#
# print(plots)
# x = np.arange(1,6,1)
# plt.plot(sizes, plots[0], 'r', label='Jacobi')
# plt.plot(sizes, plots[1], 'g', label='Gauss-Seidel')
# plt.plot(sizes, plots[2], 'b', label='Cholesky factorization')
#
# plt.xticks(sizes)
# plt.title("Comparison of time used by algorithms while working with various data size")
# plt.legend()
# plt.xlabel("Size of matrix [NxN]")
# plt.ylabel("Time [s]")
# plt.show()





'''
test = [[3,-1,1,0],
        [1,3,1,1],
        [1,1,3,1],
        [0,1,1,3]]
A = Matrix(4,4,test)
b = Matrix(4)
x = factLU(A, b, THRESHOLD)
print(x)
'''