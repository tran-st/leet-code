from collections import deque

"""
Approach:

BFS. If current node is 1, BFS and increment area count for each valid move

1.  Row and column lengths
2.  Deque, directions
3.  Loop through rows and columns
4.  If 1, add to queue
5.  BFS
6.  Check all directions
7.  Check bounds

Time    : O(n * m)
Space   : O(n)
"""

def maxAreaOfIsland(grid):
    #   1.
    row_length = len(grid)
    col_length = len(grid[0])
    queue = deque() #   2.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_area = 0

    #   3.
    for i in range(row_length):
        for j in range(col_length):
            if grid[i][j] == 1:
                queue.append([i, j])    #   4.
                current_area = 0

                while queue:
                    current_row, current_col = queue.popleft()

                    for x, y in directions: #   6.
                        new_row = current_row + x
                        new_col = current_col + y

                        if (new_row in range(row_length) and 
                        new_col in range(col_length) and 
                        grid[new_row][new_col] == 1):   #   7.
                            queue.append([new_row, new_col])    #   4.
                            grid[new_row][new_col] = 0

                    grid[current_row][current_col] = 0
                    current_area += 1

                max_area = max(max_area, current_area)
    
    return max_area

"""
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
"""

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]

print(maxAreaOfIsland(grid))