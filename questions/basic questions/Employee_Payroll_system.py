'''
Calculate salary details.
Base class Employee,Child class Manager,Use super(),Attributes: basic salary, bonus,
Methods:
calculate salary,display details,Use class method to count employees,Save payroll report to file.
'''

class Employee:
    employee_count = 0  

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary
        Employee.employee_count += 1

    def calculate_salary(self):
        return self.basic_salary

    def display_details(self):
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

class Manager(Employee):
    def __init__(self, name, basic_salary, bonus):
        super().__init__(name, basic_salary)   
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus

    def display_details(self):
        super().display_details()
        print("Bonus:", self.bonus)
        print("Total Salary:", self.calculate_salary())

m1 = Manager("Amit", 50000, 10000)
m2 = Manager("Neha", 60000, 15000)

m1.display_details()
print()
m2.display_details()

print("\nTotal Employees:", Employee.get_employee_count())

with open("payroll_report.txt", "w") as file:
    file.write("Payroll Report\n")
    file.write("-----------------\n")

    file.write(f"Name: {m1.name}, Salary: {m1.calculate_salary()}\n")
    file.write(f"Name: {m2.name}, Salary: {m2.calculate_salary()}\n")

    file.write("\nTotal Employees: " + str(Employee.get_employee_count()))

print("\nPayroll report saved to payroll_report.txt")
