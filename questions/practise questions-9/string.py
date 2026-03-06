string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result = result + ch

print("Output:", result)