#1
numbers = [1, 2, 3, 4]

cube_dict = {}

for num in numbers:
    cube_dict[num] = num ** 3

print(cube_dict)


#2
items = {'apple': 5, 'banana': 3, 'orange': 4}

for key in items:
    items[key] = items[key] + 1

print(items)


#3
names = ["Alice", "Aman", "Bob", "Bina", "Charlie"]

name_dict = {}

for name in names:
    first_letter = name[0]
    if first_letter in name_dict:
        name_dict[first_letter].append(name)
    else:
        name_dict[first_letter] = [name]

print(name_dict)
