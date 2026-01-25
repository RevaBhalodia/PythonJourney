#question 1
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total

number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))

#question 2
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

my_list = [1, 2, 2, 3, 4, 4, 5]
print("List without duplicates:", remove_duplicates(my_list))
