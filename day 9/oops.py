#del keyword = used to delet object properties or object itself.
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("reva")
print(s1)
del s1
print(s1)

