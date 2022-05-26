def setZeroes(matrix):
    row_length = len(matrix)
    col_length = len(matrix[0])

    visited = set()

    def dfs(row, col, direction):
        if (row not in range(row_length) or
            col not in range(col_length) or
            (row, col) in visited or
            matrix[row][col] == 0):
            return
        
        visited.add((row, col))
        matrix[row][col] = 0

        if direction == "up":
            dfs(row - 1, col, "up")
        elif direction == "down":
            dfs(row + 1, col, "down")
        elif direction == "left":
            dfs(row, col - 1, "left")
        else:
            dfs(row, col + 1, "right")

    for i in range(row_length):
        for j in range(col_length):
            if matrix[i][j] == 0 and (i, j) not in visited:
                dfs(i - 1, j, "up")
                dfs(i + 1, j, "down")
                dfs(i, j - 1, "left")
                dfs(i, j + 1, "right")


    return matrix

"""
Input: matrix = [[1,1,1],
                 [1,0,1],
                 [1,1,1]]

Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]

Approach:

DFS. For each 0, dfs and set entire row/col to 0. Add nodes to set to prevent wipeout

Time    : O(n * m)
Space   : O(n * m)
"""

def setZeroes2(matrix):
    row_length, col_length = len(matrix), len(matrix[0])
    first_cell = False

    for r in range(row_length):
        for c in range(col_length):
            if matrix[r][c] == 0:
                matrix[0][c] = 0

                if r > 0:
                    matrix[r][0] = 0
                else:
                    first_cell = True

    for r in range(1, row_length):
        for c in range(1, col_length):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(row_length):
            matrix[r][0] = 0

    if first_cell:
        for c in range(col_length):
            matrix[0][c] = 0
                 
    return matrix

"""
Approach:

Iterate matrix. If 0, set first row or column to 0. After full iteration,
loop again. If that row or column is 0, also set that cell to 0

Time    : O(n)
Space   : O(1)
"""

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]

print(setZeroes2(matrix))