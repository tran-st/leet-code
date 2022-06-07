import tree_node
from collections import deque


def isSameTree(p, q):
    p_queue = deque()
    q_queue = deque()

    if (p and not q) or (q and not p):
        return False

    p_queue.append(p)
    q_queue.append(q)

    while p_queue:
        for _ in range(len(p_queue)):
            p_node = p_queue.popleft()

            if not q_queue:
                return False

            q_node = q_queue.popleft()

            if (p_node.val is not q_node.val or
                p_node.left.val is not q_node.left.val or
                p_node.right.val is not q_node.right.val):
                return False

            if p_node.left:
                p_queue.append(p_node.left)
            if q_node.left:
                q_queue.append(q_node.left)
            if p_node.right:
                p_queue.append(p_node.right)
            if q_node.right:
                q_queue.append(q_node.right)


    return True


def isSameTree2(p, q):
    if not p and not q: # Both are not empty
        return True
    if (not p or not q) or (p.val is not q.val): # One is null while the other one isn't. Or if values don't match
        return False


    return (isSameTree2(p.left, q.left) and isSameTree2(p.right, q.right))

"""
Input: p = [1,2,3], q = [1,2,3]
Output: true

Approach:

DFS. Traverse both trees same time. Check each node per loop

Time    : O(n)
Space   : O(n)
"""

p = tree_node.TreeNode(1)
p.left = tree_node.TreeNode(2)
p.right = tree_node.TreeNode(3)

q = tree_node.TreeNode(1)
q.left = tree_node.TreeNode(2)
q.right = tree_node.TreeNode(3)

print(isSameTree2(p, q))