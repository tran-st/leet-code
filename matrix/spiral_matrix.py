def spiralOrder(matrix):
    row_length, col_length = len(matrix), len(matrix[0])
    result = []

    left = 0
    right = col_length
    top = 0
    bottom = row_length

    while left < right and top < bottom:

        for i in range(left, right): # Left to right
            result.append(matrix[top][i])

        top += 1

        for i in range(top, bottom): # Top to bottom
            result.append(matrix[i][right - 1])

        right -= 1

        if not (left < right and top < bottom): # Take care of duplicate copies
            break

        for i in range(right - 1, left - 1, -1): # Right to left
            result.append(matrix[bottom - 1][i])

        bottom -= 1

        for i in range(bottom -1, top - 1, -1): # Bottom to top
            result.append(matrix[i][left])

        left += 1
    
    return result

"""
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]

Approach:

          l    r
       [[1,2,3,4],
        [5,6,7,8],
    tb  [9,10,11,12]]
       

result = [1,2,3,4,8,12,11,10,9,5,6,7]

left = 0
right = 3
top = 1
bottom = 3

Loop left to right, increment top boundary
Loop top to bottom, increment right boundary
Loop right to left, increment bottom boundary
Loop bottom to top, increment left boundary

Time    : O(n*m)
Space   : O(1)
"""

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print(spiralOrder(matrix))