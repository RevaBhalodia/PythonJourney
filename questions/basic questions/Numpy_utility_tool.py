'''
Create a tool to perform number operations.
Functions for:
prime check,factorial (use recursion),sum of digits,
Menu-driven program,Store results in a file,Use built-in functions where possible.
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):   
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))  



while True:
    print("\n--- Number Operations Menu ---")
    print("1. Check Prime")
    print("2. Find Factorial")
    print("3. Sum of Digits")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    with open("number_operations.txt", "a") as file:

        if choice == 1:
            num = int(input("Enter a number: "))
            result = is_prime(num)
            print("Prime:", result)
            file.write(f"Prime check of {num}: {result}\n")

        elif choice == 2:
            num = int(input("Enter a number: "))
            result = factorial(num)
            print("Factorial:", result)
            file.write(f"Factorial of {num}: {result}\n")

        elif choice == 3:
            num = int(input("Enter a number: "))
            result = sum_of_digits(num)
            print("Sum of digits:", result)
            file.write(f"Sum of digits of {num}: {result}\n")

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

