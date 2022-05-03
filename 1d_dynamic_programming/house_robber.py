def rob(nums):
    house1 = 0
    house2 = 0

    for num in nums:
        temp = max(num + house1, house2)
        house1 = house2
        house2 = temp

    return house2
"""
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Approach:

[1,2,3,1]
 i

Brute force. Start from each index. Skip one and add max

Time    : O(?)
Space   : O(1)


Approach 2:

[1,2,3,1]
 
house1 = 0
house2 = 0

n = 1        0            0
temp = max(house1 + n, house2) = 1
house1 = house2
house2 = n

"""

nums = [1,2,3,1]
print(rob(nums))