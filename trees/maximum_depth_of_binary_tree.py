from collections import deque
import tree_node

def maxDepth(root):
    # Base case
    if root == None:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def maxDepth2(root):
    # Base case
    if root == None:
        return 0

    queue = deque()
    queue.append(root)
    depth = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        depth += 1

    return depth
    
"""
Input: root = [3,9,20,null,null,15,7]
Output: 3

Approach:

DFS. Go down left all the way, then right

Time    : O(n)
Space   : O(n)
"""

root = tree_node.TreeNode(3)
root.left = tree_node.TreeNode(9)
root.right = tree_node.TreeNode(20)
root.right.left = tree_node.TreeNode(15)
root.right.right = tree_node.TreeNode(7)

print(maxDepth2(root))