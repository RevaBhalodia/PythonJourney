# 1
class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

c = Circle()
print(c.area(5))


# 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def is_highly_paid(self):
        if self.salary > 50000:
            return "Highly Paid"
        else:
            return "Not Highly Paid"

e = Employee("nico", 60000)
print(e.is_highly_paid())

