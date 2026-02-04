#Create a class MathUtils with a static method add(a, b).
class MathUtils:
    def add(a,b):
        return a + b
print("addition:", MathUtils.add(1,9))

#Create a static method to check whether a number is prime.
class NumberUtils:

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

num = 17

if NumberUtils.is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")