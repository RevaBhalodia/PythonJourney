def longest_palindrome(s):
    res = ""

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i+1)

        res = max(res, odd, even, key=len)

    return res

# Example
print(longest_palindrome("babad"))  # Output: "bab" or "aba"