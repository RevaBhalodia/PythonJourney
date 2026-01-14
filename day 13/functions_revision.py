#Write a function add_numbers(a, b) that returns the sum of two numbers.Call the function and print the result

def add_numbers(a,b):
   sum = a + b 
   print(sum)
   return sum
 
add_numbers(1,9)

#Write a function square(num) that returns the square of a number.
#Take input from the user and pass it to the function.

def square_no(n):
   return n ** 2

num = int(input("enter any number:"))
print("square is:", square_no(num))
   