from Matrix import Matrix
import copy
def jacobi(A, b, threshold=pow(10,-9), max_iter=1000):
    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    x_new = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    for iteration in range(max_iter):
        for i in range(A.m):
            sum = 0
            for j in range(A.n):
                if j != i:
                    sum += A.mat[i][j] * x.mat[j][0]
            x_new.mat[i][0] = (b.mat[i][0] - sum) / A.mat[i][i]
        res = A*x_new-b
        x = x_new.copy()
        if all(abs(res.mat[i][0]) >= threshold for i in range(A.m)):
            return x

    return x

def gauss(A, b, threshold=pow(10,-9), max_iter=1000):
    D = A.diag()
    L = A.tril()
    U = A.triu()

    x = Matrix(b.m, 1, [[0] for _ in range(b.m)])
    for iteration in range(max_iter):
        x = (D-L).solve(U*x)+(D-L).solve(b)
        if all(abs(x.mat[i][0]) >= threshold for i in range(A.m)):
            return x
    return x