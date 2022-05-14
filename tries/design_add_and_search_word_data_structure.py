class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, node):
            current = node

            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    for child in current.children.values():
                        print(child)
                        if dfs(i + 1, child):
                            return True

                    return False
                else:
                    if char not in current.children:
                        return False

                    current = current.children[char]

            return current.endOfWord

        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("mad"))

"""
Approach:

Trie. If char not exist in children, make new TrieNode. Set bool at end of word

Time    : O(26^n)
Space   : O(n)

Takeaway:

Understand tries, dfs. If wildcard, skip and check all children
"""