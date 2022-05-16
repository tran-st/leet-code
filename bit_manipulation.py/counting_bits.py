def countBits(n):
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i: # Find most significant bit
            offset = i

        dp[i] = 1 + dp[i - offset]

    return dp

"""
0      0
1      1
2     10
3     11
4    100
5    101
6    110
7    111
8   1000
"""

"""
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Approach:

For each number in range, calculate bits

Time    : O(n log n)
Space   : O(1)


Approach 2:

DP. Calculation for n is 1 + dp[n - most significant bit]

Time    : O(n)
Space   : O(1)
"""

print(countBits(7))