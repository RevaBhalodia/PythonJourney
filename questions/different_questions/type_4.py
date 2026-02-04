# 1
def top_scorers(students):
    result = {}

    for name, marks in students.items():
        if marks >= 75:
            result[name] = marks

    return result
students = {
    "Nancy": 82,
    "Nico": 68,
    "Rico": 91,
    "Mike": 74
}

print(top_scorers(students))


# 2
def lists_to_dict(keys, values):
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result
keys = ["a", "b", "c"]
values = [1, 2, 3]

print(lists_to_dict(keys, values))


# 3
