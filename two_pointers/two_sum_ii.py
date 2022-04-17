def twoSum(numbers, target):
    # 1. Two pointers, start and end of array
    # 2. Add them up
    # 3. Sum greater than target? Decrement right
    # 4. Else, increment left

    # 1.
    left = 0
    right = len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right] # 2.

        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1

    return -1

"""
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Approach:

numbers = [2,7,11,15], target = 9
           l
                   r

Two pointers, 0 and end of array. Add them up. If sum is greater than
target, decrement right. Else, decrement left

Time  : O(n)
Space : O(1)
"""

numbers = [2,7,11,15]
target = 26

print(twoSum(numbers,target))