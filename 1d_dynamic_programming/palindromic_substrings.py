def countSubstrings(s):
    s_length = len(s)
    result = 0

    def find_palindrome_from_middle(left, right, result):
        while (left in range(s_length) and 
               right in range(s_length) and 
               s[left] == s[right]):
               result += 1

               left -= 1
               right += 1

        return result

    for i in range(len(s)):
        result = find_palindrome_from_middle(i, i, result)
        result = find_palindrome_from_middle(i, i + 1, result)


    return result

"""
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Approach:

Brute force. Check palindrome from every index

"abc"
   l
   r

Time    : O(n^3)
Space   : O(n)


Approach 2:

"abc"
 i
 l
 r

Triple pointer. From each i, set left, right to i. Expand outward, check palindrome. Track count

Time    : O(n^2)
Space   : O(n)
"""

s = "aaa"

print(countSubstrings(s))