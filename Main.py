from Matrix import Matrix
from Methods import jacobi, gauss, factLU, factLUCho
import time

#N = 988
N=988
THRESHOLD = pow(10, -9)
MAX_ITERATION=100

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

'''
for N in [100,500,1000,2000,3000]:
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

        # FactLU method
        start = time.time()
        x = factLU(A, b, THRESHOLD)
        end = time.time()
        print(f"factLU time:{end - start}")

'''


N_TEST = 1000
A = Matrix(N_TEST,N_TEST)
b = Matrix(N_TEST)

start = time.time()
x = factLU(A, b, THRESHOLD)
end = time.time()
print(end-start)

start = time.time()
x = factLUCho(A, b, THRESHOLD)
end = time.time()
print(end-start)

# test = [[3,-1,1,0],
#         [1,3,1,1],
#         [1,1,3,1],
#         [0,1,1,3]]
# A = Matrix(4,4,test)
# b = Matrix(4)
# x = factLU(A, b, THRESHOLD)
# print(x)