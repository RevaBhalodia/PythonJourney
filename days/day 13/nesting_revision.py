#Take a number as input:If the number is positive,Check if it is even or odd,Else print "Number is negative".
num = int(input("enter any number:"))
if num >= 0:
    if num % 2 == 0:
        print(" the number is postive and even")
    else:
        print(" the number is positive and odd")
else:
    print(" the number is negative")


#If marks ≥ 40,If marks ≥ 75 → print "Distinction",Else → print "Pass",Else → print "Fail".
marks = int(input("enter your marks:"))
if marks >= 40:
    if marks >= 75:
        print("distinction")
    else:
        print("pass")
else:
    print("fail")