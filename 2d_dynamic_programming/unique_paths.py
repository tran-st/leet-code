def uniquePaths(m, n):
    rows = m
    cols = n
    dp = [[0] * cols for _ in range(rows)]

    # Fill initial cells
    for i in range(rows):
        dp[i][0] = 1

    for j in range(cols):
        dp[0][j] = 1

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[rows - 1][cols - 1]

"""
Input: m = 3, n = 7
Output: 28

Approach:

    0   1   1   1   1   1   1
    1   2   3   4   5   6   7
    1   3   6   10  15  21  T

DP. First column and rows have only one possible path. From there, fill out the grid

Time    : O(n * m)
Space   : O(n * m)
"""

m = 3
n = 7

print(uniquePaths(m, n))