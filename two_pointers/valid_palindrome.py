def isPalindrome(s):
    s = "".join(x for x in s if x.isalnum()).lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1
    
    return True

"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Approach:

Two pointers. Check left char with right char

Time    : O(n)
Space   : O(1)
"""

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))