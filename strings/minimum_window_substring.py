def minWindow(s, t):
    if t == "": # Edge case
        return ""

    t_hash = {}
    window_hash = {}

    for char in t:
        t_hash[char] = 1 + t_hash.get(char, 0)

    have, need = 0, len(t_hash)
    result = [-1, -1]
    result_length = len(s) + 1

    left = 0

    for right in range(len(s)):
        right_char = s[right]
        window_hash[right_char] = 1 + window_hash.get(right_char, 0)

        if right_char in t_hash and window_hash[right_char] == t_hash[right_char]: # Exact match for char and length
            have += 1

        while have == need: # All chars and lengths met
            window_length = right - left + 1

            if window_length < result_length:
                result = [left, right]
                result_length = window_length

            left_char = s[left]

            window_hash[left_char] -= 1

            if left_char in t_hash and window_hash[left_char] < t_hash[left_char]: # Decrementing char in t_hash, have is not longer valid
                have -= 1

            left += 1


    return s[result[0]: result[1] + 1] if result_length != len(s) + 1 else ""

"""
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"ADOBECODEBANC"
  l
             r

"ABC"

Approach:

Brute force. Add t to hash. Walk through s. Each step, increment window_hash. Check if both hashes match

Time    : O(n^2)
Space   : O(26)


"ADOBECODEBANC"
      l
             r

"ABC"

t_hash = {
    A:1
    B:1
    C:1
}

window_hash = {     have = 3    need = 3    result = 6
    A:1
    B:1
    C:1
    D:1
    E:2
    O:1
    N:1
}

Approach 2:

Sliding window. Add t to hash. Slide through s and keep a hash. If hashes match, calculate min distance. Shorten
window until hash doesn't match

Time    : O(n)
Space   : O(26)
"""

s = "aa"
t = "aa"

print(minWindow(s, t))