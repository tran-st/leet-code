def countSubIslands(grid1, grid2):
    row_length = len(grid1)
    col_length = len(grid1[0])
    sub_islands = 0

    def dfs(row, col):
        if row not in range(row_length) or col not in range(col_length) or grid2[row][col] == 0:
            return True # Still could be counted as a sub island

        result = True
        grid2[row][col] = 0

        if grid1[row][col] == 0: # Only here does it get disqualified as a sub island
            result = False

        result = dfs(row - 1, col) and result
        result = dfs(row + 1, col) and result
        result = dfs(row, col - 1) and result
        result = dfs(row, col + 1) and result

        return result

    for i in range(row_length):
        for j in range(col_length):
            if grid2[i][j] == 1 and dfs(i, j):
                sub_islands += 1

    return sub_islands

"""
Input: grid1 = [[1,1,1,0,0],
                [0,1,1,1,1],
                [0,0,0,0,0],
                [1,0,0,0,0],
                [1,1,0,1,1]], 
                
        grid2 = [[1,1,1,0,0],
                 [0,0,1,1,1],
                 [0,1,0,0,0],
                 [1,0,1,1,0],
                 [0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Time    : O(n * m)
Space   : O(1)
"""

grid1 = [[1,1,1,0,0],
         [0,1,1,1,1],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [1,1,0,1,1]]

grid2 = [[1,1,1,0,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,0]]

print(countSubIslands(grid1, grid2))