class Point:
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    @staticmethod
    def counter():
        return Point.counter

    def display(self):
        return self.x, self.y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)


print(Point.count)

p1 = Point(1, 3)
p2 = Point(1, 8)

print(Point.count)
print(p1)
