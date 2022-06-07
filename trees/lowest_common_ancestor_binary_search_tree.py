import tree_node

def lowestCommonAncestor(root, p, q):
    node = root

    while node:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < node.val and q.val < node.val:
            node = node.left
        else:
            return node

"""
                                6
                        2               8
                    0       4       7       9
"""

"""
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 8, q = 9
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Approach:

If p and q > node, search right tree.
If p and q < node, search left tree.
Else, return node

Time    : O(n)
Space   : O(1)
"""

root = tree_node.TreeNode(6)
root.left = tree_node.TreeNode(2)
root.right = tree_node.TreeNode(8)
root.left.left = tree_node.TreeNode(0)
root.left.right = tree_node.TreeNode(4)
root.left.left = tree_node.TreeNode(7)
root.left.right = tree_node.TreeNode(9)

p = tree_node.TreeNode(0)
q = tree_node.TreeNode(4)

print(lowestCommonAncestor(root, p, q))