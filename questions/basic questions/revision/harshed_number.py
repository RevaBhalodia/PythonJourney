# harshed umber is a number which is divisible by the sum of its digits .
def is_harshad(n):
    digit_sum = sum(int(digit) for digit in str(n))
    if n % digit_sum == 0:
        return True
    else:
        return False

num = 18
if is_harshad(num):
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")
