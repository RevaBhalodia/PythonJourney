#Create a class Student with:attributes: name, marks,method to check if the student has passed or failed.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 40:
            print(self.name, "has Passed")
        else:
            print(self.name, "has Failed")

s1 = Student("mike", 55)
s2 = Student("lucus", 32)

s1.check_result()
s2.check_result()



#Create a parent class Employee and a child class Manager.
#Use:constructor,super(),method overridingto display employee details.
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def display_details(self):
        super().display_details()
        print("Department:", self.department)
m1 = Manager("nico", 101, "IT")
m1.display_details()
