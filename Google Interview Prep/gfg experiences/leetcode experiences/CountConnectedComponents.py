'''
DFS visit all the connected vertices of the given vertex.

When iterating over all vertices, whenever we see unvisited node, it is because it was not visited by DFS done on vertices so far.

That means it is not connected to any previous nodes visited so far i.e it was not part of previous components.

Hence this node belongs to new component.

This means, before visiting this node, we just finished visiting all nodes previous component and that component is now complete.

So we need to increment component counter as we completed a component.

The idea is to use a variable count to store the number of connected components and do the following steps:

Initialize all vertices as unvisited.
For all the vertices check if a vertex has not been visited, then perform DFS on that vertex and increment the variable count by 1.
'''
class Graph:
	def __inti__(self,V):
		self.V = V
		self.adj = [[] for i in range(self.V)]

	#returns no of connected components
	def noOfconnComponents(self):
		visited = [False for i in range(self.V)]

		#stores no of conn components
		count = 0

		for v in range(self.V):
			if(visited[v] == False):
				self.dfs(v,visited)	
				count += 1

		return count

	#dfs helper function
	def dfs(self, V, visited):
		for i in self.adj[V]:
			if(not visited[i]):
				self.dfs(i,visited)


	#add edges
	def addEdge(self, v, w):
		self.adj[v].append(w)
		self.adj[w].append(v)
    
    
    # Driver code       
if __name__=='__main__':
     
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
     
    print(g.NumberOfconnectedComponents())
 
