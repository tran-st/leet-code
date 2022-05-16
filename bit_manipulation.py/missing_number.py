def missingNumber(nums):
    result = len(nums)

    for i in range(len(nums)):
        result ^= i ^ nums[i]

    return result

"""
result = 3
[3,0,1]
[0,1,2]
"""

"""
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Approach:

Add nums to hash. Iterate through has to find the key that has value 0

Time    : O(n)
Space   : O(n)


Approach 2:

XOR

Time    : O(n)
Space   : O(1)
"""

nums = [3,0,1]

print(missingNumber(nums))