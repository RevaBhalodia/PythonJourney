def remove_consecutive_duplicates(s):
    if not s:
        return ""

    result = s[0]   

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result += s[i]

    return result


print(remove_consecutive_duplicates("aabbccdaa"))