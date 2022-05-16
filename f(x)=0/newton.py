import math


def deriv (f, x, h =1e-6):
    f_prime =(f(x + h) - f(x)) /  h
    return f_prime

def newton (f,x0, epsilon=1.e-6):

    while abs(f(x0)) > epsilon:
        x = x0 - ( f(x0) / deriv(f, x0))
    return x

f = lambda x: math.exp(-x/4)*(2-x)-1
print(newton(f,3))

