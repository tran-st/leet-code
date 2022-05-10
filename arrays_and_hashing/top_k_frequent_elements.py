from heapq import *


def topKFrequent(nums, k):
    nums_hash = {}
    max_heap = []
    result = []

    for num in nums:
        nums_hash[num] = nums_hash.get(num, 0) + 1

    for num, count in nums_hash.items():
        heappush(max_heap, (-count, num))

    for _ in range(k):
        pop = heappop(max_heap)
        result.append(pop[1])
    
    return result

"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approach:

nums = [1,1,1,2,2,3], k = 2

Heap

Time    : O(k log n)
Space   : O(n)
"""

nums = [1,1,1,2,2,2,2,3,3,3,3]
k = 2

print(topKFrequent(nums, k))

def topKFrequent2(nums, k):
    nums_length = len(nums)
    bucket = [[] for _ in range(nums_length + 1)] # Indexed by count
    nums_hash = {}
    result = []
    k_counter = k

    for num in nums:
        nums_hash[num] = 1 + nums_hash.get(num, 0)

    for num, count in nums_hash.items():
        bucket[count].append(num)

    for i in range(len(bucket) - 1, -1, -1):
        while bucket[i]:
            result.append(bucket[i].pop())
            k_counter -= 1

            if k_counter == 0:
                return result

"""
Approach 2:

Bucket sort

Time    : O(n)
Space   : O(n)
"""

print(topKFrequent2([1], 1))