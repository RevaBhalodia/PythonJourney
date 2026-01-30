# question 1
class Counter:
    def __init__(self):
        self.__count = 0   # private variable

    def increment(self):
        self.__count += 1

    def decrement(self):
        if self.__count > 0:
            self.__count -= 1
        else:
            print("Count cannot be negative")

    def display(self):
        print("Count:", self.__count)
c = Counter()
c.increment()
c.increment()
c.decrement()
c.display()


# question 2
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def result(self):
        avg = (self.m1 + self.m2 + self.m3) / 3

        if avg >= 75:
            return "Excellent"
        elif avg >= 60:
            return "Good"
        else:
            return "Needs Improvement"
s = Student(80, 70, 90)
print(s.result())


# question 3
class Notification:
    def send(self):
        print("Sending notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")
notifications = [EmailNotification(), SMSNotification()]

for n in notifications:
    n.send()
