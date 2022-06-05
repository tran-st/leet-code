def isPalindrome(x):
    x = str(x)

    left = 0
    right = len(x) - 1

    while left < right:
        if x[left] != x[right]:
            return False
        
        left += 1
        right -= 1

    return True

"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Approach:

121

Convert to string. Two pointers

Time    : O(n)
Space   : O(1)
"""

print(isPalindrome(1211))


def isPalindrome2(x):
    divisor = 1

    while x > divisor * 10: # Find multiplier to extract left int
        divisor *= 10

    while x:
        right = x % 10
        left = x // divisor

        if left != right:
            return False

        x = x % divisor
        x //= 10

        divisor //= 100


    return True

"""
100
1 * 10 * 10
100
"""

"""
Approach 2:

Extract right with % 10. Find how big num is. 1 * 10 while < x
"""

print(isPalindrome2(121))