def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image

    row_length = len(image) - 1
    column_length = len(image[0]) - 1

    fill(image, sr, sc, newColor, image[sr][sc], row_length, column_length)

    return image

def fill(image, row, col, newColor, currentColor, rowLength, columnLength):
    if row < 0 or row > rowLength or col < 0 or col > columnLength or image[row][col] != currentColor:
        return

    image[row][col] = newColor

    fill(image, row + 1, col, newColor, currentColor, rowLength, columnLength)
    fill(image, row - 1, col, newColor, currentColor, rowLength, columnLength)
    fill(image, row, col + 1, newColor, currentColor, rowLength, columnLength)
    fill(image, row, col - 1, newColor, currentColor, rowLength, columnLength)
    
"""
Input: image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
], sr = 1, sc = 1, newColor = 2
Output: [
    [2,2,2],
    [2,2,0],
    [2,0,1]
]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Approach:

1. DFS recursion
2. Change every 4 direcional connected cell into that color
"""

image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
newColor = 2

print(floodFill(image, sr, sc, newColor))