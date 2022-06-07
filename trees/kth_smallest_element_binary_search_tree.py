import tree_node


def kthSmallest(root, k):
    if not root:
        return -1

    count = [0 for i in range(2)]
    count[0] = 0

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        count[0] += 1
        if count[0] == k: count[1] = node.val
        dfs(node.right)

    dfs(root)

    return count[1]


def kthSmallest2(root, k):
    if not root:
        return -1

    stack = []
    k_count = 0

    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        # Made it all the way left
        current = stack.pop()
        k_count += 1
        
        if k_count == k: return current.val

        current = current.right


"""
Input: root = [3,1,4,null,2], k = 1
Output: 1

Approach:

Inorder traversal. Increment counter. Once counter matches k, return that value

Time    : O(log n)
Space   : O(1)
"""

root = tree_node.TreeNode(3)
root.left = tree_node.TreeNode(1)
root.right = tree_node.TreeNode(4)
root.left.right = tree_node.TreeNode(2)

print(kthSmallest(root, 3))

"""
def kthSmallest(root, k):
    k_count = 0
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k_count += 1

        if k_count == k:
            return current.val

        current = current.right

Approach:

In order traversal. Once smallest node is reached, traverse up until k

Takeaway: Understand in order traversal

Time    : O(n)
Space   : O(n)
"""