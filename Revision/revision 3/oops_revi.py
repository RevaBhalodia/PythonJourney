# oops revision 
# 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
s1 = Student("mike", 75)
print(s1.name, "-", s1.check_result())

s2 = Student("max", 32)
print(s2.name, "-", s2.check_result())


#2
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
r = Rectangle(5, 3)

print("Area:", r.area())
print("Perimeter:", r.perimeter())
