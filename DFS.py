from graph_input import graph

expanded = []
def dfs(node):
    global expanded
    if node not in expanded:
        expanded.append(node)
        for child in graph[node]:
            dfs(child)
    return expanded

print(dfs("A"))

"""
1. DFS is Complete only none of the lag is going infinite.
2. DFS is Not Optimal.
3. Time Complexity: O(b^d); b = branching factor, d = depth of goal state
4. Space Complexity: O(d)
"""