def rotate(nums, k):
    # 1. Reverse the entire array
    # 2. Reverse the array up to k - 1
    # 3. Reverse the rest of the array
    nums_length = len(nums)

    k = k % nums_length # Edge case

    # 1.
    nums = reverse(nums, 0, nums_length - 1)
    nums = reverse(nums, 0, k - 1) # 2.
    nums = reverse(nums, k, nums_length - 1) # 3.

    return nums
    
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Approach 1:

Cut the array into two, taking the last k elements into one array
and the rest into the other. Append the k part into a resulting array first.
Then append the rest

Time  : O(n)
Space : O(n)


Approach 2:

Reverse the entire array. Then reverse the rest of the array, not including the
firsts k elements. Then reverse the first k elements

Time  : O(n)
Space : O(1)
"""

nums = [-1]
k = 2

print(rotate(nums, k))