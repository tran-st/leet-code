def numDecodings(s):
    dp = { len(s) : 1}

    def dfs(i):
        if i in dp:
            return dp[i]

        if s[i] == "0":
            return 0

        res = dfs(i + 1)
        
        if (i + 1 < len(s) and (s[i] == "1" or
            s[i] == "2" and s[i + 1] in "0123456")):
            res += dfs(i + 2)

        dp[i] = res

        return res

    return dfs(0)

"""
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Approach:

Brute force

                121

          1             12
        2   21 b        1 b
      1 b

Time    : O(2 ^ n)
Space   : O()
"""

def numDecodings2(s):
    s_length = len(s)

    if s_length == 0:
        return 0

    dp = [0 for _ in range(s_length + 1)]

    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1

    for i in range(2, s_length + 1):
        one_jump = int(s[i - 1: i])
        two_jump = int(s[i - 2: i])

        if 0 < one_jump <= 9:
            dp[i] += dp[i - 1]

        if 10 <= two_jump <= 26:
            dp[i] += dp[i - 2]

    return dp[s_length]

"""
Approach 2:

DP

"121"
 i
  i+1
   i+2

2 2 6
22 6
2 26

Base case if s[i] == 0: dp[0] == 0. dp[i] += dp[i - 1] if valid for one jump. dp[i] += dp[i-2] also if valid for two jumps

Time    : O(n)
Space   : O(1)
"""

s = "12"
print(numDecodings2(s))