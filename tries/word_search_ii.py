class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWords(self, word):
        current = self

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char] # Increment

        current.isEnd = True

def findWords(board, words):
    row_length = len(board)
    col_length = len(board[0])
    visited = set()
    result = set()
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    root = TrieNode()

    for word in words: # Add word list to trie
        root.addWords(word)

    def dfs(row, col, node, word):

        if (row not in range(row_length) or
            col not in range(col_length) or
            # (row, col) in visited or
            board[row][col] not in node.children):
            return

        char = board[row][col]

        visited.add((row, col))
        word += char # Valid char, add
        nextNode = node.children[char] # Progress trie

        if nextNode.isEnd: # Word found
            result.add(word)
            nextNode.isEnd = False

            if not node.children.keys():
                del node.children[char]

        for x, y in directions:
            dfs(row+x, col+y, nextNode, word)

        visited.remove((row,col))

    for i in range(row_length):
        for j in range(col_length):
            dfs(i, j, root, "")

    return result

"""
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]], 
                
                words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Approach:

Iterate each word, each char. See if grid char match. Check all 4 directions

Time    : O(cnm4^nm)
Space   : O(1)


Approach 2:

Add each word to a trie. For each grid char see if char exists in trie. Traverse trie

Time    : O(cnm)
"""

board = [["o","a","b","n"],
         ["o","t","a","e"],
         ["a","h","k","r"],
         ["a","f","l","v"]]

words =["oa","oaa"]

print(findWords(board, words))

"""
Approach:

Create prefix tree based on words. Backtrack dfs on each cell

Takeaway:

Understand prefix trees. Understand backtrack

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        current = self

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.endOfWord = True

    def searchWords(board, words):
        row_length = len(board)
        col_length = len(board[0])
        visited = set()
        result = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        root = TrieNode()

        for word in words:
            root.addWord(word)

        def dfs(row, col, trieNode, word):
            if (row not in range(row_length) or
                col not in range(col_length) or
                (row, col) in visited or
                board[row][col] not in trieNode.children):
                return False

            visited.add((row, col))

            c = board[row][col]
            word += trieNode.children[c]
            trieNode = trieNode.children[c]

            if trieNode.endOfWord:
                result.add(word)
                trieNode.endOfWord = False // Redundant

            if not node.children.keys():
                del node.children[char]

            for x, y in directions:
                dfs(row + x, col + y, trieNode, word)

            visited.remove(row, col)


        for i in range(row_length):
            for j in range(row_length):
                dfs(i, j, root, "")


"""