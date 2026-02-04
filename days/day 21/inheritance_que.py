
'''Design a simple system to represent vehicles.
Requirements:
Create a base class Vehicle with method display_type()
Create a child class Car that inherits from Vehicle
Use the inherited method without redefining it
Goal:
Demonstrate inheritance by reusing parent class functionality.
'''
class Vehicle:
    def display_type(self):
        print("This is a vehicle")


class Car(Vehicle):
    pass   

c = Car()
c.display_type()
