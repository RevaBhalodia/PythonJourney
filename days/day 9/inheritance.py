#inheritancce = when one class(child) derives the properties & methods of another class(parents)
# types 
#1. single inheritance
'''
class car :
  @staticmethod
  def start():
    print("car started.....")

  @staticmethod
  def stop():
    print("car stopped.")

class BmwCar(car):
  def __init__(self, name):
    self.name = name

car1 = BmwCar("suden")
car2 = BmwCar("suv")

print(car1.name)
print(car1.start())
'''
# multi-level inheritance
'''
class car :
  @staticmethod
  def start():
    print("car started.....")

  @staticmethod
  def stop():
    print("car stopped.")

class BmwCar(car):
  def __init__(self, brand):
    self.brand = brand

class Suv(BmwCar):
  def __init__(self, type):
    self.type = type

car1 = Suv("bmw x series")
car1.start()
'''

#multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class c"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)