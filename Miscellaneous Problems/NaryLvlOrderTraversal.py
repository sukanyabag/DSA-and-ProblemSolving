class Node:
    def __init__(self, val=None, children = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #base
        if not root:
            return []
        
        #init queue and res
        q = deque([root])
        res = []
        
        #iterate
        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                
                for child in node.children:
                    q.append(child)
                    
                level += [node.val]
            res += [level]
            
        return res
        
