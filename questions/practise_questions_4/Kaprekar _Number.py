def is_kaprekar(n):
    if n == 1:
        return True

    square = n * n
    square_str = str(square)

    for i in range(1, len(square_str)):
        left = int(square_str[:i])
        right = int(square_str[i:])

        if right != 0 and left + right == n:
            return True

    return False


print(is_kaprekar(45))