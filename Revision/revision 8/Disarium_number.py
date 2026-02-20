#Sum of its digits raised to their respective positions = the number itself.
num = int(input("Enter a number: "))

temp = num
digits = str(num)
sum_value = 0

for i in range(len(digits)):
    digit = int(digits[i])
    sum_value += digit ** (i + 1)

if sum_value == num:
    print(num, "is a Disarium number")
else:
    print(num, "is NOT a Disarium number")
