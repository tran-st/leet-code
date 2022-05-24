def rotate(matrix):
    row_length, col_length = len(matrix), len(matrix[0])

    left = 0
    right = col_length - 1
    top = 0
    bottom = row_length - 1
    
    while left <= right:
        for i in range(col_length - 1):
            temp1 = matrix[top][right - i]
            temp2 = matrix[bottom - i][right]

            matrix[top][right - i] = matrix[top][left + i]
            matrix[bottom - i][right] = temp1

            temp1 = temp2
            temp2 = matrix[bottom][left + i]

            matrix[bottom][left + i] = temp1
            matrix[top + i][left] = temp2

        left += 1
        right -= 1
        top += 1
        bottom -= 1
    

    return matrix


def rotate2(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        top = left
        bottom = right

        for i in range(right - left):
            top_left = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left

        left += 1
        right -= 1

    return matrix

"""
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]

Output: [[7,4,1],
         [8,5,2],
         [9,6,3]]

Approach:

         l   r
      t [1,2,3],
        [4,5,6],
      b [7,8,9]

        [1,2,1],
        [4,5,6],
        [9,8,3]

left = 0
right = col_length
top = 0
bottom = row_length

temp1 = 9
temp2 = 7
"""

matrix = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]

print(rotate2(matrix))