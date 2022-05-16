"""
    Q1. Pour quelles valeurs du couple (a,b ) retrouve-t-on la méthode d'Euler ?
        a = t0 , b = t0 + T
"""

"""
    Q2. Écrire la fonction def euler(f ,y0,Lt) : qui prend en paramètres la fonction f, la condition initiale
        y0 et la liste Lt des réels correspondant aux valeurs de ti et qui retourne la liste [y0, y1, y2, …, yn-1] la
        solution de l'équation différentielles y' (t)= f (y(t),t).
"""
import matplotlib.pyplot as plt

def euler(f, y0, Lt):
    a = Lt[0]
    b = Lt[-1]
    n = len(Lt)
    y = [y0] * n
    h = (b - a) / n

    for i in range(n):
        y[i+1] = y[i] + f(y[i], Lt[i])
    return y
def func(t, y):
    return 1/(2*y+1)
y, t = euler(func, 1, 10, 0, 200)
plt.plot(t, y)
plt.show()
