"""
    Q1. Pour quelles valeurs du couple (a,b ) retrouve-t-on la méthode d'Euler ?
        a = t0 , b = t0 + T
"""

"""
    Q2. Écrire la fonction def euler(f ,y0,Lt) : qui prend en paramètres la fonction f, la condition initiale
        y0 et la liste Lt des réels correspondant aux valeurs de ti et qui retourne la liste [y0, y1, y2, …, yn-1] la
        solution de l'équation différentielles y' (t)= f (y(t),t).
"""


def euler(f, y0, Lt):
    n = len(Lt)
    Y = [y0] * n

    for i in range(n):
        Y[i + 1] = Y[i] + f(Y[i], Lt[i])
    return Y


'''
    Écrire la fonction def heun(f, t0,T,y0,N) : qui prend en paramètres la fonction f, la condition initiale
    t0, la valeur finale du temps T, y0 la valeur de f en t0 et le nombre de noeuds N et qui retourne la liste
    [y0, y1, y2, …, yn-1] la solution de l'équation différentielles y' (t)= f (y(t),t).
'''


def Heun(f, t0, y0, T, N):
    h = T / N
    tt = [t0 + i * h for i in range(N + 1)]
    Y = []
    y = y0
    for t in tt:
        k1 = f(t, y)
        k2 = f(t + h, h * k1)
        y += h * (k1 + k2) / 2
        Y.append(y)
    return tt, Y















