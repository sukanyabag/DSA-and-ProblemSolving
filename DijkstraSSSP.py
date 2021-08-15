from collections import defaultdict

#initialize weighted graph class for dijkstra's algo
class Graph:
    def __init__(self):
        #vertices
        self.nodes = set()
        #edges
        self.edges = defaultdict(list)
        #distances/ weights
        self.distances = {}

    def addNode(self, val):
        #keep vertices inside nodes
        self.nodes.add(val)

    #set distances bw nodes(edges with distances)
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

#define Dijkstra's algorithm
def dijkstra(graph, initial_node): #time - O(V^2), space = O(E)
    #mark vertices as visited
    visited = {initial_node : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None

        #nested loop to find min node
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        #remove already visited nodes
        nodes.remove(minNode)

        currWeight = visited[minNode] 
        
        #if (current node)    > (calculated)     => update (current node) = (calculated)
        #                cost              cost                        cost            cost
        for edge in graph.edges[minNode]:
            #calculated cost
            weight = currWeight + graph.distances[(minNode, edge)]
            
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print(dijkstra(customGraph, "A"))


