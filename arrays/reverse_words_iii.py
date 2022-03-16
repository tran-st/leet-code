def reverseWords(s):
    # 1.
    words = s.split()
    result = []

    # 2.
    for word in words:
        result.append(word[::-1])

    return " ".join(result)
"""
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Approach 1:

s = "Let's take LeetCode contest"
           i
               j

1. Two pointers
2. Move j along until white space
3. Reverse all chars from i to j
4. Set i to j
5. Repeat until end of array

Time  : O(n)
Space : O(1)


Approach 2:

1. Split words
2. For each word, append it's reverse into a resulting array

Time  : O(n)
Space : O(n)
"""

s = "Let's take LeetCode contest"
print(reverseWords(s))