class Matrix:
    a1 = 13
    a2 = a3 = -1
    def __init__(self, m, n=1):
        self.m = m
        self.n = n
        self.mat = self.create_matrix()
    
    def create_matrix(self):
        matrix = []
        for m in range(self.m):
            matrix_temp = []
            for n in range(self.n):
                if m==n:
                    matrix_temp.append(self.a1)
                elif abs(m-n)==1:
                    matrix_temp.append(self.a2)
                elif abs(m-n)==2:
                    matrix_temp.append(self.a3)
                else:
                    matrix_temp.append(0)
            matrix.append(matrix_temp)
        return matrix
    
    def __str__(self):
        return str(self.mat)