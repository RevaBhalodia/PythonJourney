# 1
def find_mode(lst):
    max_count = 0
    mode = lst[0]

    for num in lst:
        count = lst.count(num)
        if count > max_count:
            max_count = count
            mode = num

    return mode

print(find_mode([1, 2, 2, 3, 4, 2, 5]))

# 2
def count_cases(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    return upper, lower

u, l = count_cases("Hello World")
print("Uppercase:", u)
print("Lowercase:", l)


# 3
def is_tech_number(num):
    s = str(num)
    length = len(s)

    if length % 2 != 0:
        return False

    mid = length // 2
    first = int(s[:mid])
    second = int(s[mid:])

    return (first + second) ** 2 == num

print(is_tech_number(2025))


# 4
def longest_common_prefix(s1, s2):
    prefix = ""
    min_len = min(len(s1), len(s2))

    for i in range(min_len):
        if s1[i] == s2[i]:
            prefix += s1[i]
        else:
            break

    return prefix


print(longest_common_prefix("flower", "flow"))

