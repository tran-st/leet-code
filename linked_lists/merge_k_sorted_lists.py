import list_node


def mergeKLists(lists):
    # Edge case
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged_lists = [] # Temporary storage
        lists_length = len(lists)

        for i in range(0, lists_length, 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 in range(lists_length) else None

            merged_lists.append(mergeTwoLists(list1, list2))
        
        lists = merged_lists

    return lists[0]

def mergeTwoLists(list1, list2):
    dummy = list_node.ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

        # If any list remains, append the rest
    if list1:
            tail.next = list1
    if list2:
            tail.next = list2

    return dummy.next
"""
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Approach:

Sort each node one by one for each list

Time    : O(n * k)
Space   : O(1)


Approach 2:

Merge sort approach. Merge every two lists until one is left

Time    : O(n log k)
Space   : O(n)
"""

root = list_node.ListNode(1)
root.next = list_node.ListNode(2)
root.next.next = list_node.ListNode(4)

root2 = list_node.ListNode(1)
root2.next = list_node.ListNode(3)
root2.next.next = list_node.ListNode(4)

root3 = list_node.ListNode(2)
root3.next = list_node.ListNode(6)

lists = []
lists.append(root)
lists.append(root2)
lists.append(root3)

print(mergeKLists(lists))