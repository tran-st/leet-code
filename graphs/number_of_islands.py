from collections import deque


def numIslands(grid):
    if grid is None:
        return grid

    row_length, col_length = len(grid), len(grid[0])
    number_of_islands = 0

    # 1.
    for row in range(row_length):
        for col in range(col_length):
            if grid[row][col] == "1": # 2.
                bfs(grid, row, col, row_length, col_length)

                number_of_islands += 1
                
    return number_of_islands

def bfs(grid, row, col, row_length, col_length):
    island_queue = deque()
    island_queue.append((row,col))

    # 3.
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    grid[row][col] = "0"

    while island_queue:
        current_row, current_col = island_queue.popleft()

        # 4.
        for x, y in directions:
            new_row = current_row + x
            new_col = current_col + y

            if new_row in range(row_length) and new_col in range(col_length) and grid[new_row][new_col] == "1":
                island_queue.append((new_row, new_col))

                grid[new_row][new_col] = "0" # 5.

"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Approach:

1. Traverse to all nodes
2. If they equal 1, add the node into a queue
3. Initialize directions
4. BFS to all directions
5. Mark each visited node as 0

Time  : O(n * m)
Space : O(n * m)
"""

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]



def numIslands2(grid):
    row_length = len(grid)
    col_length = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    island_count = 0

    def dfs(row, col):
        # Base cases
        if (row not in range(row_length) or
            col not in range(col_length) or
            grid[row][col] == "0"):
            return 0

        # Mark as visited
        grid[row][col] = "0"

        # Check all directions
        for x, y in directions:
            dfs(row + x, col + y)

        return 1

    for i in range(row_length):
        for j in range(col_length):
            if grid[i][j] == "1":
                island_count += dfs(i, j)

    return island_count
"""
Approach:

DFS. For each 1, search all connecting 1s. Increment after dfs completes

Time    : O(n * m)
Space   : O(1)
"""

print(numIslands2(grid))