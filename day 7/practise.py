with open("practise.txt","w") as f:
    f.write("hii everyone\nwe are learning file I/O \n")
    f.write("using java\nI like progamming in java")




# waf that replaces all occuremces of"Java" with "python" in above file
with open("practise.txt","r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practise.txt","w") as f:
    data = f.write(new_data)

#search if "learning" word exist in the file
word = "learning"
with open("practise.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")


#waf to find in which line of the file does the word "learning" occurs first .print -1 if word found
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practise.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()

# from a file containing numbers seperated by commas, print the count of even numbers.
with open("practise.txt","r") as f:
    data = f.read()
    print(data)
