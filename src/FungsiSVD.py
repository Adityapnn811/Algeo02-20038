import math
from numpy import linalg
import numpy as np
from sympy import *
import sympy as sp
from FungsiEigen import *

def nilaiUdanS(matriks):
  baris = np.shape(matriks)[0]
  kolom = np.shape(matriks)[1]
  matriks = Matrix(matriks)
  multiply = matriks * matriks.T
  lamda, eigenVec = eigenValues(multiply)
  # Buat matriks S dulu
  S = [[0 for j in range(kolom)]for i in range(baris)]
  i = 0
  j = 0
  while i < baris and j < kolom:
    S[i][j] = abs(lamda[i])**0.5
    i += 1
    j += 1
  return eigenVec, S

def nilaiV(matriks):
  matriks = Matrix(matriks)
  matriks_T = matriks.T
  multiply = matriks_T * matriks
  lamda, eigenVec = eigenValues(multiply)
  return eigenVec

def compress(matriks, percentage):
  baris = np.shape(matriks)[0]
  kolom = np.shape(matriks)[1]
  minim = min(baris, kolom)
  k = int(percentage/100 * minim)
  U, S = nilaiUdanS(matriks)
  VT = np.transpose(nilaiV(matriks))
  U_comp = []
  S_comp = [[0 for i in range(k)] for j in range(k)]
  VT_comp = []
  # Ambil k kolom dari U
  U = np.transpose(U)
  for i in range(k):
    U_comp.append(U[i])
  U_comp = np.transpose(U_comp)
  # Ambil k kolom dan k baris dari S
  for i in range(k):
    for j in range(k):
      S_comp[i][j] = S[i][j]
  # Ambil k baris dari VT
  for i in range(k):
    VT_comp.append(VT[i])
  # Lakukan perkalian
  mat = np.matmul(U_comp, S_comp)
  mat = np.matmul(mat, VT_comp)
  return mat


# matriks =  [[3, 1, 1],
#            [-1, 3, 1]]
# #
# print(nilaiV(matriks))