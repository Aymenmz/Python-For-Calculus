import math


def lagrange(f, a, b, eps=10**(-6)):
    x = (b * f(a) - a * f(b)) / (f(a) - f(b))

    while abs(f(x)) > eps:
        if (f(a) * f(x) <= 0):
            b = x
        else:
            a = x
        x = (b * f(a) - a * f(b)) / (f(a) - f(b))

    return x

def lagrangeRec(f, a, b, eps=10**(-6)):
    x = (b*f(a) - a*f(b)) / (f(a) - f(b))

    if abs(f(x)) > eps:
        if(f(a) * f(x) <= 0):
            b = x
        else:
            a = x
        return lagrangeRec(f, a, b)
    return x

f = lambda x: x-math.exp(-x)
sol = lagrange(f, -1, 2)
sol1 = lagrangeRec(f, -1, 2)
print(sol, sol1)
