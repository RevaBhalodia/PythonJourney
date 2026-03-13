text = input("Enter text: ")

clean = text.replace(" ", "").lower()

reverse = clean[::-1]

if clean == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")