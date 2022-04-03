def productExceptSelf(nums):
    nums_length = len(nums)

    left = [None] * (nums_length)
    right = [None] * (nums_length)
    result = [None] * (nums_length)

    product = 1

    for i in range(nums_length):
        left[i] = product
        product *= nums[i]

    product = 1

    for i in range(nums_length - 1, -1, -1):
        right[i] = product
        product *= nums[i]

    for i in range(nums_length):
        result[i] = left[i] * right[i]

    return result

"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Approach:

Brute force. Two for loops. If j != i, multiply to new product.

Time    : O(n^2)
Space   : O(n)


Approach 2:

Prefix combo hack. Left array, multiply each index going to the right.
Repeast for right array, multiply right to left. Multiply left by
right array

Time    : O(n)
Space   : O(n)
"""

nums = [1,2,3,4]

print(productExceptSelf(nums))