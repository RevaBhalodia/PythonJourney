#1
numbers = []

for i in range(6):
    num = int(input("Enter a number: "))
    numbers.append(num)

div_by_3 = []

for n in numbers:
    if n % 3 == 0:
        div_by_3.append(n)

print("Numbers divisible by 3:", div_by_3)


#2
words = ["apple", "banana", "cat", "python"]

word_length = {}

for word in words:
    word_length[word] = len(word)

print(word_length)


#3
students = {
    "Rahul": 78,
    "Amit": 35,
    "Sneha": 92,
    "Neha": 40
}

print("Passed students:")
for name, marks in students.items():
    if marks >= 40:
        print(name, ":", marks)
