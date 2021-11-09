import numpy as np

# Fungsi yang menentukan nilai eigen dengan qr algorithm
def eigenValues(matrix):
    # Iterasi pertama lakukan secara manual
    q, r = np.linalg.qr(matrix)
    A = np.matmul(r, q)
    for i in range(39):
        q, r = np.linalg.qr(A)
        A = np.matmul(r, q)

    # Isolasi nilai eigen yg berada di diagonal utama
    eigen_val = []
    for i in range(len(A[0])):
        eigen_val.append(round(A[i][i], 5))
    return eigen_val

# matrix = [[49,  49,  49, 49, 49, 49, 49, 49, 49, 49],
#  [ 49, 118, 118, 118, 118, 118, 118, 118, 118, 49],
#  [ 49, 118, 49, 49, 49, 49, 49, 49, 118, 49],
#  [ 49, 118, 49, 118, 118, 118, 118, 49, 118, 49],
#  [ 49, 118, 49, 118, 49, 49, 118, 49, 118, 49],
#  [ 49, 118, 49, 118, 49, 49, 118, 49, 118, 49],
#  [ 49, 118, 49, 118, 118, 118, 118, 49, 118, 49],
#  [ 49, 118, 49, 49, 49, 49, 49, 49, 118, 49],
#  [ 49, 118,118, 118, 118, 118, 118, 118, 118, 49],
#  [ 49, 49, 49, 49, 49, 49, 49, 49, 49, 49]]
# matrix = [[10, 0, 2],
#           [0, 10, 4],
#           [2, 4, 2]]
# matrix = [[11, 1],
#           [1, 11]]

# print(qrFactor(matrix))
# print(eigenValues(matrix))