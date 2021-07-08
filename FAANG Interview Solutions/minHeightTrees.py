class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [x for x in range(n)]
        
        neighbors = [set() for x in range(n)] 
         
        # edges - [[1,0],[1,2],[1,3]]
        # nodes -  [0,1,2,3]
        # set storing edges-connections wrt each other - {1},{0,2,3},{1},{1}
        
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
                
        rem_nodes = n
        while rem_nodes > 2:
            rem_nodes -= len(leaves)
            temp = []
            
            for leaf in leaves:
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        temp.append(neighbor)
            leaves = temp
        return leaves
                    
                    
