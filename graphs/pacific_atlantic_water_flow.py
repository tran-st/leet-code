def pacificAtlantic(heights):
    row_length = len(heights)
    col_length = len(heights[0])

    pacific = set()
    atlantic = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    result = []

    def dfs(row, col, set, prev_height):
        if (row not in range(row_length) or 
            col not in range(col_length) or 
            (row, col) in set or
            heights[row][col] < prev_height):
            return

        set.add((row, col))

        for x, y in directions:
            new_row = row + x
            new_col = col + y

            dfs(new_row, new_col, set, heights[row][col])

    for i in range(row_length):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, col_length - 1, atlantic, heights[i][col_length - 1])

    for i in range(col_length):
        dfs(0, i, pacific, heights[0][i])
        dfs(row_length - 1, i, atlantic, heights[row_length - 1][i])

    for x, y in pacific:
        if (x, y) in atlantic:
            result.append((x, y))

    
    return result

"""
Input: heights = [[1,2,2,3,5],
                  [3,2,3,4,4],
                  [2,4,5,3,1],
                  [6,7,1,4,5],
                  [5,1,1,2,4]]
                  
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Approach:

Traverse perimeters to see which cells can reach pacific and atlantic seperately.
Then check for overlap.

Time    : O(n * m)
Space   : O(n * m)
"""

heights = [[1,2,2,3,5],
                  [3,2,3,4,4],
                  [2,4,5,3,1],
                  [6,7,1,4,5],
                  [5,1,1,2,4]]

# print(pacificAtlantic(heights))

def pacificAtlantic2(heights):
    row_length = len(heights)
    col_length = len(heights[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    pacific =  set()
    atlantic = set()

    result = []

    def dfs(row, col, set, prevHeight):
        # Check ranges of dimensions
        if (row not in range(row_length) or 
            col not in range(col_length) or
            heights[row][col] < prevHeight or
            (row, col) in set):
            return

        set.add((row, col))

        for x, y in directions:
            dfs(row + x, col + y, set, heights[row][col])

    for i in range(row_length):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, col_length - 1, atlantic, heights[i][col_length - 1])

    for j in range(col_length):
        dfs(0, j, pacific, heights[0][j])
        dfs(row_length - 1, j, atlantic, heights[row_length - 1][j])

    for x, y in pacific:
        if (x, y) in atlantic:
            result.append((x, y))

    return result

"""
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Approach:

Calculate first column, first row. See if it reach Pacific. Calculate last column, last row.
See if it reach Atlantic. Store both in set. Return overlap

Time    : O(n * m)
Space   : O(n * m)
"""

print(pacificAtlantic2(heights))