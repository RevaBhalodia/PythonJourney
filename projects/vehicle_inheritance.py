class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def show(self):
        print("Vehicle:", self.name)
        print("Speed:", self.speed)


class Car(Vehicle):
    def fuel_type(self):
        print("Fuel: Petrol")


class Bike(Vehicle):
    def helmet_required(self):
        print("Helmet Required: Yes")


c = Car("Swift", 120)
b = Bike("Pulsar", 100)

c.show()
c.fuel_type()

print()

b.show()
b.helmet_required()