def generate(numRows):
    #   1.
    result = [[1]]

    #   3.
    for i in range(numRows - 1):
        #   2.
        temp = [0] + result[i] + [0]
        row = []

        #   4.
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])

        result.append(row)

    return result
"""
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Approach:

1.  Initalize result to be [[1]]
2.  Append a 0 to the beginning and end of the array
3.  Loop until i == numRows - 1
4.  Loop until the second reaches the end of the array
5.  Append the sum of the second pointer and second pointer + 1
"""

numRows = 5
print(generate(numRows))