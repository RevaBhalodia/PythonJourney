students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 54},
    {"name": "Carol", "grade": 73},
    {"name": "Dave",  "grade": 91},
]

# Passing students (grade >= 60)
passing = [s["name"] for s in students if s["grade"] >= 60]

# Name → grade dict
grade_map = {s["name"]: s["grade"] for s in students}

# Grades squared
squares = [s["grade"] ** 2 for s in students]

print(passing)
print(grade_map)
print(squares)