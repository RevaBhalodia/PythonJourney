def permute(nums):
    res = []

    def backtrack(path, remaining):
        if not remaining:
            res.append(path[:])
            return

        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

    backtrack([], nums)
    return res

# Example
print(permute([1,2,3])) 
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]