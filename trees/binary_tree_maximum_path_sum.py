import tree_node

def maxPathSum(root):
    result = [root.val]

    def dfs(root):
        if not root:
            return 0

        left_max = dfs(root.left)
        right_max = dfs(root.right)
        left_max = max(left_max, 0) # Account for negatives
        right_max = max(right_max, 0)

        result[0] = max(result[0], root.val + left_max + right_max)

        return root.val + max(left_max, right_max)

    dfs(root)

    return result[0]

"""
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""

root = tree_node.TreeNode(1)
root.left = tree_node.TreeNode(2)
root.right = tree_node.TreeNode(3)
root.right.left = tree_node.TreeNode(4)
root.right.right = tree_node.TreeNode(5)

print(maxPathSum(root))

"""
def maxPathSum(root):
    result = [root.val]

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left) # Postorder traversal
        right = dfs(node.right)

        left = max(left, 0) # Don't include negatives
        right = max(right, 0)

        result[0] = max(result[0], node.val + left + right) # Calculate max with split

        return node.val + max(left, right) # Return max without split

    dfs(root)

    return result[0]

Approach:

Calculate postorder max. Compare splitting and not splitting paths

Time    : O(n)
Space   : O(n)

Takeaway:

Understand postorder traversal
"""