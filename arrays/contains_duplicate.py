def containsDuplicate(nums):
    # 1. Initialize set
    # 2. Loop through array
    # 3. Element exists in set?
    # 4. If not, add it
    # 5. If so, return true

    nums_set = set()

    for num in nums:
        if num in nums_set:
            return True

        nums_set.add(num)

    return False

"""
Input: nums = [1,2,3,1]
Output: true

Approach:

Step through the entire array, adding each element into a set.
If element already exists, return true

Time  : O(n)
Space : O(n)
"""

nums = [1,2,3,1]
print(containsDuplicate(nums))