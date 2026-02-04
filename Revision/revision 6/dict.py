# 1
def value_frequency_dict(d):
    freq = {}
    
    for value in d.values():
        freq[value] = freq.get(value, 0) + 1

    new_dict = {}
    for key in d:
        new_dict[key] = freq[d[key]]

    return new_dict

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(value_frequency_dict(d))


# 2
def merge_dicts(d1, d2):
    result = d1.copy()

    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result

d1 = {'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}
print(merge_dicts(d1, d2))


# 3
def top_two_scorers(students):
    sorted_students = sorted(
        students.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_students[:2]

students = {'alex': 85, 'Nancy': 92, 'mike': 88, 'will': 90}
print(top_two_scorers(students))


# 4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def remove_prime_length_words(d):
    new_dict = {}

    for key, value in d.items():
        if not is_prime(len(key)):
            new_dict[key] = value

    return new_dict

words = {'hi': 1, 'hello': 2, 'python': 3, 'code': 4}
print(remove_prime_length_words(words))
