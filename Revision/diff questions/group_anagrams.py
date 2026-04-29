from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())

# Example
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [['eat','tea','ate'], ['tan','nat'], ['bat']]