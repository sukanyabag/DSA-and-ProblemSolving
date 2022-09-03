
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        #an empty graph is also a tree
        if not n:
            return True
          
        #create an adj list from nodes n
        adj = {i:[] for i in range(n)}

        #add edges to the nodes bidirectionally since its a undirected graph
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        #init visited set
        visited = set()

        #perform dfs 
        #we need an extra pointer prev to store the prev node - this helps us from false-positive cycles during backtracking 
        def dfs(i,prev):
            #if already visited return false
            if i in visited :
                return False
            #otherwise add to visited
            visited.add(i)

            #j is neighbor of every i
            for j in adj[i]:
                # if we already traversed j, ignore it
                if j == prev:
                    continue
                 # here j becomes current node and i prev
                 #also, whenever dfs cannot be done, we know we are stuck in a cycle/loop
                 # so we simply return a false
                if not dfs(j,i):
                    return False
            #otherwise we are good to go, return true
            return True
        #intiate dfs on the entire graph from i = 0, and initially we keep prev pointer as -1, as we can have a node value as 0
        #we return true iff length of visited == no of given nodes , as that signifies that every node in graph is connected
        return dfs(0,-1) and n==len(visited)

