def maxSubArray(nums):
    # 1. Track max and current sum
    # 2. Step through nums once
    # 3. If current_sums is ever negative, start the count over

    # 1.
    max_sum = nums[0]
    current_sum = nums[0]

    # 2.
    for num in nums:
        # 3.
        if current_sum < 0:
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum

"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Approach 1:

nums = [-2,1,-3,4,-1,2,1,-5,4]
           l
                       r
max = 4
current_sum = 3
highest_r = 6

Time  : O(n)
Space : O(1)


Approach 2:
nums = [-2,1,-3,4,-1,2,1,-5,4]
                            i
current_sum = 5
max = 6

Step through the whole array once. On each step,
track the current and max sum. If the current sum is ever
negative, start the current sum from 0. This discounts all the
negative values on the left sub array which will not count

Time  : O(n)
Space : O(1)

"""

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))