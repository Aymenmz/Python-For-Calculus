import numpy as np
import matplotlib.pyplot as plt


def eulerExpl(f, a, b, y0, n):
    y = [y0] * n  # y=[y0,y0,y0,y0,y0,y0,y0,y0,y0,...,y0,y0]
    T = [a] * n  # T=[a,a,a,a,a,a,a,a,a,a,a,a,a,...,a,a,a,a]
    h = (b - a) / n
    for i in range(0, n - 1, 1):
        y[i + 1] = y[i] + h * f(y[i] + h * f(y[i], T[i]), T[i] + h)
        T[i + 1] = T[i] + h
    return y




