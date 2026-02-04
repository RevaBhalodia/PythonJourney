#question 1
numbers = [2, -5, 0, 7, -1, 0, 3]

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeroes:", zero)



#question 2
numbers = [5, 2, 9, 1, 7]

numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)
