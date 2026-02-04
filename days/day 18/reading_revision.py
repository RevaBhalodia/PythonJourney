#Read the entire contents of info.txt and print it.
f = open("info.txt", "r")
data = f.read()
print(data)
f.close

#Read the file line by line and print each line separately
f = open("info.txt", "r")

for line in f:
    print(line)
f.close