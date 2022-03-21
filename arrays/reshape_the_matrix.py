"""
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Approach:

1.  Base case, see if r*c is equal to the given dimensions. If not, return
2.  Create a new matrix with r rows and c columns
3.  For each row in mat, append to new matrix

Time    : O(n * m)
Space   : O(n * m)
"""

def matrixReshape(mat, r, c):
    mat_row_length = len(mat)
    mat_col_length = len(mat[0])
    r_count = 0
    c_count = 0

    #   1.
    if (r * c) != (mat_row_length * mat_col_length):
        return mat

    #   2.
    result = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(mat_row_length):
        for j in range(mat_col_length):
            result[r_count][c_count] = mat[i][j]
            c_count += 1

            if(c_count == c):
                c_count = 0
                r_count += 1

    return result

mat = [[1,2]]
r = 1
c = 1

print(matrixReshape(mat, r, c))