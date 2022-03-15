def moveZeroes(nums):
    # 1. Two pointers, both at 0
    # 2. While right is less than length of array
    # 3. If right is equal to non zero, swap with left
    # 4. Increment left

    left = 0
    
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            
    return nums

"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Approach: 

[1,3,1,0,0]
     l
         r

Two pointers, starting at 0 and 1. If right is equal to a
non zero, swap with left and increment left

Time  : O(n)
Space : O(1)
"""

nums = [0,1,0,3,12]

print(moveZeroes(nums))