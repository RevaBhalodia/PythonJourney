text = input("Enter text: ")

letters = digits = spaces = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)