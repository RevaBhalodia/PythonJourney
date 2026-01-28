# Take a list of numbers and create: one list of even numbers one list of odd numbers.
def separate_even_odd(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd

nums = [1, 2, 3, 4, 5, 6]
even_list, odd_list = separate_even_odd(nums)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

#Rotate a list one position to the right. Example: [1, 2, 3, 4] → [4, 1, 2, 3]
def rotate_right(lst):
    last = lst[-1]
    lst = [last] + lst[:-1]
    return lst

numbers = [1, 2, 3, 4]
print(rotate_right(numbers))
