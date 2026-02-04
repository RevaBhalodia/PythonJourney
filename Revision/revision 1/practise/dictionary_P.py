# dictionary
# question 1
students = {
    "finn": [80, 75, 90],
    "mike": [60, 70, 65],
    "will": [85, 88, 92]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(name, "average marks:", average)


# question 2
data = {"a": 10, "b": 20, "c": 30}

squared_data = {}

for key, value in data.items():
    squared_data[key] = value * value

print(squared_data)


# question 3
employees = {
    "nancy": 45000,
    "mike": 60000,
    "erica": 30000,
    "steve": 52000
}

for name, salary in employees.items():
    if salary < 50000:
        employees[name] = salary + (salary * 0.10)

print(employees)
