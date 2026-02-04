#question 1
employees = {
    "max": 45000,
    "mike": 60000,
    "finn": 52000,
    "will": 48000
}

for name, salary in employees.items():
    if salary > 50000:
        print(name)

#question 2
students = {
    "steve": 78,
    "lucus": 85,
    "dustin": 72,
    "johnathan": 90
}

total = 0

for marks in students.values():
    total += marks

average = total / len(students)

print("Average marks:", average)
