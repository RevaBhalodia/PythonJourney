def min_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0]*cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    # First row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # First column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill rest
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[-1][-1]


grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

print(min_path_sum(grid))