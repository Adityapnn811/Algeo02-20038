import numpy as np
from decimal import *

# Fungsi yang menentukan nilai eigen dengan qr algorithm
def eigenValues(matrix):
    # Iterasi pertama lakukan secara manual
    q, r = np.linalg.qr(matrix)
    S = q
    A = np.matmul(r, q)
    for i in range(20):
        q, r = np.linalg.qr(A)
        S = np.matmul(S, q)
        A = np.matmul(r, q)
    # Coba buletin nilai eigen vectornya
    # baris = np.shape(S)[0]
    # kolom = np.shape(S)[1]
    # for i in range(baris):
    #     for j in range(kolom):
    #         S[i][j] = round(S[i][j], 3)
    # Isolasi nilai eigen yg berada di diagonal utama
    eigen_val = []
    for i in range(len(A[0])):
        eigen_val.append(A[i][i])
    return eigen_val, S

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

# print(eigenValues(matrix))