#Create a class Person with:attribute name,method display_name(),Create an object and call the method.
class Person:
    def __init__(self,name):
        self.name = name

    def display_name(self):
        print(self.name)

p1 = Person("rico")
p1.display_name()


#Create a class Mobile with:attributes brand, price,method to check if price is greater than 20,000
class Mobile:
    def __init__(self, brand,price):
        self.brand = brand
        self.price = price

    def check_price(self):
        if self.price > 20000:
            print("price is greater than 20000")
        else:
            print("price is 20000 or less")
        
m1 = Mobile("Apple", 25000)
m1.check_price()