from Matrix import Matrix
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
    D = A.diag()
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
    L, U = A.fact_LU()
    print(f"L={L}")
    print(f"U={U}")
