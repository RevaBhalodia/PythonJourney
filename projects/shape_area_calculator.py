class Shape:
    def area(self):
        print("Area not defined")


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Rectangle Area:", self.l * self.b)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle Area:", 3.14 * self.r * self.r)


r = Rectangle(4, 5)
c = Circle(3)

r.area()
c.area()