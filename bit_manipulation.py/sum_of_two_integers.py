def getSum(a, b):
    while b != 0:
        temp = (a & b) << 1
        a = a ^ b
        b = temp
    
    return a

"""
Input: a = 1, b = 2
Output: 3


2    10
3    11
5   101

1    1
2   10  
3   11

Approach:

XOR to add numbers. & to carry numbers. Repeat while sum not 0

Time    : O(1)
Space   : O(1)
"""