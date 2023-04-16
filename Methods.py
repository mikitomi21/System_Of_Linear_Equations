from Matrix import Matrix
import time
import copy
def jacobi(A, b, threshold=pow(10,-9), max_iter=1000):
    D = A.diag()
    L = A.tril().minus()
    U = A.triu().minus()

    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    comp1 = (L + U)
    for iteration in range(max_iter):
        comp2 = comp1*x+b
        x = D.solve2(comp2)
        res = A*x - b
        if all(abs(res.mat[i][0]) <= threshold for i in range(A.m)):
            print(f"jacobi: {iteration}")
            #print(f"res={res}")
            return x

    print(f"jacobi: {max_iter}")
    return x

def gauss(A, b, threshold=pow(10,-9), max_iter=1000):
    #D = A.diag()
    L = A.tril()
    U = A.triu()

    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    for iteration in range(max_iter):
        for i in range(A.m):
            m1 = Matrix(1, L.n, [L.mat[i]])
            s1 = m1*x
            m2 = Matrix(1, U.n, [U.mat[i]])
            s2 = m2*x
            x.mat[i][0] = (b.mat[i][0]-s1.mat[0][0]-s2.mat[0][0])/A.mat[i][i]
        res = A * x - b
        if all(abs(res.mat[i][0]) <= threshold for i in range(A.m)):
            print(f"gauss: {iteration}")
            #print(f"res={res}")
            return x

    print(f"gauss: {max_iter}")
    return x

def factLU(A, b, threshold=pow(10,-9), max_iter=1000):
    start = time.time()
    L, U = A.fact_LU()
    end = time.time()
    print(f"L+U:{end - start}")
    #print(f"L={L}")
    #print(f"U={U}")
    n = A.n
    y = Matrix(n, 1, [[0] for _ in range(n)])
    x = Matrix(n, 1, [[0] for _ in range(n)])

    start = time.time()
    for iteration in range(max_iter):
        for i in range(n):
            sum_L = sum(L.mat[i][j] * y.mat[j][0] for j in range(i))
            y.mat[i][0] = (b.mat[i][0] - sum_L) / L.mat[i][i]

        for i in reversed(range(n)):
            sum_U = sum(U.mat[i][j] * x.mat[j][0] for j in range(i + 1, n))
            x.mat[i][0] = (y.mat[i][0] - sum_U) / U.mat[i][i]


        res = A * x - b
        if all(abs(res.mat[i][0]) <= threshold for i in range(A.m)):
            print(f"factLU: {iteration}")
            end = time.time()
            print(f"iteracje:{end - start}")
            # print(f"res={res}")
            return x

    print(f"factLU: {max_iter}")
    return x
