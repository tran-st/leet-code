"""
Approach 2:

"pwwkew"
   l
     r

Sliding window. Hash map. Start both pointers at 0. Step through
and add each character into hash map. If any character count ever exceeds 1, increment
the starting pointer and pop each character out until it becomes 1. Keep track of max 
length

1.  Initialize pointers
2.  Initiliaze hash map
3.  Loop through until right pointer hits end of array
4.  On each iteration, add that character to the map
5.  Check if that character count exceeds 1
    If it does, increment left pointer and update map
    until it is equal to 1
6.  Track max count

Time    : O(n)
Space   : O(n)
"""

def lengthOfLongestSubstring(s):
    s_length = len(s)

    if s_length <= 1:
        return s_length

    #   1.
    left = 0
    character_map = {}  #   2.
    current_length = 0
    max_length = 0

    #   3.
    for right in range(s_length):
        #   4.
        if s[right] in character_map:
            while character_map[s[right]] > 0:    #   5.
                character_map[s[left]] -= 1
                left += 1
                current_length -= 1 #   6.

            character_map[s[right]] += 1
        else:
            character_map[s[right]] = 1

        current_length += 1 #   6.
        max_length = max(max_length, current_length)
            

    return max_length

"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Approach:

Brute force. Hash map. For each character, walk through the 
entire array, adding each character into a hash map. If the count 
for a character ever exceeds one, start over and loop onto next character.
Track the count

Time    : O(n ^ 2)
Space   : O(n)
"""

s = "au"

print(lengthOfLongestSubstring(s))