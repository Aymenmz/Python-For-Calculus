import matplotlib.pyplot as plt


def eulerImpl(f,a,b,y0,n):
    y=[y0]*n#y=[y0,y0,y0,y0,y0,y0,y0,y0,y0,...,y0,y0]
    T=[a]*n#T=[a,a,a,a,a,a,a,a,a,a,a,a,a,...,a,a,a,a]
    h=(b-a)/n
    for i in range(0,n-1,1):
        y[i+1]=y[i]+h*f(y[i],T[i])
        T[i+1]=T[i]+h
    return y,T



def func(t, y):
    return 1/(2*y+1)
y, t = eulerImpl(func, 1, 10, 0, 200)
print(t)
plt.plot(t, y)
plt.show()

