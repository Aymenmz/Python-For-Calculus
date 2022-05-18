import math


def madichotomie(f, a, b, eps=10**(-6)):

    while abs(b-a) > eps:
        m = (a + b) / 2

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return (a+b)/2

def dichoRec(f, a, b, eps=10**(-6)):
    if abs(b-a) > eps:
        m = (a+b)/2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        return dichoRec(f, a, b)
    else:
        return (a+b)/2

f = lambda x: x-math.exp(-x)
sol = madichotomie(f, -1, 2)
sol1 = dichoRec(f, -1, 2)
print(sol, sol1)


