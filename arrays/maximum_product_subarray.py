def maxProduct(nums):
    result = max(nums)
    max_product = 1
    min_product = 1

    for n in nums:
        temp_max = max_product # Prevents double multiplication

        max_product = max(n * max_product, n * min_product, n)
        min_product = min(n * temp_max, n * min_product, n)

        result = max(result, max_product)


    return result

"""
Input: nums = [2,-3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Approach:

[2,3,-2,4,5]
          i

current_product = 20
max_product = 6

Time    : O(n)
Space   : O(1)
"""

nums = [2,3,-2,4]
print(maxProduct(nums))