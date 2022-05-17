def hammingWeight(n):
    result = 0

    while n:
        n &= n - 1
        result += 1

    return result

"""
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Approach:

Remove 1s with % 2. Shift all bits to the right

Time    : O(1)
Space   : O(1)


Approach 2:

Remove 1s with & (n -1). Increment result

Time    : O(1)
Space   : O(1)
"""

n = 0b00000000000000000000000000001011

print(hammingWeight(n))