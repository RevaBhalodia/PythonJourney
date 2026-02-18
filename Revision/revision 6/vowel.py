string = input("Enter a string: ")

vowels = "aeiouAEIOU"
new_string = ""

for ch in string:
    if ch in vowels:
        new_string += "*"
    else:
        new_string += ch

print("Modified string:", new_string)
