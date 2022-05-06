def encode(strs):
    result = ""

    for s in strs:
        result += str(len(s)) + "#" + s

    return result

def decode(str):
    result = []
    str_length = len(str)
    i = 0

    while i < str_length:
        # Find length of word. Could be a big number
        j = i
        while str[j] != "#":
            j += 1

        word_length = int(str[i : j])

        j += 1

        word = str[j : j + word_length]
        result.append(word)

        i = j + word_length

    return result

"""
1#I2#am2#an8#imposter
i
 j
"""

"""
Approach:

When encoding, need a way to seperate strings for decoding. Use number and delimiter

Time    : O(n)
Space   : O(n)
"""

strs = ["I", "am", "an", "imposter"]
print(encode(strs))

decode_me = "1#I2#am2#an8#imposter"
print(decode(decode_me))