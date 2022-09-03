"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        #edge 
        if node is None:
            return None
        
        def CloneBydfs(node):
            #if already present return 
            if node in oldToNew:
                return oldToNew[node]
            
            #otherwise create deep copy
            copy = Node(node.val)
            
            #add deepcopy as key to orignl node in map oldToNew {node:copy}
            oldToNew[node] = copy
            
            #check neighbors by dfs on each neighbor of node.neighbors and add them to copy
            for neighbor in node.neighbors:
                copy.neighbors.append(CloneBydfs(neighbor))
                
            return copy
        
        return CloneBydfs(node)
        
