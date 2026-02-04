# 1
class Logger:
    count = 0   

    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)
        Logger.count += 1

    def show_messages(self):
        return self.messages

    @classmethod
    def total_logs(cls):
        return cls.count



l1 = Logger()
l2 = Logger()

l1.log("System started")
l2.log("User logged in")
l1.log("Error occurred")

print(Logger.total_logs())   


# 2
class Order:
    def __init__(self, item_name, quantity, price_per_item):
        self.item_name = item_name
        self.quantity = quantity
        self.price_per_item = price_per_item

    def total_price(self):
        total = self.quantity * self.price_per_item
        tax = total * 0.05
        return total + tax


order = Order("Notebook", 5, 50)
print(order.total_price())


# 3
class Student:
    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def total_students(cls):
        return cls.count
#A class method is better when the operation:depends on class-level data, not on individual objects should behave the same for all objects