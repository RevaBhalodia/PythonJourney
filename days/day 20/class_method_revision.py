#Create a class Student with:class variable school_name,class method to change school name.
#Create a class method that prints the total number of objects created.
class Student:
    school_name = "ABC School"   
    count = 0                   

    def __init__(self, name):
        self.name = name
        Student.count += 1       

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @classmethod
    def total_students(cls):
        print("Total students:", cls.count)

s1 = Student("Rico")
s2 = Student("Mike")
s3 = Student("Max")
Student.change_school("St.Xaviers High School")
print("School Name:", Student.school_name)
Student.total_students()
