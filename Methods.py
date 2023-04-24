import numpy as np
import matplotlib.pyplot as plt

from Matrix import Matrix
import time
import copy
import math
def jacobi(A, b, threshold=pow(10,-9), max_iter=300):
    D = A.diag()
    L = A.tril().minus()
    U = A.triu().minus()

    vec_res = np.zeros(max_iter)

    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    comp1 = (L + U)
    for iteration in range(max_iter):
        comp2 = comp1*x+b
        x = D.solve2(comp2)
        res = A*x - b
        vec_res[iteration] = res.max()

        if all(abs(res.mat[i][0]) <= threshold for i in range(A.m)):
            print(f"Jacobi iteration: {iteration}")
            #print(f"res={res}")
            vec_res = vec_res[:iteration]
            xtest = np.arange(0, iteration, 1)
            plt.plot(xtest, vec_res)
            plt.xlabel("Number of iteration")
            plt.ylabel("Log value of residuum")
            plt.title("Residuum for Jacobi method")
            plt.yscale('log')
            plt.show()
            return x


    x_ = np.arange(0, max_iter, 1)
    plt.plot(x_, vec_res)
    plt.xlabel("Number of iteration")
    plt.ylabel("Log value of residuum")
    plt.title("Residuum for Jacobi method")
    plt.yscale('log')
    plt.show()
    print(f"jacobi: {max_iter}")
    return x

def gauss(A, b, threshold=pow(10,-9), max_iter=1000):
    #D = A.diag()
    L = A.tril()
    U = A.triu()

    vec_res = np.zeros(max_iter)

    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    for iteration in range(max_iter):
        for i in range(A.m):
            m1 = Matrix(1, L.n, [L.mat[i]])
            s1 = m1*x
            m2 = Matrix(1, U.n, [U.mat[i]])
            s2 = m2*x
            x.mat[i][0] = (b.mat[i][0]-s1.mat[0][0]-s2.mat[0][0])/A.mat[i][i]
        res = A * x - b

        vec_res[iteration] = res.max()

        if all(abs(res.mat[i][0]) <= threshold for i in range(A.m)):
            #print(f"Gauss iteration: {iteration}")
            #print(f"res={res}")
            vec_res = vec_res[:iteration]
            x_ = np.arange(0, iteration, 1)
            plt.plot(x_, vec_res)
            plt.xlabel("Number of iteration")
            plt.ylabel("Log value of residuum")
            plt.title("Residuum for Gauss method")
            plt.yscale('log')
            plt.show()
            return x

    x_ = np.arange(0, max_iter, 1)
    plt.plot(x_, vec_res)
    plt.xlabel("Number of iteration")
    plt.ylabel("Log value of residuum")
    plt.title("Residuum for Gauss method")
    plt.yscale('log')
    plt.show()
    print(f"jacobi: {max_iter}")
    #print(f"gauss: {max_iter}")
    return x

def factLU(A, b, threshold=pow(10,-9)):
    L, U = A.fact_LU()
    n = A.n
    y = Matrix(n, 1, [[0] for _ in range(n)])
    x = Matrix(n, 1, [[0] for _ in range(n)])

    for i in range(n):
        sum_L = sum(L.mat[i][j] * y.mat[j][0] for j in range(i))
        y.mat[i][0] = (b.mat[i][0] - sum_L) / L.mat[i][i]

    for i in reversed(range(n)):
        sum_U = sum(U.mat[i][j] * x.mat[j][0] for j in range(i + 1, n))
        x.mat[i][0] = (y.mat[i][0] - sum_U) / U.mat[i][i]

    res = A * x - b

    print(f"Norma residuum: {res.max()}")
    return x

def factLUCho(A, b, threshold=pow(10,-9)):
    L, LT = A.fact_LU_cho()
    n = A.n
    y = Matrix(n, 1, [[0] for _ in range(n)])
    x = Matrix(n, 1, [[0] for _ in range(n)])

    for i in range(n):
        sum_L = sum(L.mat[i][j] * y.mat[j][0] for j in range(i))
        y.mat[i][0] = (b.mat[i][0] - sum_L) / L.mat[i][i]

    for i in reversed(range(n)):
        sum_U = sum(LT.mat[i][j] * x.mat[j][0] for j in range(i + 1, n))
        x.mat[i][0] = (y.mat[i][0] - sum_U) / LT.mat[i][i]

    return x
