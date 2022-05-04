def longestPalindrome(s):
    result = ""
    max_length = 0

    def find_palindrome_from_middle(left, right, max_length, result):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            window_size = right - left + 1

            if window_size > max_length:
                result = s[left:right + 1]
                max_length = window_size

            left -= 1
            right += 1

        return result, max_length

    for i in range(len(s)):
        result, max_length = find_palindrome_from_middle(i, i, max_length, result)
        result, max_length = find_palindrome_from_middle(i, i + 1, max_length, result)


    return result


"""
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Approach:

"babad"
  l
     r

Brute force. Check all possible palindromes. Track max

Time    : O(n^3)
Space   : O(n)


Approach 2:

"babad"
 i
 l
 r

Triple pointer approach. From i, expand  left and right outwards. Check if left and right chars match

Time    : O()
"""

s = "cbbd"

print(longestPalindrome(s))