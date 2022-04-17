def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: # Duplicate
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]

            if three_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif three_sum > 0:
                right -= 1
            else:
                left += 1
    
    return result

"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Approach:

[-1,0,1,2,-1,-4]
  i
      j
        k

Brute force. 3 pointers. Find every possible combination

Time    : O(n^3)
Space   : O(1)


Approach 2:

[-4,-1,-1,0,1,2]
  i
     j
              k

current_sum = -3 

Time    : O(n log n^2)
Space   : O(1)

Sort first. 3 pointers. Check for duplicates
"""

nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))