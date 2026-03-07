def product_of_odds(lst):
    product = 1

    for i in lst:
        if i % 2 != 0:
            product = product * i

    return product


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Product of odd numbers:", product_of_odds(numbers))