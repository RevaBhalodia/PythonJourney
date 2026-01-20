#Create an abstract class Shape with an abstract method area().
from abc import ABC, abstractmethod
class Shape(ABC):
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
r = Rectangle(11,2)

print("rectangle area:", r.area())


#Create a class Square that inherits Shape and implements area().
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
s= Square(6)

print("rectangle area:", r.area())
print("square area:", s.area())