#Create a class Calculator with a method add() that adds two numbers.
class Calculator:
    def add(self, a,b):
        return a + b
    
c = Calculator()
print("addition:",c.add(9,1))

#Create a class Rectangle with methods to calculate:Area,Perimeter.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2* (self.length + self.breadth)
    
r = Rectangle(19,34)

print("area:",r.area())
print("perimeter:",r.perimeter())