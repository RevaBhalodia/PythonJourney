# question 1
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        return hours, minutes, seconds
t = Timer(3665)
print(t.convert())


# question 2
class ShoppingItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        gst = self.price * 0.18
        return self.price + gst
item = ShoppingItem("Shoes", 2000)
print(item.final_price())


# question 3
class Shape:
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
sq = Square(5)
rect = Rectangle(4, 6)

print(sq.perimeter())
print(rect.perimeter())
