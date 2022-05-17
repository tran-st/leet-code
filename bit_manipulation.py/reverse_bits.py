def reverseBits(n):
    result = 0

    for i in range(32):
        bit = (n >> i) & 1
        result = result | (bit << (31 * i))
    
    return result

"""
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Approach:

Get the first bit of n with & operator. Shift i times.
"""