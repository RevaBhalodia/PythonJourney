# with syntax 
# with open("demo.txt","a")
# data = f.read()
with open(r"day 7\demo.txt", "r") as f:
    data = f.read()
    print(data)


with open(r"day 7\demo.txt", "w") as f:
    data = f.write("new data")
    print(data)