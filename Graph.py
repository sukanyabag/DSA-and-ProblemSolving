class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


    def bfs(self, vertex):  # time - O(V+E) , V = vertex, E = edges, space - O(V+E)
        #create list to keep track of visited nodes
        visited = [vertex]

        #queue initialized with the vertex
        queue = [vertex]

        while queue:
            deqVertex = queue.pop(0)
            print(deqVertex)
            for adjVertex in self.gdict[deqVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    queue.append(adjVertex)

    def dfs(self, vertex): # time - O(V+E) , V = vertex, E = edges, space - O(V+E)
        visited = [vertex]
        stack = [vertex]

        while stack:
            popVertex = stack.pop()
            print(popVertex)

            for adjVertex in self.gdict[popVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    stack.append(adjVertex)



#create graph by declaring dictionary
customDict =  {
               "a" : ["b","c"],
               "b" : ["a","d","e"],
               "c" : ["a","e"],
               "d" : ["b","e","f"],
               "e" : ["d","f"],
               "f" : ["d","e"]
               }

graph = Graph(customDict)
#graph.addEdge("d", "e")
print(graph.gdict)
graph.bfs("a")
print("------------")
graph.dfs("a")
