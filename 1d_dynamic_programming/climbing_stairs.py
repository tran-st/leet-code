"""
Approach 2:

Dynamic programming. Start from the top step. One possible way to get there.
For the next step, it would also be one possible way to get from the second to last step
to the last step. For the third step down, it would be the sum of the last two steps

Time    : O(n)
Space   : O(1)
"""
def climbStairs(n):
    two = 1
    one = 1

    for _ in range(n - 1):
        one, two = one + two, one
    
    
    return one

"""
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Approach 1:

Recursion? Have base cases of 1 and 2 steps. Recurse by calling and subtracting 1 or 2 steps, top down

n = 3
1.  climbStairs(3 - 1)
1.  climbStairs(3 - 2)
2.  climbStairs(2 - 1)
    base case
2.  climbStairs(2 - 0)
    base case
2.  climbStairs(1 - 1)
    base case
2.  climbStairs(1 - 2)
    base case

Time    : O(n)
Space   : O(n)
"""

print(climbStairs(0))

"""
def climbStairs2(n):
    one = 1
    two = 1

    for _ in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one

Approach:

Recursion. DFS until base case. dfs(n - 1) + dfs(n - 2)

Time    : O(n) with memoization
Space   : O(n)

Takeaway:

Understand basic recursion, DFS

Approach 2:

DP. Start from top of staircase. Last two steps will always take one action, so that's the base case.
Add up previous two values

Time    : O(n)
Space   : O(1)

Takeaway:

Understand basic DP
"""