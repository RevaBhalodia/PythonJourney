# question 1
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def to_minutes(self):
        return self.hours * 60 + self.minutes
t = Time(2, 30)
print(t.to_minutes())   

# question 2
class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def is_recommended(self):
        return self.rating >= 7
m = Movie("kissing booth", 9.5)
print(m.is_recommended())  

# question 3
class Vehicle:
    def fuel_type(self):
        print("Fuel type not specified")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol or Diesel")

class Bike(Vehicle):
    def fuel_type(self):
        print("Petrol")
c = Car()
b = Bike()

c.fuel_type()
b.fuel_type()

