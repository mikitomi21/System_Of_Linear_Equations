import math


class Matrix:
    a1 = 13
    a2 = a3 = -1
    f = 8

    def __init__(self, m, n=1, mat=None):
        self.m = m
        self.n = n

        if mat:
            self.mat = mat
        else:
            self.mat = self.create()



    def create(self):
        if self.n == self.m:
            return self.create_matrix()
        if self.n == 1:
            return self.create_vector()

    def create_matrix(self):
        matrix = []
        for m in range(self.m):
            matrix_temp = []
            for n in range(self.n):
                if m == n:
                    matrix_temp.append(self.a1)
                elif abs(m - n) == 1:
                    matrix_temp.append(self.a2)
                elif abs(m - n) == 2:
                    matrix_temp.append(self.a3)
                else:
                    matrix_temp.append(0)
            matrix.append(matrix_temp)
        return matrix

    def create_vector(self):
        vector = []
        for _ in range(self.m - 1):
            vector.append([0])
        vector.append([math.sin(self.n * (self.f + 1))])
        return vector

    def __str__(self):
        return str(self.mat)

    def __add__(self, other):
        matrix = []
        for m in range(self.m):
            new_matrix = []
            for n in range(self.n):
                new_matrix.append(self.mat[m][n]+other.mat[m][n])
            matrix.append(new_matrix)
        return Matrix(self.m, self.n, matrix)

    def __sub__(self, other):
        matrix = []
        for m in range(self.m):
            new_matrix = []
            for n in range(self.n):
                new_matrix.append(self.mat[m][n] - other.mat[m][n])
            matrix.append(new_matrix)
        return Matrix(self.m, self.n, matrix)

    def __abs__(self):
        matrix = []
        for m in range(self.m):
            new_matrix = []
            for n in range(self.n):
                new_matrix.append(abs(self.mat[m][n]))
            matrix.append(new_matrix)
        return Matrix(self.m, self.n, matrix)

    def __mul__(self, other):
        if self.n != other.m:
            return
        mat = []
        for m in range(self.m):
            row = []
            for k in range(other.n):
                sum = 0
                for n in range(self.n):
                    sum += self.mat[m][n] * other.mat[n][k]
                row.append(sum)
            mat.append(row)

        return Matrix(self.m, other.n, mat)

    def minus(self):
        for m in range(self.m):
            for n in range(self.n):
                self.mat[m][n] = -1*self.mat[m][n]
        return Matrix(self.m, self.n, self.mat)
    def matmax(self):
        max_val = float('-inf')
        for m in range(self.m):
            for n in range(self.n):
                if abs(self.mat[m][n]) > max_val:
                    max_val = abs(self.mat[m][n])
        return max_val

    def solve(self, b, x):
        solution = []
        for i in range(1, self.m):
            sum = 0
            for j in range(self.n, i):
                sum += self.mat[i][j] * x.math[j][0]
            solution.append([(b.mat[i][0] - sum) / self.mat[i][i]])

        return Matrix(b.m, b.n, solution)

    def solve2(self,mat2):
        matrix = []
        for m in range(self.m):
            matrix_temp = []
            for n in range(self.n):
                if m==n:
                    matrix_temp.append(1/self.mat[m][n])
                else:
                    matrix_temp.append(0)
            matrix.append(matrix_temp)
        mat1 = Matrix(self.m, self.n, matrix)

        return mat1*mat2

    def copy(self):
        matrix = []
        for m in range(self.m):
            matrix_temp = []
            for n in range(self.n):
                matrix_temp.append(self.mat[m][n])
            matrix.append(matrix_temp)
        return Matrix(self.m, self.n, matrix)

    def diag(self):
        matrix = []
        for m in range(self.m):
            matrix_temp = []
            for n in range(self.n):
               if n==m:
                   matrix_temp.append(self.mat[m][n])
               else:
                   matrix_temp.append(0)
            matrix.append(matrix_temp)
        return Matrix(self.m, self.n, matrix)

    def triu(self):
        matrix = []
        for m in range(self.m):
            matrix_temp = []
            for n in range(self.n):
               if n>m:
                   matrix_temp.append(self.mat[m][n])
               else:
                   matrix_temp.append(0)
            matrix.append(matrix_temp)
        return Matrix(self.m, self.n, matrix)

    def tril(self):
        matrix = []
        for m in range(self.m):
            matrix_temp = []
            for n in range(self.n):
               if n<m:
                   matrix_temp.append(self.mat[m][n])
               else:
                   matrix_temp.append(0)
            matrix.append(matrix_temp)
        return Matrix(self.m, self.n, matrix)

    def unit(self):
        a1t = Matrix.a1
        a2t = Matrix.a2
        a3t = Matrix.a3

        Matrix.a1 = 1
        Matrix.a2 = Matrix.a3 = 0
        matrix = Matrix(self.m, self.n)

        Matrix.a1 = a1t
        Matrix.a2 = a2t
        Matrix.a3 = a3t

        return matrix

    def zero(self):
        a1t = Matrix.a1
        a2t = Matrix.a2
        a3t = Matrix.a3

        Matrix.a1 = Matrix.a2 = Matrix.a3 = 0
        matrix = Matrix(self.m, self.n)

        Matrix.a1 = a1t
        Matrix.a2 = a2t
        Matrix.a3 = a3t

        return matrix
    def fact_LU(self):
        U = self.copy()
        L = self.unit()
        for i in range(self.n-1):
            for j in range(i+1, U.m):
                if U.mat[i][i] == 0:
                    U.mat[i+1], U.mat[i] = U.mat[i], U.mat[i+1]
                if U.mat[i][i] == 0:
                    L.mat[j][i] = 0
                else:
                    L.mat[j][i] = U.mat[j][i]/U.mat[i][i]
                for k in range(i, U.m):
                    U.mat[j][k] = U.mat[j][k] - (L.mat[j][i]*U.mat[i][k])
        return L, U

    def trans(self):
        M = self.copy()
        for m in range(self.m):
            for n in range(self.n):
                M.mat[m][n] = self.mat[n][m]
        return M

    def fact_LU_cho(self):
        L = self.zero()
        for i in range(L.m):
            suma=sum(pow(L.mat[i][k],2) for k in range(i))
            L.mat[i][i] = math.sqrt(self.mat[i][i] - suma)
            for j in range(i,L.m):
                suma = sum(L.mat[j][k]*L.mat[i][k] for k in range(i))
                L.mat[j][i] = (self.mat[j][i] - suma) / L.mat[i][i]
        return L, L.trans()


    def max(self):
        maximum = 0
        for i in range(self.m):
            if abs(self.mat[i][0]) > maximum:
                maximum = abs(self.mat[i][0])
        return maximum