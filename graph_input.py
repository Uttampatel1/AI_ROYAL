
def takeGraph():
    graph = {}
    root = input("Enter root node: ")
    noOfChildren = int(input("No of children: "))
    children = []
    # tu  = tuple()
    for x in range(noOfChildren):  
        cost = int(input(f"Cost of child-{x+1}: ")) 
        child = input(f"Child-{x+1}: ")    
        tu = (cost, child)
        children.append(tu)

    graph[root] = children
    masterList = list(graph.values())
    print("masterList: ", masterList)
    for nodeList in masterList:
        print("nodeList: ", nodeList)
        for node in nodeList:
            # node = node[1]
            numberOfChildren = int(input(f"No of children of {node[1]}: "))
            childrenList = []
            for x in range(numberOfChildren):
                cost = int(input(f"Cost of child-{x+1}: "))
                child = input(f"Child-{x+1}: ")
                tu = (cost, child)
                childrenList.append(tu)
            print("childrenList: ", childrenList)
            graph[node[1]] = childrenList
            masterList.append(childrenList)
    return graph

graph = {
    'A' : [(1,'B1'), (2,'B2'), (3,'B3')],
    'B1' : ['C1', 'C2'],
    'B2' : ['C3'],
    'B3' : ['C4', 'C5'],
    'C1' : ['D1'],
    'C2' : [],
    'C3' : ['D2', 'D3'],
    'C4' : [],
    'C5' : ['D4'],
    'D1' : [],
    'D2' : [],
    'D3' : [],
    'D4' : []
}
if __name__ == "__main__":
    print(takeGraph())

## Graphs with Python: Overview and Best Libraries :
## https://towardsdatascience.com/graphs-with-python-overview-and-best-libraries-a92aa485c2f8
## https://www.analyticsvidhya.com/blog/2018/08/introduction-to-graph-theory-network-analysis-python-codes/
## https://www.geeksforgeeks.org/graph-and-its-representations/
