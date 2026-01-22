#Create a base class Shape with a method draw().
#Create a child class Circle that overrides the draw() method to print:
#Drawing Circle,Create an object of Circle and call draw() to observe polymorphism.
class Shape:
    def draw(self):
        print("Drawing Shape")


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


obj = Circle()
obj.draw()



#Create two classes:
#dog with method sound() → prints "Bark",Cat with method sound() → prints "Meow",
#Create objects of both classes and call the sound() method for each using the same method name.
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
