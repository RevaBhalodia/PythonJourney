#Take a number as input and:Print "Positive" if the number is greater than 0 ,
# Print "Negative" if the number is less than 0,Print "Zero" if the number is 0.

num = int(input("enter any number:"))
if num >= 0:
    print("positive")

elif num <= 0:
    print("negative")

else:
    print("zero")


#Take the user’s age as input:If age ≥ 18 → print "Eligible to vote",Else → print "Not eligible to vote".

age = int(input("enter your age:"))

if age >= 18:
    print("you are eligible to vote")

else:
    print("you are not eligible to vote")