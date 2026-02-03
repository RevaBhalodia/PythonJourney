# 1
class PasswordChecker:
    def check(self, password):
        if len(password) >= 8 and any(ch.isdigit() for ch in password):
            return "Strong"
        else:
            return "Weak"

p = PasswordChecker()
print(p.check("hello123"))   
print(p.check("hello"))      


# 2
class Counter:
    value = 0  

    def increase(self):
        Counter.value += 1
        return Counter.value
c1 = Counter()
c2 = Counter()

print(c1.increase())  
print(c2.increase())  
print(c1.increase()) 


# 3
#What is Polymorphism?
#Polymorphism means one function name, many forms.
#ifferent objects can respond differently to the same method call.

# 4
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5

class Circle(Shape):
    def area(self):
        return 3.14 * 7 * 7
shapes = [Rectangle(), Circle()]

for s in shapes:
    print(s.area())
