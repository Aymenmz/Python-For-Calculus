def gauche(i):
    return 2 * i + 1


def droite(i):
    return 2 * i + 2


def pere(i):
    return (i - 1) // 2


def maximum(i, T, limite):
    iMax = i
    g = gauche(i)
    d = droite(i)

    if g < limite and T[g] > T[iMax]:
        iMax = g

    elif d < limite and T[d] > T[iMax]:
        iMax = d

    return iMax


def echanger(T, i, j):
    tmp = T[i]
    T[i] = T[j]
    T[j] = tmp


def entasserRec(T, i, limite):
    iMax = maximum(i, T, limite)
    if iMax != i:
        echanger(T, i, iMax)
        entasserRec(T, iMax, limite)


def entasser(T, i, limite):
    iMax = maximum(i, T, limite)

    if iMax != i:
        echanger(T, i, iMax)
        i = iMax
        iMax = maximum(i, T, limite)


def construireTas(T):
    n = len(T)
    for i in range((n - 1) // 2, -1, -1):
        entasser(T, i, n)


def estUnTas(T):
    for i in range(len(T)):
        if T[pere(i)] < T[i]:
            return False
        return True


def trierTas(T):
    n = len(T)
    for i in range(n - 1, 0, -1):
        echanger(T, 0, i)
        entasser(T, 0, i)


def triParTas(T):
    construireTas(T)
    trierTas(T)
