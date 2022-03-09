def searchInsert(nums, target):
    # 1.  Left and right pointers for binary search
    # 2.  Mid pointer
    # 3.  If the target is bigger than the last element
    #   return the size of the array + 1
    # 4.  Perform standary binary search
    # 5.  If target not found, return mid + 1

    # 1.
    left = 0
    right = len(nums) - 1

    # 3.
    if nums[right] < target:
        return right + 1
    elif nums[left] > target:
        return left
    
    # 4.
    while left <= right:
        # 2.
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

"""
Input: nums = [1,3,5,6], target = 2
Output: 1

Approach:

Standard binary search. One edge case if the target is bigger than the array.
Then just return the length of the array. If not, then just perform regular 
binary search. If binary search completes without a result, return mid + 1

Time  : O(log n)
Space : O(1)
"""

nums = [1, 3, 5, 6]
target = 2

print(searchInsert(nums, target))