# methods are functions that belong to objects.
class Student:
    college_name = "ycce"

    def __init__(self, fullname,marks):
        self.name = fullname #obj attr > class attr
        self.marks = marks
        
    def welcome(self):
            print("welcome students", self.name)

    def get_marks(self):
         return self.marks


s1 = Student("jamie",100)
s1.welcome()
print(s1.get_marks())