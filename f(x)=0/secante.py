import math


def secante(f, xi, xj, erreur=0.00001):
    while abs(f(xj)) > erreur:
        # xz = xj - [ f(xj) * (xj - xi) ] / (f(xj) - f(xi))
        xz = xj - f(xj) * (xj - xi) / (f(xj) - f(xi))
        xi = xj
        xj = xz

    return xj


f = lambda x: x - math.exp(-x)
print(secante(f, 0, 1))
