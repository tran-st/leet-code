def canJump(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False

"""
[2,3,1,1,4]
 i

goal = 0
i = 0
nums[i] = 2
i + nums[i] = 2
"""

"""
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Approach:

[2,3,1,1,4]
       i

DP. Go backwards. Add i and nums[i]

Time    : O(n)
Space   : O(1)
"""

nums = [2,3,1,1,4]
print(canJump(nums))