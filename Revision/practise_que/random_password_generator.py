import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + "@#$%"
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Enter length: "))
print("Password:", generate_password(length))