#Create a class Person with a constructor that takes:name,age,Print the values using an object.
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("mike wheeler",23)

print(p1.name)
print(p1.age)

#Create a class Employee with constructor parameters:
#name,salary,Create an object and display employee details.
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("employee name:", self.name)
        print("employee salary:", self.salary)

e1 = Employee("nancy",1000000)
e1.display()