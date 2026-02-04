#private attributes & methods 
#private attributes and methods are meant to be used only within the class and are not accessible from outside the class

class Account:
    def __init__(self, acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
    

acc1 = Account("191919", "rici19")

print(acc1.acc_no)
print(acc1.reset_pass())



#method

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello people!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())