def findMin(nums):
    left = 0
    right = len(nums) - 1

    result = nums[0]

    while left <= right:
        if nums[left] < nums[right]: # Array already sorted, take the minimum
            result = min(result, nums[left])

        mid = left + (right - left // 2)
        result = min(result, nums[mid])

        if nums[mid] >= nums[left]: # Array still sorted, search right side
            left = mid + 1
        else:
            right = mid - 1

        return result

        

"""
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

[3,4,5,1,2]
       l       
         r
     m 

left = 3
right = 4
mid = 2

Approach:

Find pivot. If mid >= left, array is sorted, search right. Track minimum

Time    : O(log n)
Space   : O(1)
"""

nums = [2,1]

print(findMin(nums))