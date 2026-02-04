#Create a class Laptop with attributes:brand,price,Create an object and modify the price after creation.
class Laptop():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("macbook",100000)

l1.price = 200000

print("brand", l1.brand)
print("price", l1.price)
        


#Create a class Book and dynamically add an attribute pages to its object.
class Book:
    def __init__(self, name):
        self.name = name

b1 = Book("you only live once")
b1.pages = 350

print("book name:", b1.name)
print("pages:",b1.pages)