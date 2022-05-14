class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children[char]:
                return False

            current = current.children[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert("a")
print(obj.search("a"))

"""
Approach:

Trie() val and endOfWord
insert(word) append val into children
search(word) search all children until end of string. Check endOfWord
startsWith(word) same as search without endOfWord

class TrieNode:
    def __init__():
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__():
        self.root = TrieNode()

    def insert(word):
        current = self.root

        for c in word:
            if c not in current.children:
                currennt.children[c] = TrieNode()

            current = current.children[c]

        current.endOfWord = True

    def search(word):
        current = self.root

        for c in word:
            if c not in current.children:
                return False

            current = current.children[c]

        return current.endOfWord

    def startsWith(prefix):
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False

            current = current.children[c]

        return True
"""