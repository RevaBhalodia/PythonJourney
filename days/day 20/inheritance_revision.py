#Create a base class Animal with method sound().
# Create a child class Dog that inherits from Animal and prints "Bark".
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()


#Create a class Vehicle with attribute speed.
#Create a child class Car that inherits Vehicle and prints the speed

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def show_speed(self):
        print("Speed:", self.speed)

c = Car(120)
c.show_speed()
