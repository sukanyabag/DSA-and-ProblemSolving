class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #calc len of rows and cols
        rows = len(grid)
        cols = len(grid[0])
        
        #this marks an island as visited to avoid visiting it again
        visited = set()
        
        def dfs(r,c):
            '''
            base/edge cases
            1. r idx out of bound -> (r<0) or r == rows
            2. c idx out of bound -> (c<0) or c == cols
            3. if it's a waterbody -> grid[r][c] == 0
            4. if it's already visited -> (r,c) in visited
            '''
            if(r<0 
               or r == rows 
               or c<0 
               or c == cols 
               or grid[r][c] == 0 
               or (r,c) in visited):
                
                return 0
            
            visited.add((r,c))
            
            #dfs and calc area 
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        maxArea = 0
        
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea,dfs(r,c))
                    
        return maxArea
                
            
