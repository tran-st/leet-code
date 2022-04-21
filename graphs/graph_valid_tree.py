def valid_tree(n, edges):
    adjacency = {}
    visited = set()

    for node1, node2 in edges: # Fill list
        if node1 not in adjacency:
            adjacency[node1] = []

        if node2 not in adjacency:
            adjacency[node2] = []

        adjacency[node1].append(node2)
        adjacency[node2].append(node1)

    def dfs(i, prev):
        if i in visited:
            return False

        visited.add(i)   

        for j in adjacency[i]:
            if j == prev: # Can ignore traversing to previous elements
                continue
            if not dfs(j):
                return False

        return True

    return dfs(0, -1) and n == len(visited)

"""
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Approach:

Adjacency list. DFS, track visited and previous. Check if tree is connected

Time    : O(e + v)
Space   : O(e + v)
"""

n = 5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

print(valid_tree(n, edges))