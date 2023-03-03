
from graph_input import graph

def bfs(graph,startNode,goleNode):
    queue = []
    expanded = []
    queue.append(startNode)
    while queue:
        current_node = queue.pop(0)
        if current_node == goleNode:
            return expanded
        expanded.append(current_node)
        for child in graph[current_node]:
            queue.append(child)
    return expanded

startNode = 'A'
goleNode = 'B3'
path = bfs(graph,startNode,goleNode)
if path:
    print(path)
else:
    print("Couln't find the gole state.")

    
"""
1. BFS is Complete.
2. BFS is Optimal provided that all edges have equal weights.
3. Time Complexity: O(b^d); b = branching factor, d = depth of goal state
4. Space Complexity: O(b^d)
"""
"""
1. Completeness: Is it guaranteed that you will always find the goal state if goal state exists.
2. Optimality: Is it guaranteed that the solution that you found is most optimal?
3. Time Complexity: 
4. Space Complexity: 
"""
