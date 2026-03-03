def is_fascinating(n):
    # Create concatenated string
    combined = str(n) + str(n * 2) + str(n * 3)

    # Check conditions
    if len(combined) != 9:
        return False

    if '0' in combined:
        return False

    if set(combined) == set('123456789'):
        return True

    return False


num = int(input("Enter a number: "))

if is_fascinating(num):
    print("It is a Fascinating Number")
else:
    print("It is NOT a Fascinating Number")