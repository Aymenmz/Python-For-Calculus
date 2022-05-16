"""
    i € [|j,n-1|] tel que |ai,j|=max{|ak,j| }, k € [|j,n-1|]
"""


def pivot(A, j):
    i = j
    n = len(A)
    for i in range(n - 1):
        for k in range(n - 1):
            if abs(A[i][j]) < abs(A[k][j]):
                i = k

    return i


def echanger(A, i, j):
    n = len(A)

    for k in range(n):
        A[i][k], A[j][k] = A[j][k], A[i][k]


def Transvection(A, i, j, c):
    for k in range(len(A)):
        A[i][j] = A[i][j] - c * A[k][j]

    return A


"""
    Écrire une fonction Triang qui prend en paramètre une matrice A et un vecteur b, 
    et qui revoie A0et b0 tels que A0 soit triangulaire supérieure et que les systèmes Ax = b et A0 x = b0 soientéquivalents.
"""


def Triang(A, B):
    n = len(A)
    for j in range(n - 1):
        i = pivot(A, j)
        echanger(A, i, j)
        B[i], B[j] = B[j], B[i]

        for k in range(j + 1, n):
            c = A[k][j] / A[j][j]
            Transvection(A, k, j, c)
            B[k] = B[k] - c * B[j]


"""
    Écrire une fonction ResolutionT qui prend en paramètre une matrice triangulaire supérieure A etun vecteur b et qui, 
    sous réserve que le système soit de Cramer, revoie l'unique vecteur x tel queAx = b
"""


def ResolutionT(A, B):
    n = len(A)
    X = [] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n, 1):
            s += A[i][j] * X[j]

        X[i] = (B[i] - s) / A[i][i]
    return X



def estTriang(A):
    for i in range(len(A)):
        for j in range(i):
            if A[i][j] != 0:
                return False

    return True


def Gauss(A, B):
    Triang(A, B)
    X = ResolutionT(A, B)
    return X


A = [[1, 1, 1], [0, 5, 1], [0, 0, 8]]
B = [3, 4, 16]
X = Gauss(A, B)
print(X)
