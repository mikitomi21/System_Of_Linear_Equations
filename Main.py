from Matrix import Matrix
N = 988
N_TEST = 5

A = Matrix(N_TEST,N_TEST)
B = Matrix(N_TEST,N_TEST)

b = Matrix(N_TEST)
print(b)
print(A.solve(b))
