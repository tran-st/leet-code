import tree_node
from collections import deque


def invertTree(root):
    if not root:
        return None
    
    queue = deque()
    queue.append(root)

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node.left and node.right:
                node.left, node.right = node.right, node.left
            elif node.left: # Only left exists
                node.right = node.left
                node.left = None
            elif node.right:
                node.left = node.right
                node.right = None

    return root

"""
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

                                                    4
                                        7                       2
                                    1       3               6       9       
Approach:

BFS. Swap left and right

Time    : O(n)
Space   : O(n)
"""


def invertTree2(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left

    invertTree2(root.left)
    invertTree2(root.right)


    return root

root = tree_node.TreeNode(4)
root.left = tree_node.TreeNode(2)
root.right = tree_node.TreeNode(7)
root.left.left = tree_node.TreeNode(1)
root.left.right = tree_node.TreeNode(3)
root.right.left = tree_node.TreeNode(6)
root.right.right = tree_node.TreeNode(9)