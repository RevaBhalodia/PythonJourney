'''
Create a program that simulates sounds of different animals.
Requirements:
Create classes Dog and Cat
Both must have a method sound()
Each class should print a different sound
Goal:
Show polymorphism using the same method name with different behavior.
'''
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
