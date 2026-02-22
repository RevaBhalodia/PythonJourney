def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def prime_index_uppercase(s):
    result = ""

    for i in range(len(s)):
        if is_prime(i):
            result += s[i].upper()
        else:
            result += s[i]

    return result


# Example
print(prime_index_uppercase("python"))