# A number is Automorphic if its square ends with the same number.
def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

num = 25
if is_automorphic(num):
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number")
