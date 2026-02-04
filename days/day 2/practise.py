#name = input("enter your name:")
#print(name,len(name))



str = " hey, $ is going cray in usa, yes $"
print(str.find("$"))

num = input("enter any number:")
if(num % 2 == 0):
    print("even number")
else:
    print("odd number")



a = input("enter first num")
b = input("enter second num")
c = input("enter third num")
if(a>=b and a>=c):
    print("a is greater")
elif(b>=a and b>=c):
    print("b is greater ")
else:
    print("c is greater")



num = input("enter any number:")
if(num % 7 ==0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")