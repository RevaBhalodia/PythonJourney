# file handling revision
# 1
name = input("Enter your name: ")
age = input("Enter your age: ")

file = open("user.txt", "w")
file.write("Name: " + name + "\n")
file.write("Age: " + age)
file.close()

file = open("user.txt", "r")
content = file.read()
file.close()

print("File content:")
print(content)


# 2
file = open("user.txt", "r")
lines = file.readlines()
file.close()

print("Number of lines:", len(lines))
