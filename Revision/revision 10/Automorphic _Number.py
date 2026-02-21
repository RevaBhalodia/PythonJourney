def is_automorphic(n):
    square = n * n
    
    # Convert to string and check ending
    if str(square).endswith(str(n)):
        return True
    else:
        return False


# Example
num = int(input("Enter a number: "))
if is_automorphic(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")