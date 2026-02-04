class Student:
    college_name = "ycce"
    name = "anonymous"  #class attr

    def __init__(self, fullname,marks):
        self.name = fullname #obj attr > class attr
        self.marks = marks
        print("adding new students in database")

s1 = Student("jamie",100)
print(s1.name)
