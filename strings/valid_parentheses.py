def isValid(s):
    if len(s) < 2:
        return False

    stack = []

    for char in s:
        if (char == "(" or
            char == "[" or
            char == "{"):

            stack.append(char)
        else:
            if stack:
                pop = stack.pop()
            else:
                return False

            if ((char == ")" and pop != "(") or
                (char == "]" and pop != "[") or
                (char == "}" and pop != "{")):
                return False

    return True if len(stack) == 0 else False

"""
Input: s = "()[]{}"
Output: true

Approach:

"()[]{}"
 i

Brute force. Check each open parentheses has closing. Change to " " to mark used

Time    : O(n^2)
Space   : O(1)


Approach 2:

Stack. Append open paretheses. Pop when closing parentheses. If close not match open. Return False

Time    : O(n)
Space   : O(n)
"""

s = "()[]{}"

print(isValid(s))