def isAnagram(s, t):
    if len(s) != len(t): # Edge case
        return False

    s_hash = {}
    t_hash = {}

    for char in s:
        s_hash[char] = 1 + s_hash.get(char, 0)

    for char in t:
        t_hash[char] = 1 + t_hash.get(char, 0)

    if s_hash != t_hash:
        return False

    
    return True

"""
Input: s = "anagram", t = "nagaram"
Output: true

Approach:

Hash. Iterate both strings and add them to two seperate hashes. If hashes don't match, return false

Time    : O(n)
Space   : O(1)
"""

s = "rat"
t = "car"

print(isAnagram(s, t))