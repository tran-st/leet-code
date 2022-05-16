def search(nums, target):
    pivot = findPivot(nums)

    if pivot[0] == target: return pivot[1] # Happy path

    if pivot[1] == 0 or target < nums[0]: # Array is unrotated or target is in second half
        return binarySearch(nums, pivot[1], len(nums) - 1, target)

    return binarySearch(nums, 0, pivot[1] - 1, target) # Search first half

def findPivot(nums):
    left = 0
    right = len(nums) - 1
    result = (nums[0], 0)

    while left <= right:
        if nums[left] < nums[right]:
            if nums[left] < result[0]:
                result = (nums[left], left)

        mid = left + (right - left // 2)
        if nums[mid] < result[0]: # Potential new low
            result = (nums[mid], mid)

        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    return result

def binarySearch(nums, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Approach:

Linear search. Step through array once

Time    : O(n)
Space   : O(1)


Approach 2:

Find pivot. See if target > right. If it is, search the other array

Time    : O(log n)
Space   : O(1)
"""

nums = [4,5,6,7,0,1,2]
target = 6

print(search(nums, target))