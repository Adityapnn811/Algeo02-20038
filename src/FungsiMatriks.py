import numpy as np

def GaussElimination(matriks):
    matriks = np.matrix(matriks)
    matriks = matriks.tolist()
    b = np.shape(matriks)[0]
    k = np.shape(matriks)[1]
    b_pass = 0
    k_pass = 0
    b_ganti = 0
    while (b_pass < b and k_pass < k):
        if(matriks[b_ganti][k_pass] == 0):
            if (b_ganti == b - 1):
                b_ganti = b_pass
                k_pass += 1
            else:
                b_ganti = b_ganti + 1
        else:
            if (b_ganti != b_pass):
                temp_arr = matriks[b_ganti]
                matriks[b_ganti] = matriks[b_pass]
                matriks[b_pass] = temp_arr
            pembagi = matriks[b_pass][k_pass]
            # Jadiin leading one
            for j in range(0, k):
                matriks[b_pass][j] = matriks[b_pass][j]/pembagi
            # Kurangi baris lainnya
            # Cek apakah udah pass terakhir
            if (b_pass != b - 1):
                for i in range(b_pass + 1, b):
                    if (matriks[i][k_pass] != 0):
                        pengali = matriks[i][k_pass]
                        matriks[i][k_pass] = 0
                        for j in range(k_pass + 1, k):
                            matriks[i][j] -= matriks[b_pass][j] * pengali
            b_pass += 1
            k_pass += 1
            b_ganti = b_pass
    k_pass = 0
    b_pass = b - 1
    while (b_pass > -1 and k_pass < k):
        # cari leading one dari baris paling bawah
        if (matriks[b_pass][k_pass] != 1 and k_pass != k - 1):
            if (k_pass == k - 2):
                b_pass -= 1
                k_pass = 0
            else:
                k_pass += 1
        else:
            for i in range((b_pass - 1), -1, -1):
                if (matriks[i][k_pass] != 0):
                    pengali = matriks[i][k_pass]
                    matriks[i][k_pass] = 0
                    for j in range(k_pass + 1, k):
                        matriks[i][j] -= matriks[b_pass][j] * pengali
                        print(matriks)
            b_pass -= 1
            k_pass = 0
    matriks = np.matrix(matriks)
    return matriks

def isAllZeroRow(matriks, row):
    matriks = np.matrix(matriks)
    k = np.shape(matriks)[1]
    matriks = matriks.tolist()
    kolom_ke = 0
    allZero = True
    while kolom_ke < k and allZero:
        if (matriks[row][kolom_ke] != 0):
            allZero = False
        else:
            kolom_ke += 1
    #return boolean sama kolom ke berapa yang nilainya 1
    return allZero, kolom_ke

def searchTrueValue(list, col):
    # Fungsi akan mereturn nilai indeks dimana nilai list[indeks] = True
    isTrue = False
    while col < len(list) and not isTrue:
        if list[col] == True:
            isTrue = True
        else:
            col += 1
    return col

def getEigenVector(matriks):
    matriks = np.matrix(matriks)
    matriks = matriks.tolist()
    b = np.shape(matriks)[0]
    k = np.shape(matriks)[1] - 1 # soalnya kolom terakhir adalah augmentednya, jd buang aja
    baris_now = b - 1

    listEigenVec = []
    # buat array boolean seukuran kolom matriks - 1 (karena augmented) terus catet kolom mana aja yg BUKAN
    # jadi parametrik dengan cara cek leading one nya di kolom mana aja

    kol_parametrik = [True for i in range(k)]

    # Mulai dari baris paling bawah, klo barisnya baris 0, append sebuah array vektor eigen dengan 1 sesuai indeks baris
    # jadi klo yg allZeroRow di baris 4 dari total 6 baris, buat sebuah list yg memiliki nilai 1 di vektor[4], jadi
    # vektor = [0, 0, 0, 1, 0, 0] ntar sisanya dicek sampe baris teratas
    # ingat dia masih dalam bentuk horizontal, nanti harus di_transpose
    while (baris_now > -1):
        allZero, kolom_leadOne = isAllZeroRow(matriks, baris_now)
        if allZero:
            eigenVec = [0 for i in range(k)]
            listEigenVec.append(eigenVec)
        else:
            # Berarti semua nilai kolom ke-[kolom_leadOne] = 0 di semua eigenvec yg udah diappend pada listEigenvec
            kol_parametrik[kolom_leadOne] = False
        baris_now -= 1

    kolom_udah = 0
    for row in range(len(listEigenVec)):
        # nilai kol_parametrik[row] = 1 sesuai dengan dia True ato False
        kolom_now = searchTrueValue(kol_parametrik, kolom_udah)
        kolom_udah += kolom_now + 1
        listEigenVec[row][kolom_now] = 1
    baris_now = 0
    allZero, kolom_leadOne = isAllZeroRow(matriks, baris_now)
    while not allZero:
        # habis itu tinggal tambah negatif dari nilai di matriks setelah kolom lead_one pada row yang sama
        for col in range(kolom_leadOne + 1, k):
            if matriks[baris_now][col] != 0:
                # klo dia engga nol, berarti append ke listEigenVec. Cari row listEigenVec yg sesuai dengan kolom
                row = 0
                while row < len(listEigenVec):
                    if listEigenVec[row][col] == 1:
                        listEigenVec[row][kolom_leadOne] -= matriks[baris_now][col]
                        row += 1
                    else:
                        row += 1
        baris_now += 1
        allZero, kolom_leadOne = isAllZeroRow(matriks, baris_now)
    # normalisasi vektornya
    for i in range(len(listEigenVec)):
        magnitude = np.array(listEigenVec[i]).dot(listEigenVec[i])
        for j in range(len(listEigenVec[i])):
            listEigenVec[i][j] /= magnitude**0.5
    listEigenVec = np.array(listEigenVec)
    return listEigenVec




# matriks =  [[1,1,0,0,0],
#             [0,0,1,0,0],
#             [0,0,0,0,0],
#             [0,0,0,0,0]]
# matriks = [[-1, -1,0],
#            [0, 0,0]]
# print(getEigenVector(matriks))
# print(GaussElimination(matriks))
# print(isAllZeroRow(matriks, 1))