def eventualSafeNodes(graph):
    graph_length = len(graph)
    safe_nodes = {}
    result = []

    def dfs(i):
        if i in safe_nodes: # Already visisted
            return safe_nodes[i]

        safe_nodes[i] = False # Visit it

        for neighbor in graph[i]:
            if not dfs(neighbor): # Only one needs to be not safe
                return safe_nodes[i]

        safe_nodes[i] = True # All are safe

        return safe_nodes[i]

    for i in range(graph_length):
         if dfs(i):
             result.append(i)

    return result

"""
dfs(0)
safe_nodes[0] = False
dfs(0)->dfs(1)
safe_nodes[1] = False
dfs(0)->dfs(1)->dfs(2)
safe_nodes[2] = False
dfs(0)->dfs(1)->dfs(2)->dfs(5)
safe_nodes[5] = True
dfs(0)->dfs(1)->dfs(2)
safe_nodes[2] = True
dfs(0)->dfs(1)
dfs(0)->dfs(1)->dfs(3)
safe_nodes[3] = False
dfs(0)->dfs(1)->dfs(3)->dfs(0)
return safe_nodes[0] (False)
dfs(0)->dfs(1)->dfs(3)
return safe_nodes[3] (False)
dfs(0)->dfs(1)
return safe_nodes[1] (False)
dfs(0)
return safe_nodes[0] (False)
"""

"""
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Approach:

DFS. Visit node's neighbors. Add to hash map. If all neighbors return true, node is safe

Time    : O(e + v)
Space   : O(v)
"""

graph = [[1,2],[2,3],[5],[0],[5],[],[]]

print(eventualSafeNodes(graph))