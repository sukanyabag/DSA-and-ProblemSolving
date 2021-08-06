from collections import defaultdict

class Graph:
    def __init__(self, n_vertices):
        self.graph = defaultdict(list)
        self.n_vertices = n_vertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    #helper function for topological sort
    def topologicalSortUtil(self, vtx, visited,stack):
        visited.append(vtx)

        for i in self.graph[vtx]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)

        stack.insert(0,vtx)
    
    #main function
    def topologicalSort(self):  # time - O(V+E) , V = vertex, E = edges, space - O(V+E)

        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)


customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.topologicalSort()