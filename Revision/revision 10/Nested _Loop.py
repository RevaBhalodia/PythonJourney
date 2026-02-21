def vowel_count_dict(sentence):
    vowels = "aeiouAEIOU"
    result = {}

    words = sentence.split()

    for word in words:
        count = 0
        for ch in word:
            if ch in vowels:
                count += 1
        result[word] = count

    return result


# Example
print(vowel_count_dict("python is powerful"))