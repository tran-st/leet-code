def exist(board, word):
    row_length, col_length = len(board), len(board[0])

    visited = set()

    def dfs(row, col, i):
        if i == len(word):
            return True

        if (row not in range(row_length) or
            col not in range(col_length) or
            (row, col) in visited or
            board[row][col] != word[i]):
            return False

        visited.add((row, col))

        result = (dfs(row - 1, col, i + 1) or
                  dfs(row + 1, col, i + 1) or
                  dfs(row, col - 1, i + 1) or
                  dfs(row, col + 1, i + 1))

        visited.remove((row, col))

        return result

    for i in range(row_length):
        for j in range(col_length):
             if dfs(i, j, 0):
                 return True

    return False

"""
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
Output: true

Approach:

DFS. If matrix equals first char, DFS and use set to track each visited
"""

board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
word = "AAAAAAAAAAAAABB"

print(exist(board, word))