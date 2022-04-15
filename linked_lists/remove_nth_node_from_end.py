import list_node

def removeNthFromEnd(head, n):
    #   1.
    dummy = list_node.ListNode(0, head)
    left = dummy
    right = head 


    #   2.
    for i in range(n):
        right = right.next

    #   3.
    while right:
        left = left.next
        right = right.next

    #   4.
    left.next = left.next.next

    return dummy.next

"""
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

[1,2,3,4,5]
 s
     e

Approach:

1.  Start one pointer from the beginning of the list
2.  Start second pointer from n
3.  Step through list and increment both pointers until second 
    pointer reaches end
4.  Make first pointer = next.next
"""

head = list_node.ListNode(1)
# head.next = list_node.ListNode(2)
# head.next.next = list_node.ListNode(3)
# head.next.next.next = list_node.ListNode(4)
# head.next.next.next.next = list_node.ListNode(5)

print(removeNthFromEnd(head, 1))