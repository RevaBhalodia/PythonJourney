# 1
def even_odd_dict(numbers):
    result = {}

    for num in numbers:
        if num % 2 == 0:
            result[num] = "even"
        else:
            result[num] = "odd"

    return result
nums = [1, 2, 3, 4, 5]
print(even_odd_dict(nums))


# 2
def remove_underage(people):
    result = {}

    for name, age in people.items():
        if age >= 18:
            result[name] = age

    return result
ages = {"joe": 20, "maya": 17, "Charlie": 25}
print(remove_underage(ages))


# 3
def string_length_dict(strings):
    result = {}

    for s in strings:
        if s not in result:
            result[s] = len(s)

    return result
words = ["apple", "banana", "apple", "cherry"]
print(string_length_dict(words))
