# I = sum(i=0 à n-1) f(Xi) * h
# h = (b-a) / n
# Xi = a + i*h


def rectangles(f, a, b, n=50):
    h = (b - a) / n
    s = 0
    for i in range(n):
        xi = a + i * h
        s += f(xi + h / 2)
    return h * s


f = lambda x: x
res = rectangles(f, 0, 1)
print(res)
