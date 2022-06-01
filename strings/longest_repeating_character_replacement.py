def characterReplacement(s, k):
    left = 0
    max_count = 0
    k_count = k
    char_hash = {}

    for right in range(len(s)):
        while len(char_hash) > k + 1:
            char_hash[left] -= 1
            if char_hash[left] == 0:
                char_hash.pop(s[left])
            left += 1

        if s[right] in char_hash:
            char_hash[s[right]] += 1
        else:
            char_hash[s[right]] = 1

        result = max(max_count, right - left + 1)

    return result

"""
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Approach:

s = "ABAB", k = 2
     l
        r

k = 0

Sliding window. Store chars in hash of size k + 1. Track count

Time    : O(n)
Space   : O(k)
"""

def characterReplacement2(s, k):
    left = 0
    char_hash = {}
    result = 0

    for right in range(len(s)):
        char_hash[s[right]] = 1 + char_hash.get(s[right], 0) # Add current char

        while (right - left + 1) - max(char_hash.values()) > k:
            char_hash[s[left]] -= 1
            left += 1
        
        result = max(result, right - left + 1)


    return result

"""
Approach 2:

"ABABCD"
    l
      r

char_hash = {
    A:0
    B:1
    C:1
    D:1
}

window_size = 4
window_size - max(char_hash) = 2
result = 4

Sliding window. Store chars in hash. If max frequency - max hash values is greater than k,
slide left up

Time    : O(n)
Space   : O(n)
"""

s = "ABABCD"
k = 2

print(characterReplacement2(s, k))