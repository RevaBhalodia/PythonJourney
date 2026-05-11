def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = 1

        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][-1]
# Example
print(longest_palindrome_subseq("bbbab"))
# Output: 4 (The longest palindromic subsequence is "bbbb")