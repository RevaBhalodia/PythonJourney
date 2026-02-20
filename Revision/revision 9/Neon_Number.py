def is_neon(n):
    square = n * n
    digit_sum = 0

    while square > 0:
        digit_sum += square % 10
        square //= 10

    if digit_sum == n:
        return True
    else:
        return False


num = int(input("Enter a number: "))
if is_neon(num):
    print("Neon Number")
else:
    print("Not a Neon Number")