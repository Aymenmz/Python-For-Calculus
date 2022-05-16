
def trapezes(f, a, b, n=50):
    h = (b-a)/n
    s = 0
    for i in range(n):
        xi = a + i*h
        s += f(xi) + f(xi+h)
    return (h/2) * s

f = lambda x : x
res = trapezes(f, 0, 1)
print(res)