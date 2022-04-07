def wordBreak(s, wordDict):
    s_length = len(s)
    dp = [False] * (s_length + 1)

    dp[s_length] = True

    for i in range(s_length - 1, -1, -1):
        for w in wordDict:
            w_length = len(w)
            if i + w_length <= s_length and s[i : i + w_length] == w:
                dp[i] = dp[i + w_length]
            if dp[i]:
                break
    

    return dp[0]

"""
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Approach:

DP. Start end of string. Check length of index + length of word in dictionary
is less or equal to string
"""

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s, wordDict)) 