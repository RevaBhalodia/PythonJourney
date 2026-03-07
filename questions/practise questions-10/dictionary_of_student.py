students = {"Amit":35, "Riya":78, "Raj":40}

result = {}

for name, marks in students.items():
    if marks >= 40:
        result[name] = "Pass"
    else:
        result[name] = "Fail"

print(result)