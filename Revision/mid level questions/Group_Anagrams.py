words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = {}

for word in words:
    key = "".join(sorted(word))
    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(word)

print(list(anagrams.values()))