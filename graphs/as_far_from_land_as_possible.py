def maxDistance(grid):
    row_length = len(grid)
    col_length = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    result = 0

    def dfs(i, j, result):
        if grid[i][j] == 0: # Base case
            return True

        grid[i][j] = 1
        distance = 0
        is_zeroes = True

        for x, y in directions:
            new_i = i + x
            new_j = j + y

            if new_i in range(row_length) and new_j in range(col_length) and grid[new_i][new_j] == 0:
                is_zeroes = dfs(new_i, new_j, result) and is_zeroes
                
        distance += 1
        result = max(result, distance)

        return is_zeroes

    for i in range(row_length):
        for j in range(col_length):
            if grid[i][j] == 1 and dfs(i, j, result):
                  result += 1

    return result
"""
Input: grid = [[1,0,1],
               [0,0,0],
               [1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Time    : O(n * m)
Space   : O(1)
"""

grid = [[1,0,1],
        [0,0,0],
        [1,0,1]]

print(maxDistance(grid))