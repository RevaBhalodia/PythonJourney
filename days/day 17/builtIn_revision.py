#Use built-in functions to find:Length of a string,Maximum number from a list,Minimum number from a list.

list = [1,2,3,4,5,6]
print(len(list))
print(type(list))
print(max(list))
print(min(list))


#Given:numbers = [2, 4, 6, 8],Use a built-in function to check if all numbers are even.
numbers = [2, 4, 6, 8]
result = all(num % 2 == 0 for num in numbers)
print(result)