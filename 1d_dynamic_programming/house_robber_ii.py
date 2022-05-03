def rob(nums):
    return max(helper(nums[:-1]), helper(nums[1:]))

def helper(nums):
    house1 = 0
    house2 = 0

    for num in nums:
        max_profit = max(house1 + num, house2) # Rob current and two houses ago? Or just current house
        house1 = house2
        house2 = max_profit # Increment houses

    return house2

"""
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Approach:

    [2,3,2,1]
         4 4 
 max_profit = 2

 DP. Check max of robbing current house + house 2 doors down. Or just rob previous house

 Time   : O(n)
 Space  : O(1)
"""

nums = [2,3,2,1]
print(rob(nums))