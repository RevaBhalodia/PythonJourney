'''
Build a basic payment system framework.
Requirements:
Create an abstract class Payment
Declare an abstract method pay()
Create a class UPIPayment that implements pay()
Goal:
Demonstrate abstraction by hiding implementation details
'''
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPIPayment(Payment):
    def pay(self):
        print("Payment done using UPI")

p = UPIPayment()
p.pay()
