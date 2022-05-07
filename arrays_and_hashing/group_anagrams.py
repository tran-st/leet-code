def groupAnagrams(strs):
    sorted_hash = {}
    result = []

    for word in strs:
        sorted_word = "".join(sorted(word))

        if sorted_word not in sorted_hash:
            sorted_hash[sorted_word] = []

        sorted_hash[sorted_word].append(word)

    for word_list in sorted_hash.values():
        result.append(word_list)

    return result

"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Approach:

"eat","tea","tan","ate","nat","bat"
       l
             r

Loop through strs. Copy current string, sort it. Add it's key to a hash. Add to result

Time    : O(n log n * m)
Space   : O(n)
"""

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))