def rectangles(f,a,b,n=50):
    h=(b-a)/n
    s=0
    for i in range(n):
        xi=a+i*h
        s+=f(xi+h/2)
    return (h)*s

def trapezes(f,a,b,n=50):
    h=(b-a)/n
    s=0
    for i in range(n):
        xi=a+i*h
        s+=f(xi)+f(xi+h)
    return (h/2)*s
def simpsons(f,a,b,n=50):
    h=(b-a)/n
    s=0
    for i in range(n):
        xi=a+i*h
        s+=f(xi)+4*f(xi+h/2)+f(xi+h)
    return (h/6)*s

def fa(x):
    return x
def fb(x):
    return sin(x)**5
def fc(x):
    return log(x+1)-x**3+4
from math import *
print("qa=",rectangles(fa,0,1))
print("qb=",trapezes(fb,0,1))
print("qc=",simpsons(fc,0,1))

print("qa=",trapezes (fa,0,1))
print("qb=",rectangles(fb,0,1))
print("qc=",trapezes(fc,0,1))

