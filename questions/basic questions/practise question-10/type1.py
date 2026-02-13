def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(num):
    s = str(num)
    for i in range(len(s)):
        rotation = int(s[i:] + s[:i])
        if not is_prime(rotation):
            return False
    return True


number = 197

if is_circular_prime(number):
    print("Circular Prime")
else:
    print("Not a Circular Prime")
