#Use with statement to write:Python File Handling,into a file.
with open("info.txt", "w") as f:
    f.write("python file handling\n")
    f.write("life sucks\n")

#Use with statement to read the file and print its contents.
with open("info.txt", "r") as f:
    data = f.read()
    print(data)