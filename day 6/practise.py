#average of 3 numbers
def avg_sum(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
avg_sum(9,1,2)


#leng of a list
num = [2,3,5,7,9,0,3,4,5,6,7]
names = ["chandler","joey","monica","rachel","ross","pheobe"]

def print_len(list):
    print(len(list))

def print_list(list):    #printing a list in one line
    for item in list:
        print(item,end=" ")

print_list(num)
print_list(names)

#factorial of n
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
    print(fact)

n = 6
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(6)


# usd to inr
def converter(usd_val):
    inr_val = usd_val *89
    print(usd_val,"USD =", inr_val, "INR")

converter(1)