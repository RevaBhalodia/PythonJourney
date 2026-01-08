#static methods = methods that dont use self parameter(theyb work at class level)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hoii", self.name, "your avg score is:", sum/3)

s1 = Student("eva sharma", [99,89,97])
s1.get_avg()
s1.hello()