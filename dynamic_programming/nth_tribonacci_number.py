"""
Approach:

Same as fibonacci, but with 3 variables instead of 2?

1.  Base case for first 3 inputs
2.  Store first 3 in variables
3.  Loop until n, calculate sum for 3 variables
4.  Update variables accordingly


Time    : O(n)
Space   : O(1)
"""

def tribonacci(n):
    if n == 0:  #   1.
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2

    fib_first, fib_second, fib_third = 0, 1, 1  #   2.

    for i in range(n - 2):
        new_fib = fib_first + fib_second + fib_third
        fib_first = fib_second
        fib_second = fib_third
        fib_third = new_fib

    return new_fib

"""
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""

print(tribonacci(4))