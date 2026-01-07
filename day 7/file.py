# file I/O . python can be  used to perform operations in file 
# types of files : text file and binary files
# open,read and close file
# we have to open a file before reading or writing
# syntax: f = open("file_name","mode")
#mode: read mode and write mode



with open(r"day 7\demo.txt", "r") as f:
    data = f.read()
    print(data)
    print(type(data))
f.close()