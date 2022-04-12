def numEnclaves(grid):
    row_length = len(grid)
    col_length = len(grid[0])
    result = 0

    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for i in range(row_length):
        for j in range(col_length):
            if i == 0 or j == 0 or i == row_length - 1 or j == col_length - 1:
                if grid[i][j] == 1:
                    dfs(grid, i, j, row_length, col_length, directions)

    for i in range(row_length):
        for j in range(col_length):
            if grid[i][j] == 1:
                result += 1

    return result

def dfs(grid, i, j, row_length, col_length, directions):
    if grid[i][j] == 0:
        return

    grid[i][j] = 0

    for x, y in directions:
        if i + x in range(row_length) and j + y in range(col_length) and grid[i + x][j + y] == 1:
            dfs(grid, i + x, j + y, row_length, col_length, directions)


"""
Input: grid = [[0,0,0,0],
               [1,0,1,0],
               [0,1,1,0],
               [0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Approach:

DFS from each land cell on perimeter. Set all visited to 0. Count all remaining 1s

Time    : O(n * m)
Space   : O(1)
"""

grid = [[0,0,0,0],
        [1,0,1,1],
        [0,1,1,0],
        [0,0,0,0]]


print(numEnclaves(grid))