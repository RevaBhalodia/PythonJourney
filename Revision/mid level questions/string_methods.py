name = "  Hello, Python World!  "

# Clean up and transform
print(name.strip())           # remove whitespace
print(name.strip().lower())   # lowercase
print(name.strip().upper())   # uppercase
print(name.strip().replace("Python", "IT"))

# Split and join
words = name.strip().split(" ")
print(words)
print("-".join(words))

# f-string formatting
student = "Arjun"
marks = 87.456
print(f"Student: {student}, Marks: {marks:.2f}")

# Check content
email = "student@college.edu"
print(email.endswith(".edu"))   # True
print(email.startswith("admin"))  # False
print("college" in email)       # True