import list_node

def middleNode(head):
    # 1.
    slow = head
    fast = head # 2.

    # 3.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

"""
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

First traverse the list to get the length. Divide by two.
Traverse it again until mid point

Approach 1:

1.  Track length
2.  Walk through linked list
2a. Increment length
3.  Calculate mid
3a. Reset current
4.  Walk through linked list again, up to mid

Time  : O(n)
Space : O(1)


Approach 2:

1.  Slow pointer
2.  Fast pointer
3.  Step through linked list
"""


def middleNode2(head):
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False

"""
Approach:

Two pointers. Fast and slow. Loop until slow None. If pointers cross, return True

Time    : O(n)
Space   : O(1)
"""

head = list_node.ListNode(1)
head.next = list_node.ListNode(2)
head.next.next = list_node.ListNode(3)
head.next.next.next = list_node.ListNode(4)
head.next.next.next.next = list_node.ListNode(1)

print(middleNode(head))