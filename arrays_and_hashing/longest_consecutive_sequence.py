from heapq import heapify, heappop


def longestConsecutive(nums):
    if len(nums) == 0: # Edge case
        return 0

    count, max_count = 1, 1
    heapify(nums)

    prev = heappop(nums)
    while nums:
        current = heappop(nums)

        if current == prev + 1:
            count += 1
            max_count = max(max_count, count)
        elif current == prev:
            continue
        else:
            count = 1

        prev = current

    return max_count

"""
[1,2,4,5,6,8,9]
count = 2
max_count = 4
"""

"""
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Approach:

Min heap. Heapify for o(n). Pop and increment count if consecutive 

Time    : O(n)
Space   : O(n)
"""

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums))

def longestConsecutive2(nums):
    nums_set = set(nums)
    max_length = 0

    for num in nums_set: # Traverse set
        if num - 1 not in nums_set: # At start of sequence
            length = 0

            while (num + length) in nums_set: # Check length of sequence
                length += 1
                max_length = max(max_length, length)

    return max_length

"""
Approach 2:

[100,4,2,101,200,3,1]

1,2,3,4      100   200

Add to set. If have left neighbor, it's not the start of a sequence. Check for right neighbor

Time    : O(n)
Space   : O(n)
"""

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive2(nums))