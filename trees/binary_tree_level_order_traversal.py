import tree_node
from collections import deque


def levelOrder(root):
    if not root: # Edge case
        return []

    result = []
    queue = deque()

    queue.append(root)

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

"""
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Approach:

BFS. Traverse tree, store level nodes in array

Time    : O(n)
Space   : O(n)
"""

root = tree_node.TreeNode(3)
root.left = tree_node.TreeNode(9)
root.right = tree_node.TreeNode(20)
root.right.left = tree_node.TreeNode(15)
root.right.right = tree_node.TreeNode(7)

print(levelOrder(root))