def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        # Sort the word to use as key
        key = ''.join(sorted(word))

        if key not in anagram_dict:
            anagram_dict[key] = []

        anagram_dict[key].append(word)

    return list(anagram_dict.values())


words = input("Enter words separated by space: ").split()
result = group_anagrams(words)

print("Grouped Anagrams:")
print(result)