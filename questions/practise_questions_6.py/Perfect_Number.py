def is_perfect_number(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


num = int(input("Enter a number: "))

if is_perfect_number(num):
    print("It is a Perfect Number")
else:
    print("It is NOT a Perfect Number")