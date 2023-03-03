class Problem:
    def __init__(self):
        self.graph = {}
        self.takeGraph()

    def takeGraph(self):
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
        # print("masterList: ", masterList)
        for nodeList in masterList:
            # print("nodeList: ", nodeList)
            for node in nodeList:
                # node = node[1]
                numberOfChildren = int(input(f"No of children of {node[1]}: "))
                childrenList = []
                for x in range(numberOfChildren):
                    cost = int(input(f"Cost of child-{x+1}: "))
                    child = input(f"Child-{x+1}: ")
                    tu = (cost, child)
                    childrenList.append(tu)
                # print("childrenList: ", childrenList)
                graph[node[1]] = childrenList
                masterList.append(childrenList)
        self.graph = graph

p1 = Problem()
print(p1.graph)

# graph.sort(key = lambda x: x[0])