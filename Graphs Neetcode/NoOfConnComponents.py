'''
SIMILAR TO NUMBER OF PROVINCES 
INSTEAD OF EDGES, ADJANCENCY MATRIX IS GIVEN

SOLUTIONS FOR BOTH ADJ MATX AS WELL AS EDGES BELOW
'''

#ADJ MATX
class Solution:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
        
#EDGES
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = {i:[] for i in range(n)}
        visited = set()
        for n1,n2 in edges:
            dic[n1].append(n2)
            dic[n2].append(n1)
        
        def dfs(node):
            if node not in visited:
              visited.add(node)
              dfs(e,node)
              
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
