def diameterOfBinaryTree(root):
    result = [0]

    def dfs(node):
        if not node:
            return -1

        left = dfs(node.left)
        right = dfs(node.rigth)

        result[0] = max(result[0], 2 + left + right) # Calculate diameter


        return 1 + max(left, right) # Return height
    pass

"""
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Approach:

                                    1
                        2                       3
                4               5

DFS recursion. Calculate diameters and heights for left and right
"""