#Create a file named demo.txt and open it in write mode.Write the text:Hello Python
with open("day 18\demo2.txt ","w") as f:
    f.write("Hello Python")



#Open the same file in read mode and print its contents.
with open(r"day 18\demo2.txt ","r") as f:
    data = f.read()
    print(data)
   