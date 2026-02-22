def is_buzz(n):
    if n % 7 == 0 or n % 10 == 7:
        return True
    else:
        return False


# Example
num = int(input("Enter a number: "))

if is_buzz(num):
    print("Buzz Number")
else:
    print("Not a Buzz Number")