class Matrix:
    a1 = 13
    a2 = -1
    a3 = -1
    def __init__(self, m, n=1):
        self.m = m
        self.n = n
        self.mat = self.create_matrix()
    
    def create_matrix(self):
        matrix = []
        for _ in range(self.m):
            matrix_temp = []
            for _ in range(self.n):
                matrix_temp.append(0)
            matrix.append(matrix_temp)
        return matrix
    
    def __str__(self):
        return str(self.mat)