import numpy as np


def pivot(A, j):
    i = j
    n = len(A)

    for k in range(j, n):
        if A[i][j] < abs(A[k][j]):
            i = k
    return k


def Echanger(A, i, j):
    tmp = A[i, :].copy()
    A[i, :] = A[j, :]
    A[j, :] = tmp


def Transvection(A, i, j, c):
    A[i, :] -= c * A[j, :]
    return A


def transvection_ligne(M, i, j, l):
    M[i] = [M[i][k] + l * M[j][k] for k in range(len(M[i]))]
    return M


def Triang(A, b):  # A matrcie, b: vecteur = list
    pass


def estTriang(A):
    for i in range(len(A)):
        for j in range(i):
            if (A[i][j] != 0):
                return False

    return True


A = np.arange(9).reshape(3, 3)
print(A)
# Echanger(A, 0, 2)
Transvection(A, 0, 1, 1)
print(A)
print(estTriang(A))
