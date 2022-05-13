def search(arr, target):
    # 1. Left and right pointer
    # 2. While loop for when left is less than or equal to right
    # 3. Middle pointer
    # 4. If mid is less than target, check right half
    # 5. Else, check left half
    # 6. If mid == target, return it

    # 1.
    left = 0
    right = len(arr) - 1

    # 2.
    while left <= right:
        # 3.
        mid = left + (right - left) // 2 # Accounts for integer overflow

        # 6.
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: # 4.
            left = mid + 1
        else: # 5.
            right = mid - 1

    return -1

nums = [-1,0,3,5,9,12]
target = 9

print(search(nums, target))

"""
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Approach :

Have a left pointer starting from 0, a right pointer from the end of the array.
While left is less than right, have a middle pointer in between them.
If the middle is less than the target, search the first half of the array.
Else, search the second half

Time:  O(log n)
Space: O(1)
"""