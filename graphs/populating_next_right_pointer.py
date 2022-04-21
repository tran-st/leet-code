from collections import deque
import node

def connect(root):
    if not root:
        return []

    queue = deque()

    queue.append(root)

    while queue:
        pop_count = len(queue)

        for i in range(pop_count):
            current = queue.popleft()

            if i != pop_count - 1 and queue:
                current.next = queue[0]

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    return root

"""
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Approach:

BFS. Traverse each node, set next to remaining pointers on the queue

Time    : O(n)
Space   : O(n)
"""

root = node.node(1)
root.left = node.node(2)
root.right = node.node(3)
root.left.left = node.node(4)
root.left.right = node.node(5)
root.right.left = node.node(6)
root.right.right = node.node(7)

print(connect(root))


def connect2(root):
    current, next = root, root.left if root else None # Two pointers traversing tree

    while current and next:
        current.left.next = current.right

        if current.next: # Current.right.next value exists
            current.right.next = current.next.left

        current = current.next # Move along the same level

        if not current: # Level ended
            current = next
            next = current.left

    return root

"""
Approach 2:

BFS without queue. Traverse tree with two pointers

                                1->None
                    2->                      3
                4       5             6         7

Time    : O(n)
Space   : O(1)
"""