import tree_node


def isSubtree(root, subroot):
    if not subroot:
        return True
    if not root:
        return False

    if sameTree(root, subroot):
        return True

    return (isSubtree(root.left, subroot) or
            isSubtree(root.right, subroot))
    

def sameTree(node, subNode):
    if not node and not subNode: # Both null
        return True

    if node and subNode and node.val == subNode.val: # Only one is null or vals not equal
        return (sameTree(node.left, subNode.left) and
                sameTree(node.right, subNode.right))

    return False

"""
                                    3
                            4               5
                        1       2       
"""

"""
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Approach:

BFS until find subroot value. Then double bfs to compare values

Time    : O(n)
Space   : O(1)
"""

root = tree_node.TreeNode(3)
root.left = tree_node.TreeNode(4)
root.right = tree_node.TreeNode(5)
root.left.left = tree_node.TreeNode(1)
root.left.right = tree_node.TreeNode(2)

subRoot = tree_node.TreeNode(4)
subRoot.left = tree_node.TreeNode(1)
subRoot.right = tree_node.TreeNode(2)
subRoot.left.left = tree_node.TreeNode(1)

print(isSubtree(root, subRoot))