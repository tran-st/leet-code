"""
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Approach:

Ignore islands that are on the grid's perimeter. Loop through i = 1 and j = 1.
If land is found, DFS it and see if it is a closed island. A closed island would
be land thats surrounded by land that's already visisted, or by water. Also check
if that island is on the grid perimeter

Time    : O(n * m)
Space   : O(1)
"""

def closedIsland(grid):
    row_length = len(grid)
    col_length = len(grid[0])
    result = 0

    for i in range(1, row_length): # Skip grid perimeter
        for j in range(1, col_length):
            if grid[i][j] == 0:
                if(dfs(grid, i, j, row_length, col_length)):
                    result += 1


    return result

def dfs(grid, i, j, row_length, col_length):
    if grid[i][j] == 1 or grid[i][j] == -1: # Base case
        return True

    if i == 0 or j == 0 or i == row_length - 1 or j == col_length - 1: # Check if cell is on perimeter
        return False

    grid[i][j] = -1 # Visited

    up = dfs(grid, i - 1, j, row_length, col_length)
    down = dfs(grid, i + 1, j, row_length, col_length)
    left = dfs(grid, i, j - 1, row_length, col_length)
    right = dfs(grid, i, j + 1, row_length, col_length)

    return up and down and left and right


"""
Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]])
"""

grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]

print(closedIsland(grid))