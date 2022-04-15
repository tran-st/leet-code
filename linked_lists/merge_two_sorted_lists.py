import list_node

def mergeTwoLists(list1, list2):
    dummy = list_node.ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next
    
"""
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Approach:

Loop until both lists null. Append if less than or equal

Time    : O(n + m)
Space   : O(n + m)
"""

list1 = [1,2,4]
list2 = [1,3,4]

print(mergeTwoLists(list1, list2))