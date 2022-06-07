import tree_node


def isValidBST(root):
    def dfs(node, left_bound, right_bound):
        if not node:
            return True

        if not (node.val > left_bound and node.val < right_bound):
            return False

        return (dfs(node.left, left_bound, node.val) and
                dfs(node.right, node.val, right_bound))
        

    return dfs(root, -float("inf"), float("inf"))

"""
Input: root = [2,1,3]
Output: true

Approach:

Root node > -inf and < inf. Left > - inf and < root. 
Right < inf and > root

Time    : O(n)
Space   : O(1)
"""

root = tree_node.TreeNode(2)
root.left = tree_node.TreeNode(2)
root.right = tree_node.TreeNode(2)
# root.right.left = tree_node.TreeNode(6)
# root.right.right = tree_node.TreeNode(8)

print(isValidBST(root))

"""
def isValidBST(root):
    def dfs(node, lower_bound, upper_bound):
        if not node:
            return True

        if not (node.val < upper_bound and node.val > lower_bound):
            return False

        return (dfs(node.left, lower_bound, node.val) and dfs(node.right, node.val, upper_bound))

    dfs(root, -float("inf"), float("inf"))
    pass

Approach:

Recognize the upper and lower bounds of a BST. Traverse left, upper bound changes. Traverse right, lower changes
Recursion DFS

Time    : O(n)
Space   : O(n)
"""