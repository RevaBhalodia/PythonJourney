# 1
def exactly_twice(lst):
    result = []
    for num in lst:
        if lst.count(num) == 2 and num not in result:
            result.append(num)
    return result
print(exactly_twice([1, 2, 3, 2, 4, 5, 1, 6, 3]))


# 2
def increase_marks(students):
    new_dict = {}
    for name, marks in students.items():
        new_marks = marks + 5
        if new_marks > 100:
            new_marks = 100
        new_dict[name] = new_marks
    return new_dict

students = {"Asha": 95, "Ravi": 88, "Neha": 100}
print(increase_marks(students))


# 3
n = input("Enter a number: ")
sum_even = 0

for digit in n:
    d = int(digit)
    if d % 2 == 0:
        sum_even += d

print("Sum of even digits:", sum_even)


# 4
def greater_than_average(lst):
    avg = sum(lst) / len(lst)
    result = []

    for num in lst:
        if num > avg:
            result.append(num)

    return result
numbers = [10, 20, 30, 40]
print(greater_than_average(numbers))
