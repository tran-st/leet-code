def sortedSquares(nums):
    # 1. Two pointers, start and end of array
    # 2. Find which pointer is larger
    # 3. Insert into resulting array

    # 1.
    left = 0
    right = len(nums) - 1

    result = []

    while left <= right:
        if abs(nums[right]) > abs(nums[left]): # 2.
            result.append(nums[right] * nums[right]) # 3.
            right -= 1
        else:
            result.append(nums[left] * nums[left]) # Covers when right == left
            left += 1

    return result[::-1]

"""
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Approach 1:

Step through the entire array, squaring each element. Sort the array afterwards

Time  : O(n log n)
Space : O(1)


Approach 2:

Two pointer approach. Start left from the start of the array, right from the end.
Compare which is largest, as the largest element in the array would be on either end.
Insert it into the last slot of the resulting array

Time  : O(n)
Space : O(n)
"""

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))