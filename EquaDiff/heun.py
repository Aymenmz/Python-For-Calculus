"""

"""


def heun(f, a, b, y0, n):
    y = [y0] * n
    T = [a] * n
    h = (b - a) / n
    for i in range(0, n - 1, 1):
        y[i + 1] = y[i] + h / 2 * ( f(y[i], T[i]) + f(y[i] + h * f(y[i], T[i]), T[i] + h))
        T[i + 1] = T[i] + h
    return y
