import math
import numpy as np
from sympy import *

def eigenValues(matrix):
    A = Symbol('A')
    mat = Matrix(matrix)
    shape = np.shape(matrix)
    # Buat matriks identitas dot A sesuai ukuran matrix
    AI = [[int(0) for j in range(shape[1])] for i in range(shape[0])]
    for i in range(shape[0]):
        AI[i][i] = 1 * A
    AI = Matrix(AI)
    # Buat matrix A.I - mat
    mat = AI - mat
    # Cari determinan mat
    det = mat.det()
    # Cari akarnya, sehingga ketemu nilai eigen
    akar = solve(det)
    return akar


# DRIVER
# matrix = [[3, -2, 0],
#           [-2, 3, 0],
#           [0, 0, 5]]

#
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

# print(eigenValues(matrix)[6])