#Take 5 numbers from the user and store them in a list.
#Create a new list that contains only even numbers from the original list.
numbers = []
even_numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

print("Original list:", numbers)
print("Even numbers list:", even_numbers)


#Given a list:nums = [10, 20, 30, 40, 50],Insert 25 at index 2,Remove the last element,Reverse the list.
nums = [10, 20, 30, 40, 50]

nums.insert(2, 25)
nums.pop()
nums.reverse()
print(nums)
