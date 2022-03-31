import list_node

def reverseList(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev
    
def reverseList2(head):    
    def recursion(prev, curr):
        if not curr:
            return prev

        temp = curr.next
        curr.next = prev

        return recursion(curr, temp)

    result = recursion(None, head)


    return result

"""
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Approach:

2 -> 3 -> 4 -> 5
1 -> None

node = 1
temp = 2

Take first node, set to null. Take next node's next and set that to first node. Repeat

Time    : O(n)
Space   : O(1)
"""

head = list_node.ListNode(1)
head.next = list_node.ListNode(2)
head.next.next = list_node.ListNode(3)
head.next.next.next = list_node.ListNode(4)
head.next.next.next.next = list_node.ListNode(5)

print(reverseList2(head))