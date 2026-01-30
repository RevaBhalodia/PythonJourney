# question 1
def passed_students(students):
    passed = {}

    for name in students:
        if students[name] >= 40:
            passed[name] = students[name]

    return passed
students = {"joey": 35, "monica": 78, "chandler": 40}
print(passed_students(students))


# question 2
def invert_dict(d):
    inverted = {}

    for key in d:
        value = d[key]
        inverted[value] = key

    return inverted
print(invert_dict({"a": 1, "b": 2}))
