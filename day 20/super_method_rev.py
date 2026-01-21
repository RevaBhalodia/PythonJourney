#Create a parent class Person with constructor name.
#Create a child class Student that uses super() to initialize name.
class Person:
  def __init__(self,name):
    self.name = name
    
  def show(self):
    print("Name:", self.name)

class Student(Person):
  def __init__(self, name,roll):
    super().__init__(name)
    self.roll = roll

  def display(self):
    self.show()
    print("Roll No:", self.roll)

s1 = Student("rico", 107)
s1.display()


#Create a parent class with a method show().
#Call this method from a child class using super().

class Parent:
    def show(self):
        print("This is the show method of Parent class")

class Child(Parent):
    def show(self):
        super().show()   
        print("This is the show method of Child class")

c1 = Child()
c1.show()

