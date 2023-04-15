from Matrix import Matrix
import copy
def jacobi(A, b, threshold=pow(10,-9), max_iter=1000):
    D = A.diag()
    L = A.tril().minus()
    U = A.triu().minus()

    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    comp1 = (L + U)
    for iteration in range(max_iter):
        test3 = comp1*x+b
        x = D.solve2(test3)
        res = A*x - b
        if all(abs(res.mat[i][0]) <= threshold for i in range(A.m)):
            print(f"jacobi: {iteration}")
            print(f"res={res}")
            return x

    print(f"jacobi: {iteration}")
    print(f"res={res}")
    return x

def gauss(A, b, threshold=pow(10,-9), max_iter=1000):
    D = A.diag()
    L = A.tril()
    U = A.triu()

    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    for iteration in range(max_iter):
        print(x)
        x_new = (D-L).solve(U*x,x)+(D-L).solve(b,x)
        x = x_new.copy()
        res = A * x - b
        if all(abs(res.mat[i][0]) <= threshold for i in range(A.m)):
            print(f"gauss: {iteration}")
            return x

    print(f"gauss: {iteration}")
    print(res)
    return x