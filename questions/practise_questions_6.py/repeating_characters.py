def longest_unique_length(s):
    start = 0
    max_length = 0
    seen = {}

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1

        seen[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

string = input("Enter a string: ")
result = longest_unique_length(string)
print("Length of longest substring without repeating characters:", result)