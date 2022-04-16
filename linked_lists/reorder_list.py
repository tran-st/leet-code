import list_node


def reorderList(head):
    # Find middle
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = slow.next
    slow.next = None
    prev = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # Reorder
    first = head
    second = prev

    while second:
        temp1 = first.next # Placeholders
        temp2 = second.next
        first.next = second # Shift first node to second half
        second.next = temp1
        first = temp1 # Shift both pointers along
        second = temp2
        
"""
1->4->2    
3

temp1 = first.next
temp2 = second.next
first.next = second
second.next = temp1
temp1.next = temp2

first = temp1
second = temp2

first = 1
second = 4
temp1 = 2
temp2 = 3


"""

"""
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Approach:

Store list in array. Two pointers, build new list

Time    : O(n)
Space   : O(n)


Approach 2:

Find middle. Reverse second half. Rebuild list

Time    : O(n)
Space   : O(1)
"""

head = list_node.ListNode(1)
head.next = list_node.ListNode(2)
head.next.next =  list_node.ListNode(3)
head.next.next.next = list_node.ListNode(4)

print(reorderList(head))