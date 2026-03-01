def longest_unique_substring(s):
    start = 0
    max_length = 0
    longest = ""
    seen = {}

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1

        seen[s[end]] = end

        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest = s[start:end+1]

    return longest


string = input("Enter a string: ")
result = longest_unique_substring(string)
print("Longest substring without repeating characters:", result)