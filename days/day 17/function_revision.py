#Write a function is_even(num) that:Returns True if number is even,Returns False if number is odd.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
num = int(input("enter any number: "))
print(is_even(num))


#Write a function that takes a number and returns:"Positive" if > 0,"Negative" if < 0,"Zero" if = 0.
def number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"
    
num = int(input("enter any number: "))
print(number(num))