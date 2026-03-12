students = {
    "Rahul": 85,
    "Neha": 72,
    "Amit": 91,
    "Priya": 66
}

total = 0

for marks in students.values():
    total += marks

average = total / len(students)

print("Average Marks:", average)

print("\nStudent Grades:")

for name, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print(name, ":", marks, "Grade:", grade)