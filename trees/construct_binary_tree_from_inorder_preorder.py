import tree_node


def buildTree(preorder, inorder):
    if not preorder and not inorder:
        return None

    root = tree_node.TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
    

    return root

"""
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Approach:

First in preorder is always the root. Find root index in inorder. 
Left is from 0 in preorder to index in inorder. Right is from
index until end

Time    : O(n)
Space   : O(1)
"""

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(buildTree(preorder, inorder))

"""
def buildTree(preorder, inorder):
    if not preorder and not inorder:
        return None

    root = node(preorder[0])
    mid = inorder.index(root.val)

    root.left = buildTree(preorder[1 : mid + 1], inorder[: mid])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root

Approach:

preorder[0] == mid for that level. 1 : mid + 1 preorder elements on left tree. : mid inorder elements on right tree

Time    : O(n)
Space   : O(n)

Takeaway:

Understanding preorder and inorder traversal
"""