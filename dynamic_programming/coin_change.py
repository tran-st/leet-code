def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            possible = a - c

            if possible >= 0:
                dp[a] = min(dp[a], 1 + dp[possible]) 

    return dp[amount] if dp[amount] != amount + 1 else -1

"""
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Approach:

Top down recursion. Start from 7, subtract each number until negattive

Time    : O(n * m)
Space   : O(n * m)


Approach 2:

Bottom up DP. Base case 0 with 0 coins. Loop through amount from 1.
For each coin, subtract it from amount. If >=0, find the min for DP curent amount
and subtracted amount

Time    : O(n * m)
Space   : O(n)
"""

coins = [1,2,3]
amount = 5

print(coinChange(coins, amount))