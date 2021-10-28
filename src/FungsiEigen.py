import math
import numpy as np

# Membuat fungsi yang memfaktorkan matriks dengan qr factorization
def qrFactor(matrix):
    partial_basis = []
    # transpose matrix yang baru dateng dulu biar ngolahnya gampang
    matrix = np.transpose(matrix)
    # Append baris pertama ke partial_basis lgsg karena dia baris pertama
    partial_basis.append(matrix[0])
    # Buat partial basis nya dulu
    for i in range(1, len(matrix)):
        # Inisiasi vektor basis v dengan matrix baris ke-i
        v = matrix[i]
        for base in partial_basis:
            base_magnitude = base.dot(base)
            v = np.subtract(v, np.dot((np.dot(v, base) / base_magnitude), base))
        partial_basis.append(v)

    # Normalized semua basis di partial_basis
    for i in range(0, len(partial_basis)):
        base_magnitude = np.sqrt(partial_basis[i].dot(partial_basis[i]))
        partial_basis[i] = np.dot(1/base_magnitude, partial_basis[i])
    # transpose dulu partial basis biar jadi vektor kolom
    partial_basis = np.transpose(partial_basis)
    # Udah jadi Q

    # matrix awal di transpose lagi biar balik semula
    matrix = np.transpose(matrix)

    # Mencari R
    R = np.matmul(np.transpose(partial_basis), matrix)
    return partial_basis, R

# Fungsi yang menentukan nilai eigen dengan qr algorithm
def eigenValues(matrix):
    # Iterasi pertama lakukan secara manual
    q, r = qrFactor(matrix)
    A = np.matmul(r, q)
    for i in range(19):
        q, r = qrFactor(A)
        A = np.matmul(r, q)

    # Isolasi nilai eigen yg berada di diagonal utama
    eigen_val = []
    for i in range(len(A[0])):
        eigen_val.append(A[i][i])
    return eigen_val


# DRIVER
# matrix = [[2, 1, 0],
#           [1, 3, -1],
#           [0, -1, 6]]
# qrFactor(matrix)
# print(eigenValues(matrix))
