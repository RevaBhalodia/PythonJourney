#print the elements using loop
num = [1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)


# search number x
num = [1,4,9,16,25,36,49,64,81,100]
for i in num:
    if(i == 25):
        print("found")
        break
    else:
        print("finding")
print("the end")

# sum of first n number
n = 5

sum = 0
for i in range(1,n+1):
    sum += i

print("total sum=", sum)


#factorial of first n numbers
n = 5
fact = 1

for i in range(1,n+1):
    fact *= 1

print("factorial =", fact)