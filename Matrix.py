import math


class Matrix:
    a1 = 13
    a2 = a3 = -1
    f = 8

    def __init__(self, m, n=1):
        self.m = m
        self.n = n
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
        for m in range(self.m):
            for n in range(self.n):
                self.mat[m][n] += other.mat[m][n]
        return self.mat

    def __mul__(self, other):
        if self.n != other.m:
            return
        print(self.m)
        mat = []
        for m in range(self.m):
            row = []
            for k in range(other.n):
                sum = 0
                for n in range(self.n):
                    sum += self.mat[m][n] * other.mat[n][k]
                row.append(sum)
            mat.append(row)

        return mat

    def solve(self, vector):
        solution = [vector.mat[0][0]/self.mat[0][0]]

        for i in range(1,self.m):
            sum = 0
            for j in range(self.n, i-1):
                sum+=self.mat[i][j]*solution[j]
            solution.append((vector.mat[i][0]-sum)/self.mat[i][i])

        return solution

