# dictionary revision
# 1
marks = {
    "Maths": 85,
    "Science": 90,
    "English": 78
}

highest = max(marks, key=marks.get)

print("Subject with highest marks:", highest)


# 2
data = {"a": 10, "b": 20, "c": 30}

for key in data:
    data[key] += 5

print(data)
