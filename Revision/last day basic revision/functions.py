# question 1
def common_elements(list1, list2):
    result = []
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))


# question 2
def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
print(count_factors(12))


# question 3
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    for char in str1:
        if str1.count(char) != str2.count(char):
            return False

    return True
print(are_anagrams("listen", "silent"))
