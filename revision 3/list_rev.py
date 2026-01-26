#list revision
# 1
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

greater_than_10 = []

for n in numbers:
    if n > 10:
        greater_than_10.append(n)

print("Original list:", numbers)
print("Numbers greater than 10:", greater_than_10)


#2
nums = [1, 2, 3, 4, 5]
squared_nums = []

for n in nums:
    squared_nums.append(n * n)

print("Squared list:", squared_nums)

