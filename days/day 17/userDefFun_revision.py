#Write a function greet(name) that prints:Hello <name>,
# Call the function by taking name as input from the user.
name = input("enter your name:")
def greetings (name):
    print("hello",name)
    return name
greetings(name)



#Write a function add(a, b) that returns the sum of two numbers.
#take input from the user and print the returned value.
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))

def add(a, b):
    return(a + b)

result = add(a,b)
print("sum is:", result)