# 1
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0
for n in numbers:
    total += n

avg = total / len(numbers)

greater_than_avg = []
for n in numbers:
    if n > avg:
        greater_than_avg.append(n)

print("Original list:", numbers)
print("Average:", avg)
print("Numbers greater than average:", greater_than_avg)


# 2
items = {
    "Pen": 10,
    "Notebook": 120,
    "Bag": 500,
    "Bottle": 90
}

for item, price in items.items():
    if price > 100:
        print(item, ":", price)


# 3
words = ["apple", "book", "education", "sky"]

vowel_dict = {}

for word in words:
    count = 0
    for ch in word:
        if ch in "aeiouAEIOU":
            count += 1
    vowel_dict[word] = count

print(vowel_dict)
