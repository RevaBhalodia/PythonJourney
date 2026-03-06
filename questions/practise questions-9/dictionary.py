items = {"pen":10, "book":50, "bag":100}

total = sum(items.values())
avg = total / len(items)

new_dict = {}

for key, value in items.items():
    if value > avg:
        new_dict[key] = value

print("Average Price:", avg)
print("Items greater than average:", new_dict)