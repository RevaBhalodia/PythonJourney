def group_by_vowel_count(words):
    vowels = "aeiou"
    result = {}

    for word in words:
        count = 0
        for char in word.lower():
            if char in vowels:
                count += 1

        if count not in result:
            result[count] = []

        result[count].append(word)

    return result


words = ["cat", "apple", "dog", "elephant"]
print(group_by_vowel_count(words))
