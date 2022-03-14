def merge(nums1, m, nums2, n):
    k = len(nums1) - 1

    # 2.
    while nums1[k] == 0:
        if m > 0 and nums1[m - 1] > nums2[n - 1]: # 3.
            nums1[m - 1], nums1[k] = nums1[k], nums1[m -1] # 4.
            m -= 1
        else:
            nums2[n - 1], nums1[k] = nums1[k], nums2[n -1]
            n -= 1

        k -= 1

    return nums1

"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Approach 1:

[1,2,3,0,0,0]
 i
[2,5,6]
 j

 1. Two pointers
 2. Step through first array
 3. If j is less than i, swap
 4. If i is 0, increment j after swap

 Time  : O(n + m)
 Space : O(1)


 Approach 2:

 [1,2,3,0,5,6]
      i
        k
[2,0,0]
 j

 1. Use m and n as given pointers
 2. Start from end of nums1
 3. Put the largest elements from the two arrays there
 4. Swap out zeroes
 5. Use k as a zero pointer
"""

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3

print(merge(nums1, m, nums2, n))