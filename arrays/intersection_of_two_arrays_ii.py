def intersect(nums1, nums2):
    #   1.
    num_hash = {}
    result = []

    #   2.
    for num in nums1:
        if num in num_hash: #   3..
            num_hash[num] +=1
        else:
            num_hash[num] = 1

    #   4.
    for num in nums2:
        if num in num_hash and num_hash[num] > 0:
            num_hash[num] -= 1

            result.append(num)
            
    return result

"""
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Approach:

1.  Initialize dictionary
2.  Walk through first array
3.  Add into dictionary
4.  Walk through second array
5.  Check if element exists in dictionary
6.  Append those into resulting array

Time    : O(n + m)
Space   : O(n)
"""

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersect(nums1, nums2))