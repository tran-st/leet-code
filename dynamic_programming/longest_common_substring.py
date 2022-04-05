def longestCommonSubsequence(text1, text2):
    text1_length = len(text1)
    text2_length = len(text2)

    dp = [[0 for _ in range(text1_length + 1)] for _ in range(text2_length + 1)] # +1 for empty string comparisions

    for i in range(text2_length - 1, -1, -1):
        for j in range(text1_length - 1, -1, -1):
            if text2[i] == text1[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    return dp[0][0]


"""
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Approach:

  a c e 
a 3 2 1 0
b 2 2 1 0
c 2 2 1 0
d 1 1 1 0
e 1 1 1 0
  0 0 0 0
"""

text1 = "abcde"
text2 = "ace" 

print(longestCommonSubsequence(text1, text2))