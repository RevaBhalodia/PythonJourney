#Write your name and age into a file named info.txt(each on a new line).
f = open("info.txt","w")
f.write("name: rico\n")
f.write("age: 20\n")
f.close()

#Write numbers from 1 to 5 into a file, one number per line.
f = open("numbers.txt", "w")

for i in range(1,6):
    f.write(str(i) + "\n")
    f.close