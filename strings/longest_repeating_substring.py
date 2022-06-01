def lengthOfLongestSubstring(s):
    s_length = len(s)
    left, right = 0, 0
    count, max_count = 0, 0

    char_set = set()

    while right < s_length:
        if s[right] not in char_set:
            char_set.add(s[right])
            count += 1
            right += 1
            max_count = max(max_count, count)
        else:
            while s[right] in char_set:
                char_set.remove(s[left])
                count -= 1
                left += 1

                if s[left - 1] == s[right]:
                    break
                
    return max_count

"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Approach:

"abcabcbb"
  l
    r 

char_set = {b,c}
count = 3
max_count = 3

Sliding window. Walk through and store into set. If char is in set, increment left pointer
and pop from set until it's no longer in the set. Track count

Time    : O(n)
Space   : O(n)
"""

s = "accbbcg"

print(lengthOfLongestSubstring(s))