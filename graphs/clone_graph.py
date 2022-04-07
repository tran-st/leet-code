from node_class import Node

def cloneGraph(node):
    clone_hash = {}

    def dfs(node):
        if node in clone_hash:
            return clone_hash[node]

        clone = Node(node.val)
        clone_hash[node] = clone

        for n in node.neighbors:
            clone.neighbors.append(dfs(n))
        

        return clone

    result =  dfs(node) if node else None


    return result

"""
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


Approach:

DFS. Store copied node in hash. Make sure neighbors are copied

Time    : O(n)
Space   : O(n)
"""

adjList = [[2,4],[1,3],[2,4],[1,3]]
node = Node(2)
node.neighbors.append(Node(4))

print(cloneGraph(node))