def lengthOfLIS(nums):
    nums_length = len(nums)
    dp = [1] * nums_length

    for i in range(nums_length - 1, -1, -1):
        for j in range(i + 1, nums_length):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

"""
2 2 4 3 2 1 1
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Approach:

[10,9,2,5,3,7,101,18]
      i
        j
 
DP. Start from last index. Go backwards. If previous smaller, check min for those
DPs.

Time    : O(n^2)
Space   : O(n)
"""

nums = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))