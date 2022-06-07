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
            if not dfs(j, i):
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

"""
def valid_tree(n, edges):
    # Empty tree technically valid
    if not n:
        return True 

    # Initialize adjacency list
    adjacency = { i:[] for i in range(n) }

    # Fill adjacency list
    for vertex, edge in edges:
        adjacency[vertex].append(edge)
        adjacency[edge].append(vertex)

    # Track visited
    visited = set()

    def dfs(i, prev):
        # Loop detected
        if i in visited:
            return False

        visited.add(i)

        # Visit all children
        for vertex in adjacency[i]:
            # Don't visit if previous
            if vertex == prev:
                continue
            if not dfs(vertex, i):
                return False

    return dfs(0, -1) and n == len(visited)

Approach:

Try to visit each node. Check for loops. Track previous

Time    : O(E + V)
Space   : O(E + V)

Takeaway:

Understand graph traversal, dfs
"""

"""
400 million users x 300 bytes
120 billion bytes
120 gb per day
120 gb / 30 = 4 gb
4 gb / 4000
.001
1 MBs

120 gb x 400 days = 48,000 gb x 5 years = 250,000 gb = 250 tb
400 m tweets x 400 days = 160,000 m tweets x 5 years 800,000,000,000 tweets
"""