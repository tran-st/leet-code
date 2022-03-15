"""
Approach 3:

[7,1,5,3,6,4]
   l
       r

current_profit = 4
maximum_profit = 4

Two pointers. If left is < right, find their profit and update the max. If right is ever 
less than left, increment left all the way to the right

1.  Two pointers
2.  While right is in range of array
3.  If left is less than right, find new profit
4.  Update max
5.  Else, set left = right
6.  Increment right

Time    : O(n)
Space   : O(1)
"""
def maxProfit(prices):
    #   1.
    left, right = 0, 1
    current_profit = 0
    max_profit = 0

    #   2.
    while right in range(right, len(prices)):
        if prices[left] < prices[right]: #  3.
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit) #  4.
        else:
            left = right #  5.
        
        right += 1 #    6.

    return max_profit
"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Approach 1:

Brute force. Buy and sell at every possible starting point

Time    : O(n ^ 2)
Space   : O(1)


Approach 2:

Sort the array. Create a new array where index = price and value = day. Loop through that array and find
the first and last existing elements. Return their values

Time    : O(n log n)
Space   : O(n)
"""

prices = [7,1,5,3,6,4]

print(maxProfit(prices))