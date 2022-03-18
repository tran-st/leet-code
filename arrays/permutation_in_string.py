"""
s1 = "ab", s2 = "eidbaooo"
                     l
                      r

Approach:

Add one string to a hash map. Use sliding window on the other.
If a character from the second string exists in the map, decrement the map
and increase the current count. While it doesn't, increment the left pointer
and add it back into the map. Repeat until end

1.  Initialize map
2.  Add s1 to map
3.  Left window
4.  Slide through s2 and add to dictionary
5.  Once lenghts match, check if dictoinaries match

Time    : O(n + m)
Space   : O(n)
"""

def checkInclusion(s1, s2):
    #   1.
    s1_character_map = {}
    s2_character_map = {}
    left = 0    #   3.

    #   2.
    for char in s1:
        if char in s1_character_map:
            s1_character_map[char] += 1
        else:
            s1_character_map[char] = 1

    #   4.
    for right in range(len(s2)):
        left_char = s2[left]
        right_char = s2[right]

        while (right - left) > len(s1) - 1:

            s2_character_map[left_char] -= 1
            if s2_character_map[left_char] == 0:
                del s2_character_map[left_char]
            
            left += 1

        if s2[right] in s2_character_map:  #   5.
            s2_character_map[right_char] += 1
        else:
            s2_character_map[right_char] = 1

        if s1_character_map == s2_character_map:
            return True

    return False

"""
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

s1 = "ab"
s2 = "eidbaooo"

print(checkInclusion(s1, s2))