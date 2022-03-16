def reverseString(s):
    # 1. Left and right pointers
    # 2. Loop once
    # 3. Swap

    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s
"""
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Approach:

Two pointers, start and end of array. Swap them,
increment and decrement

Time  : O(n)
Space : O(1)
"""

s = ["h","e","l","l","o"]
print(reverseString(s))