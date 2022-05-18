#from scipy.integrate import odeint
from pylab import *
from EquaDiff import eulerImpl, RK4, heun
from numpy import sin


def f(y, t):
    return sin(y(t))


a, b, h = 0, 5, 0.1
n = int((b - a) / h)
y0 = 1
T = linspace(a, b, n)
'''
y = odeint(f, y0, T)
subplot(2, 2, 1)
title("ODEINT")
plot(T, y)
'''

y = eulerImpl.eulerImpl(f, a, b, y0, n)
subplot(2, 2, 2)
title("EULER")
plot(T, y)

y = heun.heun(f, a, b, y0, n)
subplot(2, 2, 3)
title("HEUN")
plot(T, y)

y = RK4.RK4(f, a, b, y0, n)
subplot(224)
title("RK4")
plot(T, y)
xlabel("t(s)")
ylabel("MMM")
show()
