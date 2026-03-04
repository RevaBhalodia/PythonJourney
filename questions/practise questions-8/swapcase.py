string = input("Enter a string: ")
result = ""

for ch in string:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print("Output:", result)