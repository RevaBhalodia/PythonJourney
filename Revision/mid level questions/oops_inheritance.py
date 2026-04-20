class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns ₹{self.salary:,}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self):
        base = super().describe()
        return f"{base} and manages {self.team_size} people"

e = Employee("Ravi", 50000)
m = Manager("Priya", 90000, 8)
print(e.describe())
print(m.describe())