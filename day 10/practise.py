class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
        
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(19)
print(c1.area())
print(c1.perimeter())




class Employee:
    def __init__(self, role,dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        

    def showDetails(self):
        print("role=", self.role)
        print("dept=", self.dept)
        print("salary=", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "CS", "22,00,000")

engg1 = Engineer("nico blasey",21)
engg1.showDetails()
        

#e1 = Employee("accountant", "finance", "21,00,000")
#e1.showDetails()



class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def  __gt__(self, ord2):
        return self.price > ord2.price

odr1 = Order("chips",80)
ord2 = Order("biscuit",45)

print(ord2 > ord2)
   