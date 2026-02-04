#Create a class Account with a private attribute __balance.Create a method to display the balance.
class Account:
    def __init__(self, balance):
        self.__balance = balance   

    def display_balance(self):
        print("Balance:", self.__balance)

acc = Account(5000)
acc.display_balance()


#Try accessing __balance directly outside the class.
#Write what error you get and why (in comments)
#print(acc.__balance)  