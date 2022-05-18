from numpy import *
from scipy.integrate import odeint
from pylab import *
from matplotlib import *

def f(y, t):
    return y


a, b, h = 0, 5, 0.1
y0 = 1
n = (b - a)//h

T = linspace(0, 1, 50)

y = odeint(f, a, b, y0, n)
subplot(2,2,1)
title("odeint")
plot(T, y)







xlabel('t')
ylabel('MMM')
show()
