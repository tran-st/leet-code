"""
Approach:

Base cases of F(0) and F(1). From there, increment a pointer up to n. 
Store two fibonacci numbers and calculate their sum on each iteration

1.  Base case of F(0) and F(1)
2.  Loop until n
3.  Calculate sum of two previous numbers
4.  Update first and second fib variables

Time    : O(n)
Space   : O(1)
"""
def fib(n):
    #   1.
    first_fib = 0
    second_fib = 1

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    for i in range(n - 1):  #   2.
        new_fib = first_fib + second_fib    #   3.

        first_fib = second_fib  #   4.
        second_fib = new_fib

    return new_fib

"""
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
"""

print(fib(3))