def twoSum(nums, target):
    # 1.  Initialize a dictionary with the first element in the array
    # 2.  Loops from the second element until the end
    # 3.  If at any point the dictionary contains an element such that
    #       it plus i == target, return that pair

    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]

        nums_map[nums[i]] = i

    return [-1, -1]

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Approach 1:

Sort the array. Have one pointer at the start of the array, one a the end.
Sum them up. If the sum is greater than the target, decrement the right pointer.
Else, decrement the left pointer

Time  : O(n log n)
Space : O(1)


Approach 2:

Walk through the array with a hash map. On each iteration, see if there is 
an entry in the map where nums[i] + dictionary == target

Time  : O(n)
Space : O(n)
"""

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))