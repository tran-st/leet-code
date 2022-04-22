def maxArea(height):
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(result, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1


    return result

    """
    [1,8,6,2,5,4,8,3,7]
       l
                   r

    result = 49
    area = 49
    """

"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Approach:

Brute force. Two pointers at each possible combination

Time    : O(n^2)
Space   : O(1)


Approach 2:

Two pointer. Increment/decrement the min of both pointers. Compute and store max area

Time    : O(n)
Space   : O(1)
"""

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))