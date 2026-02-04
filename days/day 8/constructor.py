#_init_function  = all classes have  a function called_init_function(), which executes when the object is being initiated
'''
class Student:
    name = "eva wheeler"
    def __init__(self):  #self parameter is a reference to the current instance of the class
        print(self)   #self is used to access variables that belongs to the class
        print("adding new students in database")

s1 = Student()
'''

class Student:


    def __init__(self, fullname):
        self.name = fullname
        print("adding new students in database")

s1 = Student("jamie")
print(s1.name)

s2 = Student("holly")
print(s2.name)