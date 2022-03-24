"""
Approach:

[1,100,1,1,1,100,1,1,100,1]
       t
    o

DP. Start from the top floor. Calculate the minimum cost to get there
comparing the last two steps

1.  Append the top floor to the cost array
2.  Loop from the top floor
3.  Change the ith stair to the minimum cost to take one or two steps
4.  Once the ground floor is reached, return that minimum cost

Time    : O(n)
Space   : O(1)
"""

def minCostClimbingStairs(cost):
    #   1.
    cost.append(0)

    #   2.
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])

"""
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

cost = [1,100,1,1,1,100,1,1,100,1]

print(minCostClimbingStairs(cost))