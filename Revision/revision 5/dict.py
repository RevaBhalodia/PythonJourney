# 1
phone_book = {
    "Alex": "9876543210",
    "luke": "8123456789",
    "manny": "9123456780",
    "lily": "7894561230"
}

for name, number in phone_book.items():
    if number.startswith("9"):
        print(name, number)


# 2
numbers = [2, 3, 4, 2, 3, 5]

square_dict = {}

for num in numbers:
    square_dict[num] = num * num

print(square_dict)


# 3
def values_unique(d):
    values = list(d.values())
    return len(values) == len(set(values))
print(values_unique({"a": 1, "b": 2, "c": 3}))  
print(values_unique({"a": 1, "b": 2, "c": 1}))  


# 4
words = ["apple", "ant", "bat", "ball"]

grouped = {}

for word in words:
    key = word[0]
    grouped.setdefault(key, []).append(word)

print(grouped)
{'a': ['apple', 'ant'], 'b': ['bat', 'ball']}
