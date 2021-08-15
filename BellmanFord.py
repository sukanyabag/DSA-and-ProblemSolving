class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s,e,w): #start = s, end = e , weight = w
        self.graph.append([s,e,w])

    def add_node(self,value):
        self.nodes.append(value)

    def print_sol(self,dist):
        print("Vertex distance from source: ")
        for key, value in dist.items():
            print(' ' + key , ':  ', value)

    def bellman_ford(self, src_vtx): #time - O(EV), space = O(V)
        dist = {i : float("Inf") for i in self.nodes}
        dist[src_vtx] =  0

        for _ in range(self.V-1):
            for s,e,w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[e]:
                    dist[e] = dist[s] + w

        #for negative cycle
        for s,e,w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[e]:
                    dist[e] = dist[s] + w

        self.print_sol(dist)

g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellman_ford("E")