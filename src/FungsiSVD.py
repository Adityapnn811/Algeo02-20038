import math
from FungsiEigen import *

def matriksVdanS(A):
  baris = np.shape(A)[0]
  kolom = np.shape(A)[1]
  AT = np.transpose(A)
  ATA = np.matmul(AT, A)
  EigVal, V = eigenValues(ATA)
  S = [[0 for j in range(kolom)]for i in range(baris)]
  i = 0
  j = 0
  while i < baris and j < kolom:
    S[i][i] = math.sqrt(abs(EigVal[i]))
    i += 1
    j += 1
  return V, S, EigVal

def MatriksU(A, V, S, EigVal):
  baris = np.shape(S)[0]
  kolom = np.shape(S)[1]
  # Kita iterasi sampe nilai singular dalam matriks S habis
  # membuat matriks U berdasarkan rumus U[i] = A*V[i]/S[i]
  U = []
  i = 0
  j = 0
  while i < baris and j < kolom:
    Ui = np.matmul(A, V[i]) / math.sqrt(abs(EigVal[i]))
    U.append(Ui)
    i += 1
    j += 1
  return np.transpose(U)

def compress(matriks, percentage):
  baris = np.shape(matriks)[0]
  kolom = np.shape(matriks)[1]
  k = int((percentage/100) * (baris*kolom/(baris + 1 + kolom)))
  V, S, EigVal = matriksVdanS(matriks)
  VT = np.transpose(V)
  U= MatriksU(matriks, VT, S, EigVal)
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

# matriks =  [[ 6, 88, 53, 15, 61],
#  [79, 53, 94, 51, 96],
#  [77, 93, 66, 39, 77],
#  [54, 25, 75, 44, 38]]
#
# V, S, Eig = matriksVdanS(matriks)
# VT = np.transpose(V)
# U = MatriksU(matriks, VT, S, Eig)
# mat = np.matmul(U, S)
# mat = np.matmul(mat, VT)
# print(U)
# print(S)
# print(V)
# print(mat)