text = input("Enter a sentence: ")

count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)